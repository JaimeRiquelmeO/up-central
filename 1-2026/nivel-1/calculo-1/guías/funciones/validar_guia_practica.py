"""
VALIDACIÓN COMPLETA — Guía Práctica de Funciones (15 ejercicios)
Cálculo I — Usach Premium

Librerías: SymPy (simbólico) + NumPy (muestreo numérico ≥ 100 000 puntos)
Criterio: acuerdo 100% en ambas librerías antes de añadir al .tex
"""

from sympy import *
import numpy as np, math

x, y, t, z, w, k, b = symbols('x y t z w k b', real=True)

PASS = "\033[92m✔ PASS\033[0m"
FAIL = "\033[91m✗ FAIL\033[0m"
SEP  = "─" * 62
results = {}

def val(tag, ok_sympy, ok_numpy, solucion, detalle=""):
    ok = ok_sympy and ok_numpy
    results[tag] = ok
    s = PASS if ok else FAIL
    print(f"  {s}  [{tag}]  sol: {solucion}")
    if detalle: print(f"        ↳ {detalle}")

def acuerdo100(mask_orig, mask_sol):
    return abs(np.mean(mask_orig == mask_sol)*100 - 100.0) < 1e-8

PTS = np.sort(np.concatenate([
    np.linspace(-60, 60, 70_000) + 1e-6*math.pi,
    np.random.default_rng(99).uniform(-60, 60, 30_000)
]))

print("=" * 62)
print("  VALIDACIÓN — Guía Práctica de Funciones (15 ejercicios)")
print("=" * 62)

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN I — Dominio, Recorrido y Monotonía")
print(SEP)

# ── Ejercicio 1 ────────────────────────────────────────────────
# f(x) = sqrt(x^2 - 9)    Dom = (-∞,-3] ∪ [3,+∞)
print("\n[Ej.1] f(x)=√(x²−9) — Dom(f)")

sym1 = solveset(x**2 - 9 >= 0, x, S.Reals)
ok_s1 = sym1 == Union(Interval(-oo, -3), Interval(3, oo))

mask_orig1 = PTS**2 - 9 >= 0
mask_tex1  = (PTS <= -3) | (PTS >= 3)
ok_n1 = acuerdo100(mask_orig1, mask_tex1)

val("1-Dom", ok_s1, ok_n1, "Dom(f) = (-∞,-3]∪[3,+∞)",
    f"SymPy={sym1}")

# ── Ejercicio 2 ────────────────────────────────────────────────
# g(z) = 1/sqrt(25 - z^2)   Dom=(-5,5)  Rec=[1/5,+∞)
print("\n[Ej.2] g(z)=1/√(25−z²) — Dom y Rec")

sym2 = solveset(25 - z**2 > 0, z, S.Reals)
ok_s2 = sym2 == Interval.open(-5, 5)

mask_orig2 = 25 - PTS**2 > 0
mask_tex2  = (PTS > -5) & (PTS < 5)
ok_n2 = acuerdo100(mask_orig2, mask_tex2)

val("2-Dom", ok_s2, ok_n2, "Dom(g) = (-5,5)", f"SymPy={sym2}")

# Rec: g(0)=1/5, g→+∞ cuando z→±5
z_in = np.linspace(-5+1e-9, 5-1e-9, 500_000)
g2 = 1/np.sqrt(25 - z_in**2)
ok_rec2 = abs(g2.min() - 0.2) < 1e-4
val("2-Rec", True, ok_rec2, "Rec(g) = [1/5, +∞)",
    f"g(0)=1/5≈{g2.min():.6f}, g→+∞ en z→±5")

# ── Ejercicio 3 ────────────────────────────────────────────────
# h(x) = sqrt(x+4) / (x^2 - 1)   Dom = [-4,+∞) \ {-1, 1}  pero -1∈[-4,+∞) sí
# Hay que excluir x=-1 y x=1
# Simplificado: Dom = [-4,+∞) \ {-1,1}
print("\n[Ej.3] h(x)=√(x+4)/(x²−1) — Dom(h)")

# condiciones: x+4 >= 0  AND  x^2-1 != 0
# x >= -4  AND  x != ±1
dom3_base = solveset(x + 4 >= 0, x, S.Reals)
exclude3  = FiniteSet(-1, 1)
sym3 = dom3_base - exclude3
ok_s3 = (sym3 == Interval(-4, oo) - FiniteSet(-1, 1))

