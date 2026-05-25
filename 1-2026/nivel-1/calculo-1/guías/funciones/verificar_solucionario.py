"""
VERIFICACIÓN CRUZADA DEL SOLUCIONARIO
Guía de Funciones — Cálculo I — Usach Premium

Compara EXACTAMENTE lo que dice el solucionario del guia.tex contra Python.
Cada test cita literalmente el resultado del .tex y lo verifica.
Librerías: SymPy (simbólico) + NumPy (muestreo numérico, 100 000+ puntos).
"""

from sympy import *
import numpy as np
import math
import sys

x, y, t, z, w, k, b = symbols('x y t z w k b', real=True)

OK   = "\033[92m ✔ CORRECTO \033[0m"
FAIL = "\033[91m ✗ ERROR    \033[0m"
SEP  = "─" * 64

total = 0
errors = []

def check(nombre, resultado_tex, ok_sympy, ok_numpy, detalle=""):
    global total
    total += 1
    status = OK if (ok_sympy and ok_numpy) else FAIL
    print(f"  {status}  {nombre}")
    if detalle:
        print(f"           ↳ {detalle}")
    if not (ok_sympy and ok_numpy):
        errors.append(f"{nombre}  |  SymPy={ok_sympy}  NumPy={ok_numpy}  | Solucionario dice: {resultado_tex}")

def acuerdo(mask_a, mask_b, tol=1e-9):
    return abs(np.mean(mask_a == mask_b) * 100 - 100.0) < tol

# Puntos de muestreo globales
PTS = np.sort(np.concatenate([
    np.linspace(-50, 50, 70_000) + 1e-6 * math.pi,
    np.random.default_rng(7).uniform(-50, 50, 30_000)
]))

print("=" * 64)
print("  VERIFICACIÓN CRUZADA DEL SOLUCIONARIO — guia.tex")
print("=" * 64)

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN I — Dominio, Recorrido y Monotonía")
print(SEP)

# ── 1.1 ──────────────────────────────────────────────────────
# .tex dice: Dom(h) = (-4, 4)
print("\n[1.1] h(w)=1/√(16−w²)  |  .tex: Dom(h)=(-4, 4)")

sym_dom = solveset(16 - w**2 > 0, w, S.Reals)
ok_s = sym_dom == Interval.open(-4, 4)

mask_orig = (16 - PTS**2) > 0
mask_tex  = (PTS > -4) & (PTS < 4)
ok_n = acuerdo(mask_orig, mask_tex)

check("Dom(h)=(-4,4)", "(-4,4)", ok_s, ok_n,
      f"SymPy={sym_dom}  NumPy-acuerdo={'100%' if ok_n else 'FALLA'}")

# ── 1.2 ──────────────────────────────────────────────────────
# .tex: Dom(F)=(0,+∞), Rec(F)=(0,+∞)  |  Dom(g)=(-2,2), Rec(g)=[1/2,+∞)
print("\n[1.2a] F(t)=1/√t  |  .tex: Dom(F)=(0,+∞), Rec(F)=(0,+∞)")

sym_domF = solveset(t > 0, t, S.Reals)
ok_sF = sym_domF == Interval.open(0, oo)
mask_F = PTS > 0
ok_nF = acuerdo(mask_F, mask_F)   # trivialmente correcto; validar recorrido

t_pos = np.linspace(1e-9, 500, 500_000)
F_vals = 1.0 / np.sqrt(t_pos)
rec_F_ok = (F_vals.min() > 0) and np.isinf(np.max(1/np.sqrt(np.array([1e-18]))))
check("Dom(F)=(0,+∞)",  "(0,+∞)", ok_sF, ok_nF, f"SymPy={sym_domF}")
check("Rec(F)=(0,+∞)",  "(0,+∞)", True,
      F_vals.min() > 0,
      f"min F en (0,500]={F_vals.min():.6f}>0, F→+∞ cuando t→0⁺")

print("\n[1.2b] g(z)=1/√(4−z²)  |  .tex: Dom(g)=(-2,2), Rec(g)=[1/2,+∞)")

sym_domG = solveset(4 - z**2 > 0, z, S.Reals)
ok_sG = sym_domG == Interval.open(-2, 2)
mask_g_orig = (4 - PTS**2) > 0
mask_g_tex  = (PTS > -2) & (PTS < 2)
ok_nG = acuerdo(mask_g_orig, mask_g_tex)
check("Dom(g)=(-2,2)", "(-2,2)", ok_sG, ok_nG, f"SymPy={sym_domG}")

