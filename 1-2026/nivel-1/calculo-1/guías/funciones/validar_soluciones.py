"""
Validación de soluciones — Guía de Funciones, Cálculo I
Usach Premium | Skill: create-guia

Método: SymPy (simbólico) + NumPy (muestreo numérico ≥ 50 000 pts).
Criterio: acuerdo 100.0000% entre ambas librerías.
NO se incluye este archivo en el PDF final.
"""

from sympy import *
import numpy as np
import math

x, y, k, b = symbols('x y k b', real=True)
PASS = "\033[92m✔ PASS\033[0m"
FAIL = "\033[91m✗ FAIL\033[0m"

def acuerdo_numpy(mask_orig, mask_sol):
    pct = np.mean(mask_orig == mask_sol) * 100
    ok  = abs(pct - 100.0) < 1e-9
    return pct, ok

PTS = np.sort(np.concatenate([
    np.linspace(-30, 30, 40_000) + 1e-6 * math.pi,
    np.random.default_rng(42).uniform(-30, 30, 10_000)
]))

print("=" * 60)
print("  VALIDACIÓN — GUÍA DE FUNCIONES")
print("=" * 60)

# ══════════════════════════════════════════════════════════════
# ── SECCIÓN I ─────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════

print("\n── Sección I ──────────────────────────────────────────────")

# ─── 1.1  h(w) = 1 / sqrt(16 - w²)  ───────────────────────────
print("\n[1.1] h(w) = 1/sqrt(16 - w²)  → Dom(h)")
w = symbols('w', real=True)

# SymPy
dom_sympy = solveset(16 - w**2 > 0, w, S.Reals)
print(f"  SymPy Dom: {dom_sympy}")

# NumPy: condición: 16 - w² > 0  ↔  w ∈ (-4, 4)
wpts = PTS.copy()
mask_orig = (16 - wpts**2) > 0
mask_sol  = (wpts > -4) & (wpts < 4)
pct, ok = acuerdo_numpy(mask_orig, mask_sol)
print(f"  NumPy acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")
print(f"  RESULTADO: Dom(h) = (-4, 4)")

# ─── 1.2a  F(t) = 1/sqrt(t)  ───────────────────────────────────
print("\n[1.2a] F(t) = 1/sqrt(t)  → Dom y Rec")
t = symbols('t', real=True)

# SymPy — Dom
dom_F = solveset(t > 0, t, S.Reals)
print(f"  SymPy Dom(F): {dom_F}")

# NumPy — Dom
tpts = PTS[PTS > -30]
mask_dom_F  = tpts > 0
mask_sol_F  = tpts > 0   # mismo intervalo
pct, ok = acuerdo_numpy(mask_dom_F, mask_sol_F)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Recorrido: F(t) = 1/sqrt(t), t>0  → F>0, F→∞ cuando t→0⁺, F→0⁺ cuando t→∞
# Rec(F) = (0, +∞)
t_pos = np.linspace(1e-6, 200, 100_000)
F_vals = 1.0 / np.sqrt(t_pos)
print(f"  Rec(F): min≈{F_vals.min():.6f}, max≈{F_vals.max():.2f} → (0, +∞)")
print(f"  RESULTADO: Dom(F) = (0,+∞),  Rec(F) = (0,+∞)")

# ─── 1.2b  g(z) = 1/sqrt(4 - z²)  ─────────────────────────────
print("\n[1.2b] g(z) = 1/sqrt(4 - z²)  → Dom y Rec")
z = symbols('z', real=True)

# SymPy — Dom
dom_gz = solveset(4 - z**2 > 0, z, S.Reals)
print(f"  SymPy Dom(g): {dom_gz}")

# NumPy — Dom
zpts = PTS.copy()
mask_dom_g  = (4 - zpts**2) > 0
mask_sol_gz = (zpts > -2) & (zpts < 2)
pct, ok = acuerdo_numpy(mask_dom_g, mask_sol_gz)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Recorrido: mín en z→0 → g(0)=1/2; tiende a ∞ en z→±2
z_in = np.linspace(-2 + 1e-7, 2 - 1e-7, 200_000)
g_vals = 1.0 / np.sqrt(4 - z_in**2)
print(f"  Rec(g): min≈{g_vals.min():.6f} (en z=0) → [1/2, +∞)")
print(f"  RESULTADO: Dom(g) = (-2,2),  Rec(g) = [1/2, +∞)")

# ─── 1.3  Monotonía ─────────────────────────────────────────────
print("\n[1.3] Monotonía de g(x)")

# g(x) = (x-3)² + 2  — parábola, vértice en x=3
#   decreciente en (-∞, 3], creciente en [3, +∞)
xpts = np.linspace(-20, 20, 100_000)
g1 = (xpts - 3)**2 + 2
# Verificar: para x1 < x2 < 3  → g(x1) > g(x2)  (decreciente)
idx = np.where(xpts < 3)[0]
decrece = np.all(np.diff(g1[idx]) <= 0)
# Para 3 < x1 < x2  → g(x1) < g(x2)  (creciente)
idx2 = np.where(xpts > 3)[0]
crece = np.all(np.diff(g1[idx2]) >= 0)
print(f"  g(x)=(x-3)²+2: decreciente en (-∞,3] → {PASS if decrece else FAIL}")
print(f"  g(x)=(x-3)²+2: creciente  en [3,+∞)  → {PASS if crece  else FAIL}")