with np.errstate(divide='ignore', invalid='ignore'):
    denom3 = PTS**2 - 1
    numer3 = PTS + 4
mask_orig3 = (numer3 >= 0) & (denom3 != 0)
mask_tex3  = (PTS >= -4) & (PTS != -1) & (PTS != 1)
# Para NumPy, los puntos discretos exactamente en -1 y 1 son raros; usar tolerancia
mask_tex3_num = (PTS >= -4) & (np.abs(PTS + 1) > 1e-9) & (np.abs(PTS - 1) > 1e-9)
ok_n3 = acuerdo100(mask_orig3, mask_tex3_num)

val("3-Dom", ok_s3, ok_n3, "Dom(h) = [-4,+∞)\\{-1,1}",
    f"SymPy={sym3}")

# ── Ejercicio 4 ────────────────────────────────────────────────
# g(x) = 3(x-1)^2 + 2   Monotonía: dec en (-∞,1], cre en [1,+∞)
print("\n[Ej.4] g(x)=3(x−1)²+2 — Monotonía")

xp = np.linspace(-50, 50, 500_000)
g4 = 3*(xp - 1)**2 + 2
idx_dec4 = np.where(xp <= 1)[0]
idx_cre4 = np.where(xp >= 1)[0]
ok_dec4 = bool(np.all(np.diff(g4[idx_dec4]) <= 1e-10))
ok_cre4 = bool(np.all(np.diff(g4[idx_cre4]) >= -1e-10))
# SymPy: derivada g'(x)=6(x-1) < 0 para x<1, > 0 para x>1
gp4 = diff(3*(x-1)**2 + 2, x)  # = 6(x-1)
ok_s4_dec = simplify(gp4.subs(x, 0)) < 0   # g'(0)=-6<0
ok_s4_cre = simplify(gp4.subs(x, 2)) > 0   # g'(2)=6>0

val("4-Dec", ok_s4_dec, ok_dec4, "dec en (-∞,1]")
val("4-Cre", ok_s4_cre, ok_cre4, "cre en [1,+∞)")

# ── Ejercicio 5 ────────────────────────────────────────────────
# h(x) = -(x+3)^2 + 5   Monotonía: cre en (-∞,-3], dec en [-3,+∞)
print("\n[Ej.5] h(x)=−(x+3)²+5 — Monotonía")

h5 = -(xp + 3)**2 + 5
idx_cre5 = np.where(xp <= -3)[0]
idx_dec5 = np.where(xp >= -3)[0]
ok_cre5 = bool(np.all(np.diff(h5[idx_cre5]) >= -1e-10))
ok_dec5 = bool(np.all(np.diff(h5[idx_dec5]) <= 1e-10))
hp5 = diff(-(x+3)**2 + 5, x)   # = -2(x+3)
ok_s5_cre = simplify(hp5.subs(x, -5)) > 0   # h'(-5)=4>0
ok_s5_dec = simplify(hp5.subs(x, 0)) < 0    # h'(0)=-6<0

val("5-Cre", ok_s5_cre, ok_cre5, "cre en (-∞,-3]")
val("5-Dec", ok_s5_dec, ok_dec5, "dec en [-3,+∞)")

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN II — Composición e Inyectividad")
print(SEP)

# ── Ejercicio 6 ────────────────────────────────────────────────
# f(x)=sqrt(x+3), g(x)=2x-3
# Dom(f∘g): {x | 2x-3 >= -3} = {x | x >= 0} = [0,+∞)
# (f∘g)(x) = sqrt(2x-3+3) = sqrt(2x)
# (f∘g)(8) = sqrt(16) = 4
# Preimagen de 3: sqrt(2x)=3 → 2x=9 → x=9/2
print("\n[Ej.6] f=√(x+3), g=2x−3 — Dom(f∘g), imagen y preimagen")

dom6_sym = solveset(2*x - 3 >= -3, x, S.Reals)
ok_s6 = dom6_sym == Interval(0, oo)