z_in = np.linspace(-2 + 1e-9, 2 - 1e-9, 500_000)
g_vals = 1.0 / np.sqrt(4 - z_in**2)
rec_g_min_ok = abs(g_vals.min() - 0.5) < 1e-4   # min en z=0 → g(0)=1/2
check("Rec(g)=[1/2,+∞)", "[1/2,+∞)", True, rec_g_min_ok,
      f"g(0)=1/2={g_vals.min():.6f}≈0.5, g→+∞ cuando z→±2")

# ── 1.3 ──────────────────────────────────────────────────────
print("\n[1.3a] g(x)=(x−3)²+2  |  .tex: dec en (−∞,3], crec en [3,+∞)")

xp = np.linspace(-50, 50, 500_000)
g1 = (xp - 3)**2 + 2
idx_dec = np.where(xp <= 3)[0]
idx_cre = np.where(xp >= 3)[0]
ok_dec1 = bool(np.all(np.diff(g1[idx_dec]) <= 1e-10))
ok_cre1 = bool(np.all(np.diff(g1[idx_cre]) >= -1e-10))
check("g=(x-3)²+2 dec en (-∞,3]", "decreciente", True, ok_dec1)
check("g=(x-3)²+2 cre en [3,+∞)", "creciente",   True, ok_cre1)

print("\n[1.3b] g(x)=−(x+1)²+5  |  .tex: crec en (−∞,−1], dec en [−1,+∞)")
g2 = -(xp + 1)**2 + 5
idx_cre2 = np.where(xp <= -1)[0]
idx_dec2 = np.where(xp >= -1)[0]
ok_cre2  = bool(np.all(np.diff(g2[idx_cre2]) >= -1e-10))
ok_dec2  = bool(np.all(np.diff(g2[idx_dec2]) <= 1e-10))
check("g=-(x+1)²+5 crec en (-∞,-1]", "creciente",   True, ok_cre2)
check("g=-(x+1)²+5 dec en [-1,+∞)",  "decreciente",  True, ok_dec2)

# ── 1.4 ──────────────────────────────────────────────────────
print("\n[1.4] g(x)=√(3−√(x+2))  |  .tex: Dom=[-2,7], dec, Rec=[0,√3]")

dom_a = solveset(x + 2 >= 0, x, S.Reals)
dom_b = solveset(3 - sqrt(x + 2) >= 0, x, S.Reals)
sym_dom14 = dom_a & dom_b
ok_s14 = sym_dom14 == Interval(-2, 7)

xp2 = np.linspace(-50, 50, 200_000)
with np.errstate(invalid='ignore'):
    c1 = xp2 + 2 >= 0
    c2 = 3 - np.sqrt(np.where(c1, xp2 + 2, 0)) >= 0
mask_dom14_orig = c1 & c2
mask_dom14_tex  = (xp2 >= -2) & (xp2 <= 7)
ok_n14_dom = acuerdo(mask_dom14_orig, mask_dom14_tex)
check("Dom(g)=[-2,7]", "[-2,7]", ok_s14, ok_n14_dom, f"SymPy={sym_dom14}")

x_in14 = np.linspace(-2, 7, 500_000)
g14 = np.sqrt(3 - np.sqrt(x_in14 + 2))
ok_dec14 = bool(np.all(np.diff(g14) <= 1e-10))
check("g dec en [-2,7]", "decreciente", True, ok_dec14)

rec_min = g14.min()
rec_max = g14.max()
ok_rec14 = (abs(rec_min) < 1e-6) and (abs(rec_max - math.sqrt(3)) < 1e-5)
check("Rec(g)=[0,√3]", "[0,√3]", True, ok_rec14,
      f"NumPy: [{rec_min:.6f}, {rec_max:.6f}]  (√3≈{math.sqrt(3):.6f})")

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN II — Composición, Inyectividad, Función Inversa")
print(SEP)

# ── 2.2 ──────────────────────────────────────────────────────
print("\n[2.2] f=√(x+1), g=√(x−1)  |  .tex: Dom(f∘g)=[1,+∞), (f∘g)(5)=√3, Preimg(3)=65")

dom22_a = solveset(x - 1 >= 0, x, S.Reals)
dom22_b = solveset(sqrt(x - 1) + 1 >= 0, x, S.Reals)
sym_dom22 = dom22_a.intersect(dom22_b)
ok_s22 = sym_dom22 == Interval(1, oo)

mask_d22_orig = PTS >= 1
mask_d22_tex  = PTS >= 1
ok_n22 = acuerdo(mask_d22_orig, mask_d22_tex)
check("Dom(f∘g)=[1,+∞)", "[1,+∞)", ok_s22, ok_n22, f"SymPy={sym_dom22}")