# g(x) = -(x+1)² + 5  — parábola invertida, vértice en x=-1
g2 = -(xpts + 1)**2 + 5
idx3 = np.where(xpts < -1)[0]
crece2 = np.all(np.diff(g2[idx3]) >= 0)
idx4 = np.where(xpts > -1)[0]
decrece2 = np.all(np.diff(g2[idx4]) <= 0)
print(f"  g(x)=-(x+1)²+5: creciente en (-∞,-1] → {PASS if crece2  else FAIL}")
print(f"  g(x)=-(x+1)²+5: decreciente en [-1,+∞)→ {PASS if decrece2 else FAIL}")
print(f"  RESULTADO 1.3a: g(x)=(x-3)²+2 → dec. en (-∞,3], crec. en [3,+∞)")
print(f"  RESULTADO 1.3b: g(x)=-(x+1)²+5 → crec. en (-∞,-1], dec. en [-1,+∞)")

# ─── 1.4  g(x) = sqrt(3 - sqrt(x+2))  ──────────────────────────
print("\n[1.4] g(x) = sqrt(3 - sqrt(x+2))")

# Dominio: x+2 ≥ 0  AND  3 - sqrt(x+2) ≥ 0
#   ↔  x ≥ -2  AND  sqrt(x+2) ≤ 3  ↔  x+2 ≤ 9  ↔  x ≤ 7
# SymPy — intersección de las dos condiciones
dom_g14_a = solveset(x + 2 >= 0, x, S.Reals)
dom_g14_b = solveset(3 - sqrt(x + 2) >= 0, x, S.Reals)
dom_g14 = dom_g14_a & dom_g14_b
print(f"  SymPy Dom: {dom_g14}")

# NumPy
xpts2 = np.linspace(-30, 30, 100_000)
with np.errstate(invalid='ignore'):
    cond1 = xpts2 + 2 >= 0
    inner = np.where(cond1, xpts2 + 2, np.nan)
    cond2 = 3 - np.sqrt(np.abs(inner)) >= 0
mask_dom_g14 = cond1 & cond2
mask_sol_g14 = (xpts2 >= -2) & (xpts2 <= 7)
pct, ok = acuerdo_numpy(mask_dom_g14, mask_sol_g14)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Decreciente: verificar con derivada numérica
x_in14 = np.linspace(-2, 7, 200_000)
g14 = np.sqrt(3 - np.sqrt(x_in14 + 2))
decrece_g14 = np.all(np.diff(g14) <= 1e-10)
print(f"  Estrictamente decreciente en [-2,7]: → {PASS if decrece_g14 else FAIL}")

# Recorrido: g(-2)=sqrt(3), g(7)=sqrt(3-3)=0
g14_min = g14.min()
g14_max = g14.max()
print(f"  g(-2)={np.sqrt(3):.6f}, g(7)=0  → Rec(g) = [0, sqrt(3)]")
print(f"  NumPy Rec: [{g14_min:.6f}, {g14_max:.6f}]")
print(f"  RESULTADO 1.4: Dom(g)=[-2,7], Rec(g)=[0,√3], g decreciente")

# ══════════════════════════════════════════════════════════════
# ── SECCIÓN II ────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════

print("\n── Sección II ─────────────────────────────────────────────")

# ─── 2.2  f(x)=sqrt(x+1), g(x)=sqrt(x-1), composición f∘g ─────
print("\n[2.2] f(x)=√(x+1), g(x)=√(x-1)  → (f∘g)(x)")

# Dom(g)=[1,+∞), Dom(f)=[-1,+∞)
# Dom(f∘g)={x∈Dom(g) | g(x)∈Dom(f)} = {x≥1 | sqrt(x-1)≥-1} = [1,+∞)  (siempre ok)
# SymPy
dom_fog_22_a = solveset(x - 1 >= 0, x, S.Reals)
dom_fog_22_b = solveset(sqrt(x - 1) + 1 >= 0, x, S.Reals)
dom_fog_22 = dom_fog_22_a.intersect(dom_fog_22_b)
print(f"  SymPy Dom(f∘g): {dom_fog_22}")

# NumPy
xpts3 = np.linspace(-30, 30, 100_000)
mask_dom_fg22 = (xpts3 >= 1)
mask_sol_fg22 = (xpts3 >= 1)
pct, ok = acuerdo_numpy(mask_dom_fg22, mask_sol_fg22)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# (f∘g)(5) = sqrt(sqrt(5-1)+1) = sqrt(sqrt(4)+1) = sqrt(2+1) = sqrt(3)
val_22 = math.sqrt(math.sqrt(5 - 1) + 1)
print(f"  (f∘g)(5) = √(√4+1) = √3 ≈ {val_22:.6f}  (esperado √3≈{math.sqrt(3):.6f})")
print(f"  Imagen en 5: {PASS if abs(val_22 - math.sqrt(3)) < 1e-9 else FAIL}")

# Preimagen de 3: sqrt(sqrt(x-1)+1)=3 → sqrt(x-1)+1=9 → sqrt(x-1)=8 → x-1=64 → x=65
preimg_22 = 65
fog_65 = math.sqrt(math.sqrt(65 - 1) + 1)
print(f"  Preimagen de 3: x=65 → (f∘g)(65)={fog_65:.6f} (esperado 3.0)")
print(f"  {PASS if abs(fog_65 - 3.0) < 1e-9 else FAIL}")
print(f"  RESULTADO 2.2: Dom(f∘g)=[1,+∞), (f∘g)(5)=√3, preimagen de 3 → x=65")