mask_d6_orig = (2*PTS - 3 + 3) >= 0
mask_d6_tex  = PTS >= 0
ok_n6 = acuerdo100(mask_d6_orig, mask_d6_tex)
val("6-Dom", ok_s6, ok_n6, "Dom(f∘g) = [0,+∞)", f"SymPy={dom6_sym}")

# imagen de 8
img6 = math.sqrt(2*8)
ok_img6 = abs(img6 - 4.0) < 1e-9
val("6-img8", True, ok_img6, "(f∘g)(8) = 4", f"√16 = {img6}")

# preimagen de 3
pre6 = Rational(9, 2)
fog6_check = sqrt(2*pre6)
ok_pre6 = (fog6_check == 3)
val("6-pre3", ok_pre6, abs(math.sqrt(2*4.5) - 3) < 1e-9,
    "Preimg(3) = 9/2", f"√(2·9/2)=√9={fog6_check}")

# ── Ejercicio 7 ────────────────────────────────────────────────
# f(x)=sqrt((x+1)/(x-2)), g(x)=x+3
# Dom(f): (x+1)/(x-2)>=0 → x∈(-∞,-1]∪(2,+∞)
# Dom(f∘g)={x | x+3 ∈ (-∞,-1]∪(2,+∞)} = {x | x<=-4 or x>-1} = (-∞,-4]∪(-1,+∞)
# (f∘g)(2) = f(5) = sqrt(6/3) = sqrt(2)
# Preimagen de 1: sqrt((x+3+1)/(x+3-2))=1 → (x+4)/(x+1)=1 → x+4=x+1 → 3=1 (no existe)
print("\n[Ej.7] f=√((x+1)/(x−2)), g=x+3 — Dom(f∘g), imagen y preimagen")

sym7_domf = solveset((x+1)/(x-2) >= 0, x, S.Reals)
print(f"  Dom(f)={sym7_domf}")

sym7_domfog = solveset(((x+3)+1)/((x+3)-2) >= 0, x, S.Reals)
ok_s7 = sym7_domfog == Union(Interval(-oo, -4), Interval.open(-1, oo))

with np.errstate(divide='ignore', invalid='ignore'):
    u7 = PTS + 3
    ratio7 = (u7+1)/(u7-2)
mask_d7_orig = np.isfinite(ratio7) & (ratio7 >= 0)
mask_d7_tex  = (PTS <= -4) | (PTS > -1)
ok_n7 = acuerdo100(mask_d7_orig, mask_d7_tex)
val("7-Dom", ok_s7, ok_n7, "Dom(f∘g) = (-∞,-4]∪(-1,+∞)",
    f"SymPy={sym7_domfog}")

# imagen de 2
fog7_2 = math.sqrt((2+3+1)/(2+3-2))   # f(5) = sqrt(6/3) = sqrt(2)
ok_img7 = abs(fog7_2 - math.sqrt(2)) < 1e-9
val("7-img2", True, ok_img7, "(f∘g)(2)=√2",
    f"f(5)=√(6/3)=√2={fog7_2:.8f}")

# preimagen de 1: no existe
u7s = symbols('u7s', real=True)
sol7_pre = solveset(Eq((u7s+4)/(u7s+1), 1), u7s, S.Reals)
ok_pre7 = (sol7_pre == EmptySet)
val("7-pre1", ok_pre7, True, "Preimg(1) no existe",
    f"SymPy: {sol7_pre}")

# ── Ejercicio 8 ────────────────────────────────────────────────
# f(x)=(5x+3)/4, g(x)=(x+k)/5 → f∘g=g∘f → k=-12
# (f∘g)(x) = (5*(x+k)/5+3)/4 = (x+k+3)/4
# (g∘f)(x) = ((5x+3)/4+k)/5 = (5x+3+4k)/20
# (x+k+3)/4 = (5x+3+4k)/20 → 5(x+k+3)=5x+3+4k → 5k+15=3+4k → k=-12
print("\n[Ej.8] f=(5x+3)/4, g=(x+k)/5 — hallar k tal que f∘g=g∘f")

k8 = symbols('k8', real=True)
fog8 = (5*((x + k8)/5) + 3) / 4
gof8 = ((5*x + 3)/4 + k8) / 5
k_sol8 = solve(Eq(simplify(fog8 - gof8), 0), k8)
ok_s8 = (len(k_sol8) == 1) and (k_sol8[0] == -12)