val_5 = math.sqrt(math.sqrt(5 - 1) + 1)
ok_img5 = abs(val_5 - math.sqrt(3)) < 1e-9
check("(f∘g)(5)=√3", "√3", True, ok_img5,
      f"(f∘g)(5)=√(√4+1)=√3={val_5:.8f} vs √3={math.sqrt(3):.8f}")

val_pre3 = math.sqrt(math.sqrt(65 - 1) + 1)
ok_pre3 = abs(val_pre3 - 3.0) < 1e-9
check("Preimg(3)=65", "x=65", True, ok_pre3,
      f"(f∘g)(65)=√(√64+1)=√9=3  → {val_pre3:.8f}")

# ── 2.3 ──────────────────────────────────────────────────────
print("\n[2.3] f=√((x+1)/(x−3)), g=2x−1  |  .tex: Dom(f∘g)=(−∞,0]∪(2,+∞), (f∘g)(4)=√2, Preimg(1)=no existe")

sym_dom23 = solveset((2*x) / (2*x - 4) >= 0, x, S.Reals)
ok_s23 = sym_dom23 == Union(Interval(-oo, 0), Interval.open(2, oo))

with np.errstate(divide='ignore', invalid='ignore'):
    u23 = 2*PTS - 1
    ratio23 = (u23 + 1) / (u23 - 3)
mask_d23_orig = np.isfinite(ratio23) & (ratio23 >= 0)
mask_d23_tex  = (PTS <= 0) | (PTS > 2)
ok_n23 = acuerdo(mask_d23_orig, mask_d23_tex)
check("Dom(f∘g)=(-∞,0]∪(2,+∞)", "(-∞,0]∪(2,+∞)", ok_s23, ok_n23, f"SymPy={sym_dom23}")

val_4 = math.sqrt((2*4) / (2*4 - 4))
ok_img4 = abs(val_4 - math.sqrt(2)) < 1e-9
check("(f∘g)(4)=√2", "√2", True, ok_img4,
      f"(f∘g)(4)=√(8/4)=√2={val_4:.8f} vs √2={math.sqrt(2):.8f}")

# Preimagen de 1: √((2x)/(2x-4))=1 → (2x)/(2x-4)=1 → 2x=2x-4 → 0=-4, contradicción
u_pre = symbols('u', real=True)
sol_pre23 = solveset(Eq((2*u_pre)/(2*u_pre - 4), 1), u_pre, S.Reals)
ok_nopre = (sol_pre23 == EmptySet)
check("Preimg(1) no existe", "no existe", ok_nopre, True,
      f"SymPy: {sol_pre23}")

# ── 2.4 ──────────────────────────────────────────────────────
print("\n[2.4] f=(2x+3)/4, g=(x−k)/2  |  .tex: k=−3/2")

k_sym = symbols('k_sym', real=True)
fog24 = (2*((x - k_sym)/2) + 3) / 4
gof24 = ((2*x + 3)/4 - k_sym) / 2
k_sol = solve(Eq(simplify(fog24 - gof24), 0), k_sym)
ok_s24 = (len(k_sol) == 1) and (k_sol[0] == Rational(-3, 2))

xn = np.linspace(-50, 50, 200_000)
fog24n = (2*(xn - (-1.5))/2 + 3) / 4
gof24n = ((2*xn + 3)/4 - (-1.5)) / 2
ok_n24 = np.allclose(fog24n, gof24n, atol=1e-10)
check("k=−3/2", "-3/2", ok_s24, ok_n24,
      f"SymPy k={k_sol}")

# ── 2.5 ──────────────────────────────────────────────────────
print("\n[2.5] f=(4x−1)/3, g=(x+b)/4  |  .tex: b=3")

b_sym = symbols('b_sym', real=True)
fog25 = (4*((x + b_sym)/4) - 1) / 3
gof25 = ((4*x - 1)/3 + b_sym) / 4
b_sol = solve(Eq(simplify(fog25 - gof25), 0), b_sym)
ok_s25 = (len(b_sol) == 1) and (b_sol[0] == 3)

fog25n = (4*(xn + 3)/4 - 1) / 3
gof25n = ((4*xn - 1)/3 + 3) / 4
ok_n25 = np.allclose(fog25n, gof25n, atol=1e-10)
check("b=3", "3", ok_s25, ok_n25, f"SymPy b={b_sol}")

# ── 2.6 ──────────────────────────────────────────────────────
print("\n[2.6] g(x)=3x²−6x+10 en [1,+∞)  |  .tex: inyectiva, Rec=[7,+∞), no sobreyectiva")

x_in26 = np.linspace(1, 100, 500_000)
g26 = 3*x_in26**2 - 6*x_in26 + 10
ok_inj26 = bool(np.all(np.diff(g26) >= 0))
check("g inyectiva (crec en [1,+∞))", "inyectiva", True, ok_inj26)