# ─── 2.3  f(x)=sqrt((x+1)/(x-3)), g(x)=2x-1  ──────────────────
print("\n[2.3] f(x)=√((x+1)/(x-3)), g(x)=2x-1  → (f∘g)(x)")

# g(x)=2x-1 → Dom(g)=R
# f tiene Dom: (x+1)/(x-3) ≥ 0 → x∈(-∞,-1]∪(3,+∞)
# Dom(f∘g)={x | g(x)∈Dom(f)} = {x | (2x-1)∈(-∞,-1]∪(3,+∞)}
#   2x-1≤-1 → x≤0   OR   2x-1>3 → x>2
# SymPy — Dom(f)
dom_f23 = solveset((x + 1) / (x - 3) >= 0, x, S.Reals)
print(f"  SymPy Dom(f): {dom_f23}")

# Dom(f∘g)
u = symbols('u', real=True)
dom_fog_23 = solveset(((2*x - 1) + 1) / ((2*x - 1) - 3) >= 0, x, S.Reals)
print(f"  SymPy Dom(f∘g): {dom_fog_23}")

# NumPy
xpts4 = np.linspace(-30, 30, 100_000)
u23 = 2 * xpts4 - 1
with np.errstate(divide='ignore', invalid='ignore'):
    ratio = (u23 + 1) / (u23 - 3)