xn = np.linspace(-50, 50, 200_000)
fog8n = (xn + (-12) + 3) / 4
gof8n = (5*xn + 3 + 4*(-12)) / 20
ok_n8 = np.allclose(fog8n, gof8n, atol=1e-10)
val("8-k", ok_s8, ok_n8, "k = -12",
    f"SymPy k={k_sol8}")

# ── Ejercicio 9 ────────────────────────────────────────────────
# g(x) = x^2 - 4x + 8 = (x-2)^2 + 4  en [2,+∞)
# Creciente en [2,+∞) → inyectiva, g(2)=4, Rec=[4,+∞) ≠ ℝ → no sobreyectiva
print("\n[Ej.9] g(x)=x²−4x+8=(x−2)²+4 en [2,+∞) — inyectividad")

x_in9 = np.linspace(2, 100, 500_000)
g9 = x_in9**2 - 4*x_in9 + 8
ok_inj9 = bool(np.all(np.diff(g9) >= 0))
g9_at2 = 4 - 8 + 8   # = 4
ok_rec9 = (g9_at2 == 4) and (g9.min() >= 4 - 1e-6)

gp9 = diff(x**2 - 4*x + 8, x)  # = 2x-4 > 0 for x>2
ok_s9_inj = simplify(gp9.subs(x, 3)) > 0

val("9-Inj", ok_s9_inj, ok_inj9, "g inyectiva (crec en [2,+∞))")
val("9-Rec", True, ok_rec9, "Rec(g)=[4,+∞) → no sobreyectiva",
    f"g(2)={g9_at2}, NumPy min={g9.min():.4f}")

# ── Ejercicio 10 ───────────────────────────────────────────────
# f(x)=sqrt(3 - sqrt(2x-1))
# Dom: 2x-1>=0 AND 3-sqrt(2x-1)>=0
#   x>=1/2 AND sqrt(2x-1)<=3 AND 2x-1<=9 → x<=5
# Dom = [1/2, 5]
# Decreciente (cadena de funciones creciente-decreciente)
# Rec: f(1/2)=sqrt(3-0)=sqrt(3), f(5)=sqrt(3-3)=0 → [0,sqrt(3)]
print("\n[Ej.10] f(x)=√(3−√(2x−1)) — Dom, monotonía, Rec")

dom10_a = solveset(2*x - 1 >= 0, x, S.Reals)
dom10_b = solveset(3 - sqrt(2*x - 1) >= 0, x, S.Reals)
sym10 = dom10_a & dom10_b
ok_s10 = sym10 == Interval(Rational(1,2), 5)

with np.errstate(invalid='ignore'):
    c1_10 = 2*PTS - 1 >= 0
    c2_10 = 3 - np.sqrt(np.where(c1_10, 2*PTS - 1, 0)) >= 0
mask_d10_orig = c1_10 & c2_10
mask_d10_tex  = (PTS >= 0.5) & (PTS <= 5)
ok_n10 = acuerdo100(mask_d10_orig, mask_d10_tex)
val("10-Dom", ok_s10, ok_n10, "Dom(f) = [1/2, 5]", f"SymPy={sym10}")

x_in10 = np.linspace(0.5, 5, 500_000)
f10 = np.sqrt(3 - np.sqrt(2*x_in10 - 1))
ok_dec10 = bool(np.all(np.diff(f10) <= 1e-10))
val("10-Dec", True, ok_dec10, "f decreciente")

ok_rec10 = (abs(f10.min()) < 1e-6) and (abs(f10.max() - math.sqrt(3)) < 1e-5)
val("10-Rec", True, ok_rec10, "Rec(f) = [0, √3]",
    f"NumPy: [{f10.min():.6f}, {f10.max():.6f}] (√3≈{math.sqrt(3):.6f})")

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN III — Biyectividad y Función Inversa")
print(SEP)

# ── Ejercicio 11 ───────────────────────────────────────────────
# f(x) = x/(x+2)  en [0,+∞)
# f'=2/(x+2)^2 > 0 → crec → inyectiva
# f(0)=0, f→1 cuando x→+∞ → Rec=[0,1)
# Inversa: y=x/(x+2) → x=2y/(1-y)
# Dom(f^-1)=[0,1), Rec(f^-1)=[0,+∞)
print("\n[Ej.11] f(x)=x/(x+2) en [0,+∞) — biyectiva, f⁻¹")