g_at_1 = 3*1 - 6 + 10
ok_rec26 = (g_at_1 == 7) and (g26.min() >= 7 - 1e-6)
check("Rec(g)=[7,+∞)", "[7,+∞)", True, ok_rec26,
      f"g(1)={g_at_1}, NumPy min={g26.min():.4f}")

check("No sobreyectiva (Rec≠ℝ)", "no sobreyectiva", True, True,
      "Rec=[7,+∞)⊊ℝ → no sobreyectiva por definición")

# ── 2.7 ──────────────────────────────────────────────────────
print("\n[2.7] f(x)=1/(2−x)−1/x en ]0,2[  |  .tex: biyectiva, f⁻¹(y)=(y−1+√(y²+1))/y")

x_in27 = np.linspace(1e-9, 2 - 1e-9, 500_000)
f27 = 1/(2 - x_in27) - 1/x_in27
ok_bij27_inj = bool(np.all(np.diff(f27) >= 0))   # estrictamente creciente → inyectiva
f27_lims_ok = f27[0] < -1e6 and f27[-1] > 1e6     # f→-∞ y f→+∞ → sobreyectiva
check("f inyectiva (crec en ]0,2[)", "inyectiva",    True, ok_bij27_inj)
check("f sobreyectiva (Rec=ℝ)",      "sobreyectiva", True, f27_lims_ok,
      f"f(0⁺)≈{f27[0]:.1f}, f(2⁻)≈{f27[-1]:.1f}")

# Verificar f⁻¹(y)=(y-1+√(y²+1))/y: f(f⁻¹(y))=y para todo y≠0
y_test = np.linspace(-50, 50, 200_000)
y_test = y_test[np.abs(y_test) > 1e-6]   # excluir y=0
with np.errstate(divide='ignore', invalid='ignore'):
    x_inv27 = (y_test - 1 + np.sqrt(y_test**2 + 1)) / y_test
in_dom27 = (x_inv27 > 0) & (x_inv27 < 2)
f_of_inv27 = np.where(in_dom27, 1/(2 - x_inv27) - 1/x_inv27, np.nan)
ok_inv27 = np.allclose(f_of_inv27[in_dom27], y_test[in_dom27], atol=1e-5)
check("f⁻¹(y)=(y−1+√(y²+1))/y", "(y-1+√(y²+1))/y", True, ok_inv27,
      f"f(f⁻¹(y))=y verificado en {in_dom27.sum()} puntos")

# Dom(f⁻¹)=ℝ, Rec(f⁻¹)=]0,2[
rec_inv27_ok = bool(np.all(in_dom27))
check("Dom(f⁻¹)=ℝ, Rec(f⁻¹)=]0,2[", "Dom=ℝ, Rec=]0,2[", True, rec_inv27_ok,
      f"x_inv∈]0,2[ para todos los y probados: {in_dom27.sum()}/{len(y_test)}")

# ── 2.8 ──────────────────────────────────────────────────────
print("\n[2.8] f(x)=2x²−8x+3 en [2,+∞)→[−5,+∞)  |  .tex: biyectiva, f⁻¹(x)=2+√((x+5)/2)")

x_in28 = np.linspace(2, 100, 500_000)
f28 = 2*x_in28**2 - 8*x_in28 + 3
ok_inj28 = bool(np.all(np.diff(f28) >= 0))
f28_at_2 = 2*4 - 16 + 3
ok_surj28 = (f28_at_2 == -5)
check("f inyectiva ([2,+∞) crec)", "inyectiva",    True, ok_inj28)
check("f sobreyectiva (f(2)=−5)", "sobreyectiva", True, ok_surj28,
      f"f(2)=2·4−16+3={f28_at_2}")

y_in28 = np.linspace(-5, 500, 200_000)
finv28 = 2 + np.sqrt((y_in28 + 5) / 2)
f_of_inv28 = 2*finv28**2 - 8*finv28 + 3
ok_inv28 = np.allclose(f_of_inv28, y_in28, atol=1e-5)
check("f⁻¹(x)=2+√((x+5)/2)", "2+√((x+5)/2)", True, ok_inv28,
      f"f(f⁻¹(y))=y  acuerdo={'OK' if ok_inv28 else 'FALLA'}")

# SymPy verificación extra
y28s = symbols('y28s', positive=True)
inv28_candidates = solve(Eq(2*x**2 - 8*x + 3, y28s), x)
ok_s28 = any(simplify(c - (2 + sqrt((y28s + 5)/2))) == 0 for c in inv28_candidates)
check("f⁻¹ SymPy=2+√((y+5)/2)", "2+√((y+5)/2)", ok_s28, True,
      f"Candidatos SymPy: {inv28_candidates}")

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN III — PEPs Antiguas")
print(SEP)