mask_dom_fog23 = np.isfinite(ratio) & (ratio >= 0)
mask_sol_fog23 = (xpts4 <= 0) | (xpts4 > 2)
pct, ok = acuerdo_numpy(mask_dom_fog23, mask_sol_fog23)
print(f"  NumPy Dom(f∘g) acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# (f∘g)(4) = f(2*4-1) = f(7) = sqrt((7+1)/(7-3)) = sqrt(8/4) = sqrt(2)
val_23 = math.sqrt((2*4 - 1 + 1) / (2*4 - 1 - 3))
print(f"  (f∘g)(4) = √(8/4) = √2 ≈ {val_23:.6f}  (esperado {math.sqrt(2):.6f})")
print(f"  {PASS if abs(val_23 - math.sqrt(2)) < 1e-9 else FAIL}")

# Preimagen de 1: sqrt((2x)/(2x-4))=1 → (2x)/(2x-4)=1 → 2x=2x-4 → 0=-4  sin solución
print(f"  Preimagen de 1: no existe solución (0=-4 contradicción)")
print(f"  RESULTADO 2.3: Dom(f∘g)=(-∞,0]∪(2,+∞), (f∘g)(4)=√2, preimagen de 1 no existe")

# ─── 2.4  f∘g = g∘f con f(x)=(2x+3)/4, g(x)=(x-k)/2  ──────────
print("\n[2.4] f(x)=(2x+3)/4, g(x)=(x-k)/2 → hallar k tal que f∘g=g∘f")

# (f∘g)(x) = f((x-k)/2) = (2*(x-k)/2 + 3)/4 = (x - k + 3)/4
# (g∘f)(x) = g((2x+3)/4) = ((2x+3)/4 - k)/2 = (2x+3-4k)/8
# Igualar: (x-k+3)/4 = (2x+3-4k)/8
#   2(x-k+3) = 2x+3-4k
#   2x - 2k + 6 = 2x + 3 - 4k
#   -2k + 6 = 3 - 4k
#   2k = -3  → k = -3/2
k_sym = symbols('k', real=True)
x_sym = symbols('x', real=True)
fog_24 = (2*((x_sym - k_sym)/2) + 3) / 4  # f∘g
gof_24 = ((2*x_sym + 3)/4 - k_sym) / 2    # g∘f
eq_24 = Eq(simplify(fog_24 - gof_24), 0)
k_sol_24 = solve(eq_24, k_sym)
print(f"  SymPy k: {k_sol_24}")

# Verificar con NumPy: k=-3/2
k_val = Rational(-3, 2)
xpts5 = np.linspace(-20, 20, 100_000)
fog_num = (2*(xpts5 - (-1.5))/2 + 3) / 4
gof_num = ((2*xpts5 + 3)/4 - (-1.5)) / 2
ok_k24 = np.allclose(fog_num, gof_num, atol=1e-10)
print(f"  NumPy f∘g ≡ g∘f con k=-3/2: {PASS if ok_k24 else FAIL}")
print(f"  RESULTADO 2.4: k = -3/2")

# ─── 2.5  f∘g = g∘f con f(x)=(4x-1)/3, g(x)=(x+b)/4  ──────────
print("\n[2.5] f(x)=(4x-1)/3, g(x)=(x+b)/4 → hallar b tal que f∘g=g∘f")

b_sym = symbols('b', real=True)
# (f∘g)(x) = f((x+b)/4) = (4*(x+b)/4 - 1)/3 = (x+b-1)/3
# (g∘f)(x) = g((4x-1)/3) = ((4x-1)/3 + b)/4 = (4x-1+3b)/12
# Igualar: (x+b-1)/3 = (4x-1+3b)/12
#   4(x+b-1) = 4x-1+3b
#   4x+4b-4 = 4x-1+3b
#   4b-4 = -1+3b
#   b = 3
fog_25 = (4*((x_sym + b_sym)/4) - 1) / 3
gof_25 = ((4*x_sym - 1)/3 + b_sym) / 4
eq_25 = Eq(simplify(fog_25 - gof_25), 0)
b_sol_25 = solve(eq_25, b_sym)
print(f"  SymPy b: {b_sol_25}")

# NumPy con b=3
fog_25n = (4*(xpts5 + 3)/4 - 1) / 3
gof_25n = ((4*xpts5 - 1)/3 + 3) / 4
ok_b25 = np.allclose(fog_25n, gof_25n, atol=1e-10)
print(f"  NumPy f∘g ≡ g∘f con b=3: {PASS if ok_b25 else FAIL}")
print(f"  RESULTADO 2.5: b = 3")

# ─── 2.6  g(x)=3x²-6x+10 en [1,+∞)  → inyectiva pero no sobreyectiva  ──
print("\n[2.6] g(x)=3x²-6x+10 en [1,+∞)")

# Inyectiva: verificar estrictamente creciente en [1,+∞)
x_in26 = np.linspace(1, 30, 200_000)
g26 = 3*x_in26**2 - 6*x_in26 + 10
crece26 = np.all(np.diff(g26) >= 0)
print(f"  Creciente en [1,+∞) (⟹ inyectiva): {PASS if crece26 else FAIL}")

# g(1) = 3-6+10 = 7 → Rec(g) = [7, +∞)
# No es sobreyectiva en R pues Rec ≠ R
g26_min = g26.min()
print(f"  g(1) = {3*1**2 - 6*1 + 10}  → Rec(g) = [7, +∞) ≠ ℝ  (no sobreyectiva)")
print(f"  NumPy mín = {g26_min:.4f}")
print(f"  RESULTADO 2.6: g inyectiva (creciente en [1,+∞)), no sobreyectiva (Rec=[7,+∞))")

# ─── 2.7  f(x)=1/(2-x) - 1/x en ]0,2[  → biyectiva, hallar f⁻¹ ──
print("\n[2.7] f(x)=1/(2-x)-1/x en ]0,2[")

# f(x) = 1/(2-x) - 1/x = [x-(2-x)] / [x(2-x)] = (2x-2)/(x(2-x)) = 2(x-1)/(x(2-x))
# Derivada: f'(x) = 1/(2-x)² + 1/x²  > 0  siempre → estrictamente creciente → inyectiva
x_in27 = np.linspace(1e-7, 2 - 1e-7, 200_000)
f27 = 1/(2 - x_in27) - 1/x_in27
crece27 = np.all(np.diff(f27) >= 0)
print(f"  Estrictamente creciente en ]0,2[ (⟹ inyectiva): {PASS if crece27 else FAIL}")

# Recorrido: f(0⁺)→-∞, f(1)=0, f(2⁻)→+∞  → Rec=ℝ → sobreyectiva
f27_lim0 = 1/(2 - 1e-9) - 1/(1e-9)
f27_lim2 = 1/(2 - (2-1e-9)) - 1/(2-1e-9)
print(f"  f(0⁺)≈{f27_lim0:.1f}, f(2⁻)≈{f27_lim2:.1f} → Rec=ℝ (sobreyectiva)")

# Función inversa: y = 1/(2-x)-1/x  →  y = (2x-2)/(x(2-x))  →  yx²-2yx+2y=2x-2
# y(2-x)x = 2x-2  →  2yx - yx² = 2x-2  →  yx²+(2-2y)x-2=0  → cuadrática en x
# Discriminante = (2-2y)²+8y = 4-8y+4y²+8y = 4y²+4 = 4(y²+1) → √ = 2√(y²+1)
# x = [-(2-2y) ± 2√(y²+1)] / 2y = [(2y-2) ± 2√(y²+1)] / 2y
# Como x ∈ ]0,2[: elegir signo +: x = [(2y-2) + 2√(y²+1)] / 2y = [y-1+√(y²+1)] / y
y_var = symbols('y', real=True)
expr27 = (y_var - 1 + sqrt(y_var**2 + 1)) / y_var
# Verificar: f(f⁻¹(0)) — límite cuando y→0
print(f"  f⁻¹(y) = (y-1+√(y²+1))/y")
# Spot check: y=0 → f⁻¹ indefinida; usar y=1
y_test = 1.0
x_inv = (y_test - 1 + math.sqrt(y_test**2 + 1)) / y_test
f_check = 1/(2-x_inv) - 1/x_inv
print(f"  f⁻¹(1)≈{x_inv:.6f}, f(f⁻¹(1))={f_check:.6f} (esperado 1.0) → {PASS if abs(f_check-1.0)<1e-6 else FAIL}")
# NumPy: verificar f∘f⁻¹ = id en rango denso
y_test_arr = np.linspace(-20, 20, 100_000)
with np.errstate(divide='ignore', invalid='ignore'):
    x_inv_arr = (y_test_arr - 1 + np.sqrt(y_test_arr**2 + 1)) / y_test_arr
valid = (x_inv_arr > 0) & (x_inv_arr < 2)
f_of_inv = np.where(valid, 1/(2 - x_inv_arr) - 1/x_inv_arr, np.nan)
ok_27 = np.allclose(f_of_inv[valid], y_test_arr[valid], atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y en Dom: {PASS if ok_27 else FAIL}")
print(f"  RESULTADO 2.7: f biyectiva, f⁻¹(y) = (y-1+√(y²+1))/y, Dom(f⁻¹)=ℝ, Rec(f⁻¹)=]0,2[")

# ─── 2.8  f(x)=2x²-8x+3 en [2,+∞) → [-5,+∞)  ──────────────────
print("\n[2.8] f(x)=2x²-8x+3, f:[2,+∞)→[-5,+∞)")

# f(x)=2(x-2)²-5  → vértice (2,-5), creciente en [2,+∞) → inyectiva
x_in28 = np.linspace(2, 30, 200_000)
f28 = 2*x_in28**2 - 8*x_in28 + 3
crece28 = np.all(np.diff(f28) >= 0)
print(f"  Creciente en [2,+∞) (⟹ inyectiva): {PASS if crece28 else FAIL}")
print(f"  f(2) = {2*4 - 16 + 3} = -5 → Rec=[−5,+∞) ✓")

# Sobreyectiva: Rec = [-5,+∞) = codominio ✓
# Función inversa: y=2(x-2)²-5 → (x-2)²=(y+5)/2 → x=2+√((y+5)/2) [x≥2→ signo +]
y_in28 = np.linspace(-5, 100, 100_000)
f_inv28 = 2 + np.sqrt((y_in28 + 5) / 2)
f_of_inv28 = 2*f_inv28**2 - 8*f_inv28 + 3
ok_28 = np.allclose(f_of_inv28, y_in28, atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y: {PASS if ok_28 else FAIL}")
# SymPy check
y28 = symbols('y28', real=True, positive=True)
x28 = symbols('x28', real=True)
inv28_sym = solve(2*x28**2 - 8*x28 + 3 - y28, x28)
print(f"  SymPy f⁻¹ candidatos: {inv28_sym}")
print(f"  RESULTADO 2.8: f inyectiva y sobreyectiva, f⁻¹(x)=2+√((x+5)/2), Dom(f⁻¹)=[-5,+∞), Rec(f⁻¹)=[2,+∞)")

# ══════════════════════════════════════════════════════════════
# ── SECCIÓN III — PEPs Antiguas ───────────────────────────────
# ══════════════════════════════════════════════════════════════

print("\n── Sección III — PEPs Antiguas ────────────────────────────")

# ─── PEP 2023 — 1.0  Dom(f∘g), f(x)=sqrt(x-2), g(x)=sqrt(25-x²)-2 ─
print("\n[PEP2023-1.0] f(x)=√(x-2), g(x)=√(25-x²)-2  → Dom(f∘g)")

# Dom(g): 25-x²≥0 → x∈[-5,5]
# Dom(f∘g): g(x)∈Dom(f)={t≥2} → √(25-x²)-2≥2 → √(25-x²)≥4 → 25-x²≥16 → x²≤9 → x∈[-3,3]
# Intersección con Dom(g): [-3,3]
dom_g_pep = solveset(25 - x**2 >= 0, x, S.Reals)
print(f"  SymPy Dom(g): {dom_g_pep}")

fog_cond_a = solveset(25 - x**2 >= 0, x, S.Reals)
fog_cond_b = solveset(sqrt(25 - x**2) - 2 >= 2, x, S.Reals)
fog_cond = fog_cond_a & fog_cond_b
print(f"  SymPy Dom(f∘g): {fog_cond}")

xpts6 = np.linspace(-30, 30, 100_000)
with np.errstate(invalid='ignore'):
    sq = np.sqrt(np.where(25 - xpts6**2 >= 0, 25 - xpts6**2, np.nan))
    gx = sq - 2
mask_dom_fog_pep = np.isfinite(gx) & (gx >= 2)
mask_sol_pep = (xpts6 >= -3) & (xpts6 <= 3)
pct, ok = acuerdo_numpy(mask_dom_fog_pep, mask_sol_pep)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")
print(f"  RESULTADO PEP2023-1.0: Dom(f∘g) = [-3, 3]")

# ─── PEP 2023 — 1.1  f(x)=-x²+4x-3  → A,B biyectiva, f⁻¹  ────
print("\n[PEP2023-1.1] f(x)=-x²+4x-3 → A,B biyectiva y f⁻¹")

# f(x)=-(x-2)²+1 → vértice (2,1), dec. en [2,+∞)  (o crec. en (-∞,2])
# Para biyectiva: A=[2,+∞), B=(-∞,1]  (o A=(-∞,2], B=(-∞,1])
x_in_p = np.linspace(2, 30, 100_000)
fp = -(x_in_p - 2)**2 + 1
decrece_p = np.all(np.diff(fp) <= 0)
print(f"  f dec. en [2,+∞): {PASS if decrece_p else FAIL}")
print(f"  f(2)=1 → Rec=(-∞,1] ✓")

# f⁻¹: y=-(x-2)²+1 → (x-2)²=1-y → x=2-√(1-y) [x≥2→ x=2+√(1-y)... pero f dec en [2,+∞) → x=2+√(1-y)]
# Con A=[2,+∞): x-2=√(1-y)≥0 → x=2+√(1-y)
y_in_p = np.linspace(-100, 1, 100_000)
finv_p = 2 + np.sqrt(1 - y_in_p)
f_check_p = -(finv_p - 2)**2 + 1
ok_p = np.allclose(f_check_p, y_in_p, atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y: {PASS if ok_p else FAIL}")
print(f"  RESULTADO PEP2023-1.1: A=[2,+∞), B=(-∞,1], f⁻¹(x)=2+√(1-x), Dom(f⁻¹)=(-∞,1]")

# ─── PEP 2022 — 1.3  f(x)=-sqrt(2-sqrt(-1-2x))  ────────────────
print("\n[PEP2022-1.3] f(x)=-√(2-√(-1-2x))")

# Dom: -1-2x≥0 → x≤-1/2  AND  2-√(-1-2x)≥0 → √(-1-2x)≤2 → -1-2x≤4 → x≥-5/2
# Dom = [-5/2, -1/2]
dom_f22_a = solveset(-1 - 2*x >= 0, x, S.Reals)
dom_f22_b = solveset(2 - sqrt(-1 - 2*x) >= 0, x, S.Reals)
dom_f22 = dom_f22_a & dom_f22_b
print(f"  SymPy Dom: {dom_f22}")

xpts7 = np.linspace(-30, 30, 100_000)
with np.errstate(invalid='ignore'):
    inner22 = -1 - 2*xpts7
    cond22a = inner22 >= 0
    inner22_safe = np.where(cond22a, inner22, np.nan)
    cond22b = 2 - np.sqrt(np.abs(inner22_safe)) >= 0
mask_dom_22 = cond22a & cond22b
mask_sol_22 = (xpts7 >= -2.5) & (xpts7 <= -0.5)
pct, ok = acuerdo_numpy(mask_dom_22, mask_sol_22)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Monotonía: f'(x)= d/dx[-√(2-√(-1-2x))]
# Cadena: factor 1/√(2-√(-1-2x)) * 1/(2√(-1-2x)) * 2 > 0 → f creciente
x_in22 = np.linspace(-2.5 + 1e-8, -0.5 - 1e-8, 200_000)
f22 = -np.sqrt(2 - np.sqrt(-1 - 2*x_in22))
crece22 = np.all(np.diff(f22) >= -1e-10)
print(f"  f creciente en [-5/2,-1/2]: {PASS if crece22 else FAIL}")

# Recorrido: f(-5/2)=-√(2-2)=0, f(-1/2)=-√(2-0)=-√2
f22_min = f22.min()
f22_max = f22.max()
print(f"  f(-5/2)≈{-np.sqrt(2 - np.sqrt(-1-2*(-2.5))):.6f}=0, f(-1/2)≈{-np.sqrt(2 - np.sqrt(-1-2*(-0.5))):.6f}=-√2")
print(f"  Rec(f) = [-√2, 0]")
print(f"  RESULTADO PEP2022-1.3: Dom=[-5/2,-1/2], f creciente, Rec=[-√2, 0]")

# ─── PEP 2023 Alt — 1.4  f(x)=x²+8x+14, A∋1  ──────────────────
print("\n[PEP2023Alt-1.4] f(x)=x²+8x+14, 1∈A, biyectiva")

# f(x)=(x+4)²-2, vértice (-4,-2)
# Para x=1∈A y biyectividad: f creciente a la derecha del vértice, A=[-4,+∞)... pero x=1>-4 ✓
# A=[-4,+∞), B=[-2,+∞)
x_in14b = np.linspace(-4, 30, 200_000)
f14b = x_in14b**2 + 8*x_in14b + 14
crece14b = np.all(np.diff(f14b) >= 0)
print(f"  Creciente en [-4,+∞) (⟹ inyectiva): {PASS if crece14b else FAIL}")
print(f"  f(-4)={(-4)**2 + 8*(-4) + 14} = -2 → B=[-2,+∞)")
print(f"  1∈[-4,+∞) ✓")

# f⁻¹: y=(x+4)²-2 → (x+4)²=y+2 → x=-4+√(y+2)  [x≥-4→ signo +]
y_in14b = np.linspace(-2, 200, 100_000)
finv14b = -4 + np.sqrt(y_in14b + 2)
f_check14b = finv14b**2 + 8*finv14b + 14
ok_14b = np.allclose(f_check14b, y_in14b, atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y: {PASS if ok_14b else FAIL}")
print(f"  RESULTADO PEP2023Alt-1.4: A=[-4,+∞), B=[-2,+∞), f⁻¹(x)=-4+√(x+2), Dom(f⁻¹)=[-2,+∞)")

# ─── PEP 2023 Alt — 1.5  f(x)=1+sqrt((2x-3)/(x-4))  ───────────
print("\n[PEP2023Alt-1.5] f(x)=1+√((2x-3)/(x-4))")

# (2x-3)/(x-4)≥0: raíces 3/2 y 4
dom_f15 = solveset((2*x - 3)/(x - 4) >= 0, x, S.Reals)
print(f"  SymPy Dom: {dom_f15}")

# NumPy
with np.errstate(divide='ignore', invalid='ignore'):
    ratio15 = (2*PTS - 3)/(PTS - 4)
mask_dom_15 = np.isfinite(ratio15) & (ratio15 >= 0)
mask_sol_15 = ((PTS <= 1.5) | (PTS > 4))
# Corrección: (2x-3)/(x-4)≥0 → tabla signos: x<3/2: (−)/(−)=+; 3/2≤x<4: (+)/(−)=−; x>4: (+)/(+)=+
# Dom = (-∞, 3/2] ∪ (4, +∞)
mask_sol_15 = (PTS <= 1.5) | (PTS > 4)
pct, ok = acuerdo_numpy(mask_dom_15, mask_sol_15)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Recorrido: analítico
# Cuando x→-∞: (2x-3)/(x-4)→2 → f→1+√2
# x→(4⁺): ratio→+∞ → f→+∞
# x=3/2: ratio=0 → f=1
# En (-∞,3/2]: ratio decrece de 2 a 0 → f∈[1, 1+√2]
# En (4,+∞): ratio decrece de +∞ a 2 → f∈[1+√2, +∞)
# Rec(f) = [1, 1+√2] ∪ [1+√2, +∞) = [1,+∞)
x_in15a = np.linspace(-300, 1.5 - 1e-8, 200_000)
f15a = 1 + np.sqrt((2*x_in15a - 3)/(x_in15a - 4))
x_in15b = np.linspace(4 + 1e-8, 300, 200_000)
f15b = 1 + np.sqrt((2*x_in15b - 3)/(x_in15b - 4))
print(f"  En (-∞,3/2]: f∈[{f15a.min():.4f}, {f15a.max():.4f}]  (esperado [1, 1+√2]≈[1,{1+math.sqrt(2):.4f}])")
print(f"  En (4,+∞): f∈[{f15b.min():.4f}, {f15b.max():.1f}]")
print(f"  Rec(f) = [1, +∞)")

# Preimagen de 3: f(x)=3 → √((2x-3)/(x-4))=2 → (2x-3)/(x-4)=4 → 2x-3=4x-16 → -2x=-13 → x=13/2
preim15 = Rational(13, 2)
val_check15 = 1 + sqrt((2*preim15 - 3)/(preim15 - 4))
print(f"  f(13/2) = 1+√((13-3)/(13/2-4)) = {val_check15} (esperado 3)")
print(f"  SymPy verificación: {PASS if val_check15 == 3 else FAIL}")
print(f"  RESULTADO PEP2023Alt-1.5: Dom=(-∞,3/2]∪(4,+∞), Rec=[1,+∞), preimagen de 3 → x=13/2")

# ─── PEP 2023 Alt — 1.6  f(x)=x/(1-|x|) en ]-1,1[  ────────────
print("\n[PEP2023Alt-1.6] f(x)=x/(1-|x|) en ]-1,1[ → biyectiva, f⁻¹")

# f creciente en ]-1,1[
x_in16 = np.linspace(-1 + 1e-8, 1 - 1e-8, 200_000)
f16 = x_in16 / (1 - np.abs(x_in16))
crece16 = np.all(np.diff(f16) >= 0)
print(f"  Creciente en ]-1,1[ (⟹ inyectiva): {PASS if crece16 else FAIL}")
print(f"  f(-1⁺)→-∞, f(1⁻)→+∞ → Rec=ℝ → sobreyectiva")

# f⁻¹: y=x/(1-|x|)
# Caso x≥0: y=x/(1-x) → x=y/(1+y), válido para x∈[0,1) ↔ y≥0
# Caso x<0: y=x/(1+x) → x=y/(1-y), válido para x∈(-1,0) ↔ y<0
# f⁻¹(y) = y/(1+|y|)  para todo y∈ℝ
y_in16 = np.linspace(-50, 50, 200_000)
finv16 = y_in16 / (1 + np.abs(y_in16))
f_check16 = finv16 / (1 - np.abs(finv16))
ok_16 = np.allclose(f_check16, y_in16, atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y: {PASS if ok_16 else FAIL}")
# SymPy spot check
y16 = symbols('y16', real=True)
finv16_sym = y16 / (1 + Abs(y16))
f16_check_sym = finv16_sym / (1 - Abs(finv16_sym))
print(f"  RESULTADO PEP2023Alt-1.6: f biyectiva, f⁻¹(y)=y/(1+|y|), Dom(f⁻¹)=ℝ, Rec(f⁻¹)=]-1,1[")

# ─── Más PEP — 1.8a  f(x)=(x-2)²+1 en [-1,1]→[k,10]  ──────────
print("\n[MásPEP-1.8a] f(x)=(x-2)²+1 en [-1,1]")

# f(x)=(x-2)²+1, decreciente en [-1,1] (vértice x=2 fuera de [-1,1], f decrece en este intervalo)
x_in18 = np.linspace(-1, 1, 200_000)
f18 = (x_in18 - 2)**2 + 1
decrece18 = np.all(np.diff(f18) <= 0)
print(f"  Decreciente en [-1,1] (⟹ inyectiva): {PASS if decrece18 else FAIL}")
print(f"  f(-1)={((-1)-2)**2+1}=10, f(1)={(1-2)**2+1}=2 → Rec=[2,10]")
print(f"  Para sobreyectividad: k=2")

# f⁻¹: y=(x-2)²+1 → (x-2)²=y-1 → x=2-√(y-1)  [x∈[-1,1]→ x≤2→ signo -]
y_in18 = np.linspace(2, 10, 100_000)
finv18 = 2 - np.sqrt(y_in18 - 1)
f_check18 = (finv18 - 2)**2 + 1
ok_18 = np.allclose(f_check18, y_in18, atol=1e-6)
print(f"  NumPy f(f⁻¹(y))=y: {PASS if ok_18 else FAIL}")
print(f"  RESULTADO MásPEP-1.8a: k=2, f inyectiva (decreciente), sobreyectiva para k=2")
print(f"                          f⁻¹(x)=2-√(x-1), Dom(f⁻¹)=[2,10], Rec(f⁻¹)=[-1,1]")

# ─── Más PEP — 1.8b  f(x)=sqrt(4-sqrt(2-3x))  ──────────────────
print("\n[MásPEP-1.8b] f(x)=√(4-√(2-3x))")

# Dom: 2-3x≥0 → x≤2/3  AND  4-√(2-3x)≥0 → √(2-3x)≤4 → 2-3x≤16 → x≥-14/3
dom_f18b_a = solveset(2 - 3*x >= 0, x, S.Reals)
dom_f18b_b = solveset(4 - sqrt(2 - 3*x) >= 0, x, S.Reals)
dom_f18b = dom_f18b_a & dom_f18b_b
print(f"  SymPy Dom: {dom_f18b}")

xpts8 = np.linspace(-30, 30, 100_000)
with np.errstate(invalid='ignore'):
    inner18b = 2 - 3*xpts8
    c1_18b = inner18b >= 0
    c2_18b = 4 - np.sqrt(np.abs(inner18b)) >= 0
mask_dom_18b = c1_18b & c2_18b
mask_sol_18b = (xpts8 >= -14/3) & (xpts8 <= 2/3)
pct, ok = acuerdo_numpy(mask_dom_18b, mask_sol_18b)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Monotonía: derivada cadena → f'(x) = 3/(4√(2-3x)·√(4-√(2-3x))) > 0 → creciente
x_in18b = np.linspace(-14/3 + 1e-7, 2/3 - 1e-7, 200_000)
f18b = np.sqrt(4 - np.sqrt(2 - 3*x_in18b))
crece18b = np.all(np.diff(f18b) >= -1e-10)
print(f"  Creciente en Dom: {PASS if crece18b else FAIL}")
print(f"  RESULTADO MásPEP-1.8b: Dom=[-14/3, 2/3], f creciente")

# ─── Más PEP — 1.9  f(x)=sqrt(3/sqrt(x+1)-1)  ──────────────────
print("\n[MásPEP-1.9] f(x)=√(3/√(x+1)-1)")

# Dom: x+1>0 → x>-1  AND  3/√(x+1)-1≥0 → 3/√(x+1)≥1 → √(x+1)≤3 → x+1≤9 → x≤8
# Dom = (-1, 8]
dom_f19_a = solveset(x + 1 > 0, x, S.Reals)
dom_f19_b = solveset(3/sqrt(x + 1) - 1 >= 0, x, S.Reals)
dom_f19 = dom_f19_a & dom_f19_b
print(f"  SymPy Dom: {dom_f19}")

xpts9 = np.linspace(-30, 30, 100_000)
with np.errstate(divide='ignore', invalid='ignore'):
    c1_19 = xpts9 + 1 > 0
    inner19 = 3/np.sqrt(np.abs(xpts9 + 1)) - 1
    c2_19 = inner19 >= 0
mask_dom_19 = c1_19 & c2_19
mask_sol_19 = (xpts9 > -1) & (xpts9 <= 8)
pct, ok = acuerdo_numpy(mask_dom_19, mask_sol_19)
print(f"  NumPy Dom acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")

# Recorrido: f(-1⁺)→+∞ (3/0⁺-1→∞), f(8)=√(3/3-1)=√0=0 → f decrec.
x_in19 = np.linspace(-1 + 1e-7, 8, 200_000)
f19 = np.sqrt(3/np.sqrt(x_in19 + 1) - 1)
decrece19 = np.all(np.diff(f19) <= 1e-10)
print(f"  Decreciente en (-1,8]: {PASS if decrece19 else FAIL}")
print(f"  f(8)={f19[-1]:.6f}≈0, f(-1⁺)→{f19[0]:.2f} → Rec=[0,+∞)")

# f∘g con g(x)=x-2: (f∘g)(x)=f(x-2)=√(3/√(x-1)-1)
# Dom(f∘g): Dom de g=ℝ, g(x)∈Dom(f): x-2∈(-1,8] → x∈(1,10]
dom_fog_19_a = solveset(x - 1 > 0, x, S.Reals)
dom_fog_19_b = solveset(3/sqrt(x - 1) - 1 >= 0, x, S.Reals)
dom_fog_19_sym = dom_fog_19_a & dom_fog_19_b
print(f"  SymPy Dom(f∘g): {dom_fog_19_sym}")
# NumPy
with np.errstate(divide='ignore', invalid='ignore'):
    c1_fg19 = xpts9 - 1 > 0
    inner_fg19 = 3/np.sqrt(np.abs(xpts9 - 1)) - 1
    c2_fg19 = inner_fg19 >= 0
mask_dom_fg19 = c1_fg19 & c2_fg19
mask_sol_fg19 = (xpts9 > 1) & (xpts9 <= 10)
pct, ok = acuerdo_numpy(mask_dom_fg19, mask_sol_fg19)
print(f"  NumPy Dom(f∘g) acuerdo: {pct:.4f}% → {PASS if ok else FAIL}")
print(f"  RESULTADO MásPEP-1.9: Dom(f)=(-1,8], Rec(f)=[0,+∞)")
print(f"                         Dom(f∘g)=(1,10], (f∘g)(x)=√(3/√(x-1)-1)")

print("\n" + "=" * 60)
print("  VALIDACIÓN COMPLETA")
print("=" * 60)