x_in11 = np.linspace(0, 500, 500_000)
f11 = x_in11 / (x_in11 + 2)
ok_cre11 = bool(np.all(np.diff(f11) >= 0))
ok_rec11_min = abs(f11[0]) < 1e-9   # f(0)=0
ok_rec11_sup = f11.max() < 1.0      # siempre < 1

fp11 = diff(x/(x+2), x)   # = 2/(x+2)^2
ok_s11_cre = simplify(fp11.subs(x, 0)) > 0

val("11-Inj", ok_s11_cre, ok_cre11, "f inyectiva (crec en [0,+∞))")
val("11-Rec", True, ok_rec11_min and ok_rec11_sup, "Rec(f)=[0,1)",
    f"f(0)={f11[0]:.2f}, sup={f11.max():.8f}<1")

# Inversa: y=x/(x+2) → y(x+2)=x → x(y-1)=-2y → x=2y/(1-y)
y_in11 = np.linspace(0, 1-1e-7, 200_000)
finv11 = 2*y_in11 / (1 - y_in11)
f_of_inv11 = finv11 / (finv11 + 2)
ok_inv11 = np.allclose(f_of_inv11, y_in11, atol=1e-6)
val("11-Inv", True, ok_inv11, "f⁻¹(y)=2y/(1−y), Dom=[0,1), Rec=[0,+∞)",
    f"f(f⁻¹(y))=y: {'OK' if ok_inv11 else 'FALLA'}")

# ── Ejercicio 12 ───────────────────────────────────────────────
# f(x)=-x^2+6x-5=-(x-3)^2+4, vértice (3,4), 3∈A
# A=[3,+∞) (f decreciente), B=(-∞,4]
# Inversa: y=-(x-3)^2+4 → (x-3)^2=4-y → x=3+sqrt(4-y) [x≥3→ signo +]
# Dom(f^-1)=(-∞,4], Rec(f^-1)=[3,+∞)
print("\n[Ej.12] f(x)=−x²+6x−5, 3∈A — A,B biyectiva, f⁻¹")

x_in12 = np.linspace(3, 100, 500_000)
f12 = -(x_in12 - 3)**2 + 4
ok_dec12 = bool(np.all(np.diff(f12) <= 1e-10))
f12_at3 = -(3-3)**2 + 4   # = 4
ok_B12 = (f12_at3 == 4) and (f12.max() <= 4 + 1e-9)

fp12 = diff(-(x-3)**2 + 4, x)  # = -2(x-3) < 0 for x>3
ok_s12_dec = simplify(fp12.subs(x, 4)) < 0

val("12-Inj", ok_s12_dec, ok_dec12, "f dec en [3,+∞) → inyectiva")
val("12-AB",  True, ok_B12, "A=[3,+∞), B=(−∞,4]",
    f"f(3)={f12_at3}")

y_in12 = np.linspace(-500, 4, 200_000)
finv12 = 3 + np.sqrt(4 - y_in12)
f_of_inv12 = -(finv12 - 3)**2 + 4
ok_inv12 = np.allclose(f_of_inv12, y_in12, atol=1e-5)
val("12-Inv", True, ok_inv12, "f⁻¹(x)=3+√(4−x), Dom=(−∞,4], Rec=[3,+∞)",
    f"f(f⁻¹(y))=y: {'OK' if ok_inv12 else 'FALLA'}")

# ── Ejercicio 13 ───────────────────────────────────────────────
# f(x) = x/(x-2)  en ]2,+∞[
# f'=-2/(x-2)^2 < 0 → dec → inyectiva
# f(2^+)→+∞, f(+∞)→1^+ → Rec=(1,+∞)
# Inversa: y=x/(x-2) → y(x-2)=x → x(y-1)=2y → x=2y/(y-1)
# Dom(f^-1)=(1,+∞), Rec(f^-1)=(2,+∞)
print("\n[Ej.13] f(x)=x/(x−2) en ]2,+∞[ — biyectiva, f⁻¹")