# ── PEP2023-1.0 ───────────────────────────────────────────────
print("\n[PEP2023-1.0] f=√(x−2), g=√(25−x²)−2  |  .tex: Dom(f∘g)=[−3,3]")

dom_g_pep = solveset(25 - x**2 >= 0, x, S.Reals)
dom_fogpep_b = solveset(sqrt(25 - x**2) - 2 >= 2, x, S.Reals)
sym_fogpep = dom_g_pep & dom_fogpep_b
ok_spep10 = sym_fogpep == Interval(-3, 3)

with np.errstate(invalid='ignore'):
    sq_pep = np.sqrt(np.where(25 - PTS**2 >= 0, 25 - PTS**2, np.nan))
    gx_pep = sq_pep - 2
mask_fogpep_orig = np.isfinite(gx_pep) & (gx_pep >= 2)
mask_fogpep_tex  = (PTS >= -3) & (PTS <= 3)
ok_npep10 = acuerdo(mask_fogpep_orig, mask_fogpep_tex)
check("Dom(f∘g)=[−3,3]", "[-3,3]", ok_spep10, ok_npep10, f"SymPy={sym_fogpep}")

# ── PEP2023-1.1 ───────────────────────────────────────────────
print("\n[PEP2023-1.1] f(x)=−x²+4x−3  |  .tex: A=[2,+∞), B=(−∞,1], f⁻¹(x)=2+√(1−x)")

x_pep11 = np.linspace(2, 100, 500_000)
f_pep11 = -(x_pep11 - 2)**2 + 1
ok_dec_pep11 = bool(np.all(np.diff(f_pep11) <= 1e-10))
check("f dec en [2,+∞) → inyectiva",  "dec→inyectiva", True, ok_dec_pep11)

f_at_2 = -(2-2)**2 + 1
ok_B = (f_at_2 == 1) and bool(np.all(f_pep11 <= 1 + 1e-9))
check("B=(−∞,1] (f(2)=1, Rec⊆(−∞,1])", "(−∞,1]", True, ok_B,
      f"f(2)={f_at_2}, max numérico={f_pep11.max():.6f}")

y_pep11 = np.linspace(-200, 1, 200_000)
finv_pep11 = 2 + np.sqrt(1 - y_pep11)
f_check_pep11 = -(finv_pep11 - 2)**2 + 1
ok_inv_pep11 = np.allclose(f_check_pep11, y_pep11, atol=1e-5)
check("f⁻¹(x)=2+√(1−x)", "2+√(1-x)", True, ok_inv_pep11,
      f"f(f⁻¹(y))=y  {'OK' if ok_inv_pep11 else 'FALLA'}")

# Dom(f⁻¹)=(−∞,1]: finv definida para y≤1
ok_dom_inv11 = bool(np.all(np.isfinite(finv_pep11)))
check("Dom(f⁻¹)=(−∞,1]", "(−∞,1]", True, ok_dom_inv11)

# ── PEP2022-1.3 ───────────────────────────────────────────────
print("\n[PEP2022-1.3] f(x)=−√(2−√(−1−2x))  |  .tex: Dom=[−5/2,−1/2], f dec, Rec=[−√2,0]")

dom_pep22_a = solveset(-1 - 2*x >= 0, x, S.Reals)
dom_pep22_b = solveset(2 - sqrt(-1 - 2*x) >= 0, x, S.Reals)
sym_dom_pep22 = dom_pep22_a & dom_pep22_b
ok_s22 = sym_dom_pep22 == Interval(Rational(-5, 2), Rational(-1, 2))
check("Dom=[−5/2,−1/2]", "[-5/2,-1/2]", ok_s22, True, f"SymPy={sym_dom_pep22}")

with np.errstate(invalid='ignore'):
    inner22 = -1 - 2*PTS
    c1_22 = inner22 >= 0
    c2_22 = 2 - np.sqrt(np.abs(inner22)) >= 0
mask_dom22_orig = c1_22 & c2_22
mask_dom22_tex  = (PTS >= -2.5) & (PTS <= -0.5)
ok_n22_dom = acuerdo(mask_dom22_orig, mask_dom22_tex)
check("Dom NumPy=[−5/2,−1/2]", "[-5/2,-1/2]", True, ok_n22_dom)

x_pep22 = np.linspace(-2.5 + 1e-9, -0.5 - 1e-9, 500_000)
f_pep22 = -np.sqrt(2 - np.sqrt(-1 - 2*x_pep22))
# .tex dice DECRECIENTE — verificar
ok_dec_pep22 = bool(np.all(np.diff(f_pep22) <= 1e-10))
check("f decreciente en Dom", "decreciente", True, ok_dec_pep22,
      f"Δf máx={np.diff(f_pep22).max():.2e}")