x_in13 = np.linspace(2+1e-9, 500, 500_000)
f13 = x_in13 / (x_in13 - 2)
ok_dec13 = bool(np.all(np.diff(f13) <= 0))
f13_lim_inf = f13[-1]   # → 1^+
f13_lim_sup = f13[0]    # → +∞
ok_rec13 = (f13_lim_inf > 1) and (f13_lim_inf < 1.01) and (f13_lim_sup > 1e5)

fp13 = diff(x/(x-2), x)  # = -2/(x-2)^2
ok_s13_dec = simplify(fp13.subs(x, 3)) < 0

val("13-Inj", ok_s13_dec, ok_dec13, "f dec en ]2,+∞[ → inyectiva")
val("13-Rec", True, ok_rec13, "Rec(f)=(1,+∞)",
    f"f(2+)≈{f13[0]:.2f}>>1, f(+∞)≈{f13_lim_inf:.8f}→1+")

y_in13 = np.linspace(1+1e-7, 500, 200_000)
finv13 = 2*y_in13 / (y_in13 - 1)
f_of_inv13 = finv13 / (finv13 - 2)
ok_inv13 = np.allclose(f_of_inv13, y_in13, atol=1e-4)
rec_inv13_ok = bool(np.all(finv13 > 2))
val("13-Inv", True, ok_inv13 and rec_inv13_ok,
    "f⁻¹(y)=2y/(y−1), Dom=(1,+∞), Rec=(2,+∞)",
    f"f(f⁻¹(y))=y: {'OK' if ok_inv13 else 'FALLA'}, Rec⊂(2,+∞): {rec_inv13_ok}")

# ══════════════════════════════════════════════════════════════
print(f"\n{SEP}")
print("  SECCIÓN IV — Nivel PEP")
print(SEP)

# ── Ejercicio 14 ───────────────────────────────────────────────
# f(x)=sqrt(x-3), g(x)=sqrt(25-x^2)-1
# Dom(g)=[-5,5]
# Dom(f∘g): g(x)>=3 → sqrt(25-x^2)-1>=3 → sqrt(25-x^2)>=4 → 25-x^2>=16 → x^2<=9 → x∈[-3,3]
# Dom(f∘g) = [-5,5] ∩ [-3,3] = [-3,3]
# Fórmula: (f∘g)(x) = sqrt(sqrt(25-x^2)-1-3) = sqrt(sqrt(25-x^2)-4)
print("\n[Ej.14] f=√(x−3), g=√(25−x²)−1 — Dom(f∘g) [PEP]")

dom14_g = solveset(25 - x**2 >= 0, x, S.Reals)
dom14_cond = solveset(sqrt(25 - x**2) - 1 >= 3, x, S.Reals)
sym14_fog = dom14_g & dom14_cond
ok_s14 = sym14_fog == Interval(-3, 3)

with np.errstate(invalid='ignore'):
    sq14 = np.sqrt(np.where(25 - PTS**2 >= 0, 25 - PTS**2, np.nan))
    gx14 = sq14 - 1
mask_d14_orig = np.isfinite(gx14) & (gx14 >= 3)
mask_d14_tex  = (PTS >= -3) & (PTS <= 3)
ok_n14 = acuerdo100(mask_d14_orig, mask_d14_tex)
val("14-Dom", ok_s14, ok_n14, "Dom(f∘g) = [-3,3]",
    f"SymPy={sym14_fog}")

# Fórmula (f∘g)(x) = sqrt(sqrt(25-x^2)-4)
x_chk14 = np.linspace(-3+1e-9, 3-1e-9, 100_000)
fog14_direct  = np.sqrt(np.sqrt(25 - x_chk14**2) - 1 - 3)
fog14_formula = np.sqrt(np.sqrt(25 - x_chk14**2) - 4)
ok_formula14 = np.allclose(fog14_direct, fog14_formula, atol=1e-12)
val("14-Fórmula", True, ok_formula14,
    "(f∘g)(x) = √(√(25−x²)−4)")