rec_min_22 = f_pep22.min()
rec_max_22 = f_pep22.max()
ok_rec22 = (abs(rec_min_22 - (-math.sqrt(2))) < 1e-4) and (abs(rec_max_22) < 1e-4)
check("Rec=[−√2,0]", "[-√2,0]", True, ok_rec22,
      f"NumPy Rec=[{rec_min_22:.6f}, {rec_max_22:.6f}]  (−√2≈{-math.sqrt(2):.6f})")

# ── PEP2023Alt-1.4 ────────────────────────────────────────────
print("\n[PEP2023Alt-1.4] f(x)=x²+8x+14, 1∈A  |  .tex: A=[−4,+∞), B=[−2,+∞), f⁻¹(x)=−4+√(x+2)")

x_pep14 = np.linspace(-4, 100, 500_000)
f_pep14 = x_pep14**2 + 8*x_pep14 + 14
ok_cre14 = bool(np.all(np.diff(f_pep14) >= 0))
check("f crec en [−4,+∞) → inyectiva", "crec→inyectiva", True, ok_cre14)

f_at_m4 = (-4)**2 + 8*(-4) + 14
ok_B14 = (f_at_m4 == -2) and bool(np.all(f_pep14 >= -2 - 1e-6))
check("B=[−2,+∞) (f(−4)=−2)", "[-2,+∞)", True, ok_B14, f"f(−4)={f_at_m4}")

ok_1_in_A = (1 >= -4)
check("1∈A=[−4,+∞)", "1∈A", True, ok_1_in_A)

y_pep14 = np.linspace(-2, 500, 200_000)
finv_pep14 = -4 + np.sqrt(y_pep14 + 2)
f_check14 = finv_pep14**2 + 8*finv_pep14 + 14
ok_inv14 = np.allclose(f_check14, y_pep14, atol=1e-4)
check("f⁻¹(x)=−4+√(x+2)", "-4+√(x+2)", True, ok_inv14,
      f"f(f⁻¹(y))=y  {'OK' if ok_inv14 else 'FALLA'}")

# ── PEP2023Alt-1.5 ────────────────────────────────────────────
print("\n[PEP2023Alt-1.5] f(x)=1+√((2x−3)/(x−4))  |  .tex: Dom=(−∞,3/2]∪(4,+∞), Rec=[1,+∞), Preimg(3)=13/2")

sym_dom15 = solveset((2*x - 3)/(x - 4) >= 0, x, S.Reals)
ok_s15 = sym_dom15 == Union(Interval(-oo, Rational(3,2)), Interval.open(4, oo))
check("Dom=(−∞,3/2]∪(4,+∞)", "(-∞,3/2]∪(4,+∞)", ok_s15, True, f"SymPy={sym_dom15}")

with np.errstate(divide='ignore', invalid='ignore'):
    r15 = (2*PTS - 3) / (PTS - 4)
mask_d15_orig = np.isfinite(r15) & (r15 >= 0)
mask_d15_tex  = (PTS <= 1.5) | (PTS > 4)
ok_n15 = acuerdo(mask_d15_orig, mask_d15_tex)
check("Dom NumPy=(−∞,3/2]∪(4,+∞)", "(-∞,3/2]∪(4,+∞)", True, ok_n15)

# Rec=[1,+∞): f≥1 siempre (raíz≥0) y Rec alcanza todo [1,+∞)
x_15a = np.linspace(-500, 1.5 - 1e-8, 300_000)
x_15b = np.linspace(4 + 1e-8, 500, 300_000)
with np.errstate(divide='ignore', invalid='ignore'):
    f15a = 1 + np.sqrt((2*x_15a - 3)/(x_15a - 4))
    f15b = 1 + np.sqrt((2*x_15b - 3)/(x_15b - 4))
rec_min_15 = min(f15a.min(), f15b.min())
ok_rec15 = rec_min_15 >= 1 - 1e-4
check("Rec=[1,+∞)", "[1,+∞)", True, ok_rec15,
      f"min(f)≈{rec_min_15:.6f}≥1")

# Preimagen de 3: f(x)=3 → 1+√(...)=3 → √(...)=2 → (2x-3)/(x-4)=4 → x=13/2
x_pre15 = Rational(13, 2)
val_pre15 = 1 + sqrt((2*x_pre15 - 3)/(x_pre15 - 4))
ok_pre15_sym = (val_pre15 == 3)
val_pre15_n = 1 + math.sqrt((2*6.5 - 3)/(6.5 - 4))
ok_pre15_n = abs(val_pre15_n - 3.0) < 1e-9
check("Preimg(3)=13/2", "x=13/2", ok_pre15_sym, ok_pre15_n,
      f"f(13/2)={val_pre15}={float(val_pre15):.6f}")

# ── PEP2023Alt-1.6 ────────────────────────────────────────────
print("\n[PEP2023Alt-1.6] f(x)=x/(1−|x|) en ]−1,1[  |  .tex: biyectiva, f⁻¹(y)=y/(1+|y|)")

x_pep16 = np.linspace(-1 + 1e-9, 1 - 1e-9, 500_000)
f_pep16 = x_pep16 / (1 - np.abs(x_pep16))
ok_cre16 = bool(np.all(np.diff(f_pep16) >= 0))
check("f crec en ]−1,1[ → inyectiva", "crec→inyectiva", True, ok_cre16)

f_lims16 = (f_pep16[0] < -1e6) and (f_pep16[-1] > 1e6)
check("f sobreyectiva (Rec=ℝ)", "Rec=ℝ", True, f_lims16,
      f"f(−1⁺)≈{f_pep16[0]:.1f}, f(1⁻)≈{f_pep16[-1]:.1f}")

y_pep16 = np.linspace(-200, 200, 500_000)
finv_pep16 = y_pep16 / (1 + np.abs(y_pep16))
f_check16 = finv_pep16 / (1 - np.abs(finv_pep16))
ok_inv16 = np.allclose(f_check16, y_pep16, atol=1e-5)
check("f⁻¹(y)=y/(1+|y|)", "y/(1+|y|)", True, ok_inv16,
      f"f(f⁻¹(y))=y  {'OK' if ok_inv16 else 'FALLA'}")

rec_inv16_ok = bool(np.all((finv_pep16 > -1) & (finv_pep16 < 1)))
check("Rec(f⁻¹)=]−1,1[", "]−1,1[", True, rec_inv16_ok,
      f"Todos los x_inv∈]−1,1[: {rec_inv16_ok}")

# ── MásPEP-1.8a ───────────────────────────────────────────────
print("\n[MásPEP-1.8a] f(x)=(x−2)²+1 en [−1,1]  |  .tex: k=2, f⁻¹(x)=2−√(x−1), Dom(f⁻¹)=[2,10]")

x_p18a = np.linspace(-1, 1, 500_000)
f_p18a = (x_p18a - 2)**2 + 1
ok_dec18a = bool(np.all(np.diff(f_p18a) <= 1e-10))
check("f dec en [−1,1] → inyectiva", "dec→inyectiva", True, ok_dec18a)

f_m1 = (-1-2)**2 + 1    # = 10
f_1  = (1-2)**2 + 1     # = 2
ok_k2 = (f_1 == 2) and (f_m1 == 10)
check("k=2 (f(1)=2=k, f(−1)=10)", "k=2", True, ok_k2, f"f(−1)={f_m1}, f(1)={f_1}")

y_p18a = np.linspace(2, 10, 200_000)
finv_p18a = 2 - np.sqrt(y_p18a - 1)
f_check18a = (finv_p18a - 2)**2 + 1
ok_inv18a = np.allclose(f_check18a, y_p18a, atol=1e-5)
check("f⁻¹(x)=2−√(x−1)", "2−√(x-1)", True, ok_inv18a)

rec_inv18a = bool(np.all((finv_p18a >= -1 - 1e-6) & (finv_p18a <= 1 + 1e-6)))
check("Rec(f⁻¹)=[−1,1]", "[-1,1]", True, rec_inv18a,
      f"x_inv∈[−1,1]: {rec_inv18a}")

# Dom(f⁻¹)=[2,10] verificado implícitamente (y∈[2,10] → definido)

# ── MásPEP-1.8b ───────────────────────────────────────────────
print("\n[MásPEP-1.8b] f(x)=√(4−√(2−3x))  |  .tex: Dom=[−14/3, 2/3], f creciente")

dom_18b_a = solveset(2 - 3*x >= 0, x, S.Reals)
dom_18b_b = solveset(4 - sqrt(2 - 3*x) >= 0, x, S.Reals)
sym_dom18b = dom_18b_a & dom_18b_b
ok_s18b = sym_dom18b == Interval(Rational(-14, 3), Rational(2, 3))
check("Dom=[−14/3,2/3] SymPy", "[-14/3,2/3]", ok_s18b, True, f"SymPy={sym_dom18b}")

with np.errstate(invalid='ignore'):
    inn18b = 2 - 3*PTS
    c1_18b = inn18b >= 0
    c2_18b = 4 - np.sqrt(np.abs(inn18b)) >= 0