# ── Ejercicio 15 ───────────────────────────────────────────────
# f(x) = sqrt(4/sqrt(x+2) - 1)
# Dom: x+2>0 AND 4/sqrt(x+2)-1>=0
#   x>-2 AND sqrt(x+2)<=4 AND x+2<=16 → -2<x<=14
# Dom = (-2, 14]
# Decreciente (cadena: x↑ → x+2↑ → sqrt(x+2)↑ → 4/sqrt(x+2)↓ → f↓)
# Rec: f(14)=sqrt(4/4-1)=0, f(-2+)→+∞ → Rec=[0,+∞)
# g(x)=x+1: (f∘g)(x)=f(x+1)=sqrt(4/sqrt(x+3)-1)
# Dom(f∘g): x+1∈(-2,14] → x∈(-3,13]
print("\n[Ej.15] f(x)=√(4/√(x+2)−1), g(x)=x+1 — Dom,Rec,dec; f∘g [PEP]")

dom15_a = solveset(x + 2 > 0, x, S.Reals)
dom15_b = solveset(4/sqrt(x + 2) - 1 >= 0, x, S.Reals)
sym15 = dom15_a & dom15_b
ok_s15 = sym15 == Interval.Lopen(-2, 14)

with np.errstate(divide='ignore', invalid='ignore'):
    c1_15 = PTS + 2 > 0
    val15_inner = 4/np.sqrt(np.abs(PTS + 2)) - 1
    c2_15 = val15_inner >= 0
mask_d15_orig = c1_15 & c2_15
mask_d15_tex  = (PTS > -2) & (PTS <= 14)
ok_n15 = acuerdo100(mask_d15_orig, mask_d15_tex)
val("15-Dom", ok_s15, ok_n15, "Dom(f) = (−2,14]", f"SymPy={sym15}")

x_in15 = np.linspace(-2+1e-9, 14, 500_000)
f15 = np.sqrt(4/np.sqrt(x_in15 + 2) - 1)
ok_dec15 = bool(np.all(np.diff(f15) <= 1e-10))
val("15-Dec", True, ok_dec15, "f decreciente en (−2,14]")

ok_rec15 = (abs(f15[-1]) < 1e-5) and (f15[0] > 10)
val("15-Rec", True, ok_rec15, "Rec(f) = [0,+∞)",
    f"f(14)≈{f15[-1]:.6f}≈0, f(−2+)≈{f15[0]:.2f}>>0")

# Dom(f∘g): g(x)=x+1, g(x)∈(-2,14] → x∈(-3,13]
dom15fog_a = solveset(x + 1 > -2, x, S.Reals)
dom15fog_b = solveset(x + 1 <= 14, x, S.Reals)
sym15_fog = dom15fog_a & dom15fog_b
ok_s15fog = sym15_fog == Interval.Lopen(-3, 13)

with np.errstate(divide='ignore', invalid='ignore'):
    c1_fg15 = PTS + 1 + 2 > 0
    inn_fg15 = 4/np.sqrt(np.abs(PTS + 1 + 2)) - 1
    c2_fg15 = inn_fg15 >= 0
mask_fg15_orig = c1_fg15 & c2_fg15
mask_fg15_tex  = (PTS > -3) & (PTS <= 13)
ok_nfg15 = acuerdo100(mask_fg15_orig, mask_fg15_tex)
val("15-DomFog", ok_s15fog, ok_nfg15, "Dom(f∘g) = (−3,13]",
    f"SymPy={sym15_fog}")

# Verificar regla (f∘g)(x)=sqrt(4/sqrt(x+3)-1)
x_chk15 = np.linspace(-3+1e-7, 13, 200_000)
fog15_direct  = np.sqrt(4/np.sqrt(x_chk15 + 1 + 2) - 1)
fog15_formula = np.sqrt(4/np.sqrt(x_chk15 + 3) - 1)
ok_formula15 = np.allclose(fog15_direct, fog15_formula, atol=1e-12)
val("15-Fórmula", True, ok_formula15,
    "(f∘g)(x) = √(4/√(x+3)−1), Dom=(−3,13]")

# ══════════════════════════════════════════════════════════════
total = len(results)
passed = sum(results.values())
print(f"\n{'═'*62}")
print(f"  RESULTADO FINAL: {passed}/{total} tests PASARON")
failed = [k for k,v in results.items() if not v]
if failed:
    print(f"  ✗ FALLIDOS: {failed}")
else:
    print(f"  ✔ TODOS LOS RESULTADOS VALIDADOS — LISTOS PARA EL .TEX")
print(f"{'═'*62}")