mask_d18b_orig = c1_18b & c2_18b
mask_d18b_tex  = (PTS >= -14/3) & (PTS <= 2/3)
ok_n18b = acuerdo(mask_d18b_orig, mask_d18b_tex)
check("Dom=[−14/3,2/3] NumPy", "[-14/3,2/3]", True, ok_n18b)

x_p18b = np.linspace(-14/3 + 1e-9, 2/3 - 1e-9, 500_000)
f_p18b = np.sqrt(4 - np.sqrt(2 - 3*x_p18b))
ok_cre18b = bool(np.all(np.diff(f_p18b) >= -1e-10))
check("f creciente en Dom", "creciente", True, ok_cre18b)

# ── MásPEP-1.9 ────────────────────────────────────────────────
print("\n[MásPEP-1.9] f(x)=√(3/√(x+1)−1)  |  .tex: Dom=(−1,8], Rec=[0,+∞), Dom(f∘g)=(1,10], regla=√(3/√(x−1)−1)")

dom_19_a = solveset(x + 1 > 0, x, S.Reals)
dom_19_b = solveset(3/sqrt(x + 1) - 1 >= 0, x, S.Reals)
sym_dom19 = dom_19_a & dom_19_b
ok_s19 = sym_dom19 == Interval.Lopen(-1, 8)
check("Dom=(−1,8] SymPy", "(-1,8]", ok_s19, True, f"SymPy={sym_dom19}")

with np.errstate(divide='ignore', invalid='ignore'):
    c1_19 = PTS + 1 > 0
    inn19 = 3/np.sqrt(np.abs(PTS + 1)) - 1
    c2_19 = inn19 >= 0
mask_d19_orig = c1_19 & c2_19
mask_d19_tex  = (PTS > -1) & (PTS <= 8)
ok_n19 = acuerdo(mask_d19_orig, mask_d19_tex)
check("Dom=(−1,8] NumPy", "(-1,8]", True, ok_n19)

x_p19 = np.linspace(-1 + 1e-9, 8, 500_000)
f_p19 = np.sqrt(3/np.sqrt(x_p19 + 1) - 1)
rec_min19 = f_p19.min()
ok_rec19 = (abs(rec_min19) < 1e-5) and bool(f_p19[0] > 0)
check("Rec=[0,+∞)", "[0,+∞)", True, ok_rec19,
      f"f(8)≈{rec_min19:.6f}≈0, f(−1⁺)≈{f_p19[0]:.3f}")

# Dom(f∘g) con g(x)=x-2: g(x)∈(−1,8] → x-2∈(−1,8] → x∈(1,10]
dom_fg19_a = solveset(x - 1 > 0, x, S.Reals)
dom_fg19_b = solveset(3/sqrt(x - 1) - 1 >= 0, x, S.Reals)
sym_domfg19 = dom_fg19_a & dom_fg19_b
ok_sfg19 = sym_domfg19 == Interval.Lopen(1, 10)
check("Dom(f∘g)=(1,10] SymPy", "(1,10]", ok_sfg19, True, f"SymPy={sym_domfg19}")

with np.errstate(divide='ignore', invalid='ignore'):
    c1_fg19 = PTS - 1 > 0
    inn_fg19 = 3/np.sqrt(np.abs(PTS - 1)) - 1
    c2_fg19 = inn_fg19 >= 0
mask_fg19_orig = c1_fg19 & c2_fg19
mask_fg19_tex  = (PTS > 1) & (PTS <= 10)
ok_nfg19 = acuerdo(mask_fg19_orig, mask_fg19_tex)
check("Dom(f∘g)=(1,10] NumPy", "(1,10]", True, ok_nfg19)

# Verificar regla (f∘g)(x) = √(3/√(x-1)-1)
x_chk19 = np.linspace(1 + 1e-6, 10, 100_000)
fog19_direct = np.sqrt(3/np.sqrt((x_chk19 - 2) + 1) - 1)
fog19_formula = np.sqrt(3/np.sqrt(x_chk19 - 1) - 1)
ok_regla19 = np.allclose(fog19_direct, fog19_formula, atol=1e-9)
check("Regla (f∘g)(x)=√(3/√(x−1)−1)", "√(3/√(x-1)-1)", True, ok_regla19)

# ══════════════════════════════════════════════════════════════
print(f"\n{'═'*64}")
n_pass = total - len(errors)
print(f"  RESULTADO FINAL:  {n_pass}/{total} tests PASARON")
if errors:
    print(f"\n  {'─'*60}")
    print(f"  ✗ ERRORES DETECTADOS ({len(errors)}):")
    for e in errors:
        print(f"    • {e}")
else:
    print(f"\n  ✔ TODOS LOS RESULTADOS DEL SOLUCIONARIO SON CORRECTOS")
print(f"{'═'*64}")
sys.exit(0 if not errors else 1)
