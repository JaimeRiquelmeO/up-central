"""
VALIDACIÓN PASO A PASO — Solucionario Avanzado + PEP
Guía Práctica de Funciones — Cálculo I — Usach Premium

Ejercicios: 11, 12, 13 (Avanzado) y 14, 15 (PEP)
Valida cada paso intermedio antes de incluirlo en el PDF.

Librerías: SymPy (simbólico) + NumPy (numérico, ≥ 100 000 puntos)
"""
from sympy import *
import numpy as np, math

x, y, t = symbols('x y t', real=True)

OK   = "\033[92m✔ PASS\033[0m"
FAIL = "\033[91m✗ FAIL\033[0m"
SEP  = "─" * 60
steps = {}   # tag → bool

def chk(tag, ok, detalle=""):
    steps[tag] = bool(ok)
    s = OK if ok else FAIL
    print(f"  {s}  {tag}")
    if detalle:
        print(f"       ↳ {detalle}")

PTS = np.sort(np.concatenate([
    np.linspace(-50, 50, 70_000) + 1e-6 * math.pi,
    np.random.default_rng(7).uniform(-50, 50, 30_000)
]))

# ══════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("  EJERCICIO 11 — f(x) = x/(x+2) en [0,+∞) → [0,1)")
print(f"{'='*60}")

# ── Paso 1: f'(x) > 0 → f estrictamente creciente ────────────
print(f"\n{SEP}\n  Paso 1: Derivada → inyectividad\n{SEP}")
f11   = x / (x + 2)
fp11  = diff(f11, x)   # debe ser 2/(x+2)^2

chk("11.P1a — f'(x) = 2/(x+2)²",
    simplify(fp11 - 2/(x+2)**2) == 0,
    f"f'(x) = {fp11}")

# f'(x) > 0 para todo x > -2 (en particular para x ≥ 0)
ok_pos = fp11.subs(x, 0) > 0 and fp11.subs(x, 10) > 0
chk("11.P1b — f'(0)>0, f'(10)>0",
    ok_pos,
    f"f'(0)={fp11.subs(x,0)}, f'(10)={fp11.subs(x,10)}")

x_in11 = np.linspace(0, 500, 500_000)
f11n   = x_in11 / (x_in11 + 2)
chk("11.P1c — f creciente en [0,+∞) NumPy",
    bool(np.all(np.diff(f11n) >= 0)))

# ── Paso 2: Recorrido = [0,1) ─────────────────────────────────
print(f"\n{SEP}\n  Paso 2: Recorrido\n{SEP}")

f11_at0 = f11.subs(x, 0)
chk("11.P2a — f(0) = 0",
    f11_at0 == 0,
    f"f(0) = {f11_at0}")

lim11 = limit(f11, x, oo)
chk("11.P2b — lím f(x) = 1 cuando x→+∞",
    lim11 == 1,
    f"límite = {lim11}")

# Numéricamente: min = 0, sup < 1 siempre
chk("11.P2c — Rec = [0,1) NumPy",
    abs(f11n.min()) < 1e-9 and f11n.max() < 1.0,
    f"min={f11n.min():.4f}, max={f11n.max():.8f} < 1")

# ── Paso 3: f⁻¹(y) = 2y/(1-y) ────────────────────────────────
print(f"\n{SEP}\n  Paso 3: Función inversa\n{SEP}")

# Despejar x: y = x/(x+2) → y(x+2) = x → xy+2y = x → x(y-1) = -2y → x = 2y/(1-y)
finv11_sym = solve(Eq(y, x/(x+2)), x)
chk("11.P3a — SymPy despeja x = 2y/(1-y)",
    any(simplify(s - 2*y/(1-y)) == 0 for s in finv11_sym),
    f"SymPy inversa: {finv11_sym}")

# Verificar f(f⁻¹(y)) = y
y_test11 = np.linspace(0, 1-1e-7, 200_000)
finv11n  = 2*y_test11 / (1 - y_test11)
fofInv11 = finv11n / (finv11n + 2)
chk("11.P3b — f(f⁻¹(y)) = y NumPy",
    np.allclose(fofInv11, y_test11, atol=1e-6),
    f"max error = {abs(fofInv11 - y_test11).max():.2e}")

# Dom(f⁻¹) = [0,1), Rec(f⁻¹) = [0,+∞)
chk("11.P3c — Rec(f⁻¹) ⊆ [0,+∞)",
    bool(np.all(finv11n >= 0)),
    f"min(f⁻¹) = {finv11n.min():.4f}")

# ══════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("  EJERCICIO 12 — f(x) = -x²+6x-5, 3∈A → A=[3,+∞), B=(-∞,4]")
print(f"{'='*60}")

# ── Paso 1: Completar el cuadrado ─────────────────────────────
print(f"\n{SEP}\n  Paso 1: Forma canónica\n{SEP}")

f12     = -x**2 + 6*x - 5
f12_can = -(x-3)**2 + 4
chk("12.P1a — f(x) = -(x-3)²+4",
    simplify(f12 - f12_can) == 0,
    f"expand: {expand(f12_can)}")

chk("12.P1b — Vértice en (3, 4)",
    f12.subs(x, 3) == 4 and f12_can.subs(x, 3) == 4)

# ── Paso 2: Monotonía en [3,+∞) ──────────────────────────────
print(f"\n{SEP}\n  Paso 2: Decrecimiento en [3,+∞)\n{SEP}")

fp12 = diff(f12, x)   # = -2x+6 = -2(x-3)
chk("12.P2a — f'(x) = -2(x-3)",
    simplify(fp12 - (-2*(x-3))) == 0,
    f"f'(x) = {fp12}")

chk("12.P2b — f'(x) ≤ 0 para x ≥ 3",
    fp12.subs(x, 3) == 0 and fp12.subs(x, 4) < 0 and fp12.subs(x, 100) < 0)

x_in12 = np.linspace(3, 200, 500_000)
f12n   = -(x_in12 - 3)**2 + 4
chk("12.P2c — f decreciente en [3,+∞) NumPy",
    bool(np.all(np.diff(f12n) <= 1e-10)))

# ── Paso 3: Recorrido → B = (-∞, 4] ──────────────────────────
print(f"\n{SEP}\n  Paso 3: B = Rec(f) en [3,+∞)\n{SEP}")

chk("12.P3a — f(3) = 4  (máximo del recorrido)",
    f12.subs(x, 3) == 4)

lim12 = limit(f12, x, oo)
chk("12.P3b — f(x) → -∞ cuando x → +∞",
    lim12 == -oo,
    f"límite = {lim12}")

chk("12.P3c — f₁₂(n) ≤ 4 NumPy",
    bool(f12n.max() <= 4 + 1e-9),
    f"max numérico = {f12n.max():.6f}")

# ── Paso 4: Función inversa ───────────────────────────────────
print(f"\n{SEP}\n  Paso 4: Función inversa\n{SEP}")

# y = -(x-3)^2+4  ->  (x-3)^2 = 4-y  ->  x = 3 +/- sqrt(4-y)
# Como x >= 3, tomamos x = 3 + sqrt(4-y)
# Verificacion: sustituir directamente
finv12_check = 3 + sqrt(4 - y)
fofInv12_sym = simplify(-(finv12_check - 3)**2 + 4)
chk("12.P4a — f(3+sqrt(4-y)) = y SymPy",
    simplify(fofInv12_sym - y) == 0,
    f"f(f^-1(y)) = {fofInv12_sym}")

chk("12.P4b — Para x>=3 se toma signo + (verificacion en y=0)",
    float((3 + sqrt(4)).evalf()) == 5.0 and float((3 - sqrt(4)).evalf()) == 1.0,
    "3+sqrt(4)=5 in [3,+inf), 3-sqrt(4)=1 not in [3,+inf)")

y_test12 = np.linspace(-500, 4, 200_000)
finv12n  = 3 + np.sqrt(4 - y_test12)
fofInv12 = -(finv12n - 3)**2 + 4
chk("12.P4c — f(f⁻¹(y)) = y NumPy",
    np.allclose(fofInv12, y_test12, atol=1e-5),
    f"max error = {abs(fofInv12-y_test12).max():.2e}")

chk("12.P4d — Rec(f⁻¹) ⊆ [3,+∞)",
    bool(np.all(finv12n >= 3)),
    f"min(f⁻¹) = {finv12n.min():.4f}")

# ══════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("  EJERCICIO 13 — f(x) = x/(x-2) en ]2,+∞[ → B=(1,+∞)")
print(f"{'='*60}")

# ── Paso 1: Derivada → decreciente ───────────────────────────
print(f"\n{SEP}\n  Paso 1: Derivada\n{SEP}")

f13   = x / (x - 2)
fp13  = diff(f13, x)   # = -2/(x-2)²
chk("13.P1a — f'(x) = -2/(x-2)²",
    simplify(fp13 - (-2/(x-2)**2)) == 0,
    f"f'(x) = {fp13}")

chk("13.P1b — f'(x) < 0 para x > 2",
    fp13.subs(x, 3) < 0 and fp13.subs(x, 10) < 0)

x_in13 = np.linspace(2+1e-9, 500, 500_000)
f13n   = x_in13 / (x_in13 - 2)
chk("13.P1c — f decreciente en ]2,+∞[ NumPy",
    bool(np.all(np.diff(f13n) <= 0)))

# ── Paso 2: Límites → Rec = (1,+∞) ──────────────────────────
print(f"\n{SEP}\n  Paso 2: Recorrido\n{SEP}")

lim13_2p = limit(f13, x, 2, '+')
lim13_inf = limit(f13, x, oo)
chk("13.P2a — f(x) → +∞ cuando x → 2⁺",
    lim13_2p == oo,
    f"lím(x→2+) = {lim13_2p}")

chk("13.P2b — f(x) → 1 cuando x → +∞",
    lim13_inf == 1,
    f"lím(x→∞) = {lim13_inf}")

chk("13.P2c — 1 < f(x) < +∞ NumPy",
    bool(np.all(f13n > 1)) and f13n[0] > 1e5,
    f"min={f13n[-1]:.6f}>1, f(2+)={f13n[0]:.2f}")

# ── Paso 3: Inversa f⁻¹(y) = 2y/(y-1) ───────────────────────
print(f"\n{SEP}\n  Paso 3: Función inversa\n{SEP}")

# y = x/(x-2) → y(x-2)=x → xy-2y=x → x(y-1)=2y → x=2y/(y-1)
finv13_sym = solve(Eq(y, x/(x-2)), x)
chk("13.P3a — SymPy despeja x = 2y/(y-1)",
    any(simplify(s - 2*y/(y-1)) == 0 for s in finv13_sym),
    f"candidatos: {finv13_sym}")

y_test13 = np.linspace(1+1e-7, 500, 200_000)
finv13n  = 2*y_test13 / (y_test13 - 1)
fofInv13 = finv13n / (finv13n - 2)
chk("13.P3b — f(f⁻¹(y)) = y NumPy",
    np.allclose(fofInv13, y_test13, atol=1e-4),
    f"max error = {abs(fofInv13-y_test13).max():.2e}")

chk("13.P3c — Rec(f⁻¹) ⊆ (2,+∞)",
    bool(np.all(finv13n > 2)),
    f"min(f⁻¹) = {finv13n.min():.6f}")

# ══════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("  EJERCICIO 14 — f=√(x-3), g=√(25-x²)-1 → Dom(f∘g)=[-3,3]")
print(f"{'='*60}")

# ── Paso 1: Dom(f) y Dom(g) ───────────────────────────────────
print(f"\n{SEP}\n  Paso 1: Dominios individuales\n{SEP}")

sym14_domf = solveset(x - 3 >= 0, x, S.Reals)
sym14_domg = solveset(25 - x**2 >= 0, x, S.Reals)
chk("14.P1a — Dom(f) = [3,+∞)",
    sym14_domf == Interval(3, oo),
    f"Dom(f) = {sym14_domf}")

chk("14.P1b — Dom(g) = [-5,5]",
    sym14_domg == Interval(-5, 5),
    f"Dom(g) = {sym14_domg}")

# ── Paso 2: g(x) ≥ 3 → x∈[-3,3] ─────────────────────────────
print(f"\n{SEP}\n  Paso 2: Condición g(x) ∈ Dom(f)\n{SEP}")

# √(25-x²) - 1 ≥ 3  →  √(25-x²) ≥ 4  →  25-x² ≥ 16  →  x² ≤ 9
# Paso a: √(25-x²) ≥ 4
sym14_sq4 = solveset(sqrt(25 - x**2) >= 4, x, S.Reals)
chk("14.P2a — √(25-x²) ≥ 4 → x∈[-3,3]",
    sym14_sq4 == Interval(-3, 3),
    f"SymPy: {sym14_sq4}")

# Paso b: 25-x² ≥ 16  →  x² ≤ 9
sym14_x2 = solveset(x**2 <= 9, x, S.Reals)
chk("14.P2b — x² ≤ 9 → x∈[-3,3]",
    sym14_x2 == Interval(-3, 3),
    f"SymPy: {sym14_x2}")

# Verificación numérica: g(x) ≥ 3 iff x ∈ [-3,3]
with np.errstate(invalid='ignore'):
    gx14 = np.sqrt(np.where(25-PTS**2 >= 0, 25-PTS**2, np.nan)) - 1
mask_gx3  = np.isfinite(gx14) & (gx14 >= 3)
mask_tex14 = (PTS >= -3) & (PTS <= 3)
chk("14.P2c — g(x)≥3 ↔ x∈[-3,3] NumPy",
    abs(np.mean(mask_gx3 == mask_tex14)*100 - 100) < 1e-6)

# ── Paso 3: Intersección ─────────────────────────────────────
print(f"\n{SEP}\n  Paso 3: Dom(f∘g) = Dom(g) ∩ {{x | g(x)>=3}}\n{SEP}")

sym14_fog = sym14_domg & sym14_sq4
chk("14.P3a — Dom(f∘g) = [-5,5]∩[-3,3] = [-3,3]",
    sym14_fog == Interval(-3, 3),
    f"Intersección: {sym14_fog}")

# ── Paso 4: Fórmula (f∘g)(x) = √(√(25-x²)-4) ────────────────
print(f"\n{SEP}\n  Paso 4: Regla de asignación\n{SEP}")

x_chk14 = np.linspace(-3+1e-9, 3-1e-9, 200_000)
fog14_directo  = np.sqrt(np.sqrt(25 - x_chk14**2) - 1 - 3)
fog14_formula  = np.sqrt(np.sqrt(25 - x_chk14**2) - 4)
chk("14.P4a — (f∘g)(x) = √(√(25-x²)-4) NumPy",
    np.allclose(fog14_directo, fog14_formula, atol=1e-12))

# Verificación simbólica
fog14_sym = sqrt(sqrt(25 - x**2) - 1 - 3)
fog14_simplified = simplify(fog14_sym - sqrt(sqrt(25 - x**2) - 4))
chk("14.P4b — (f∘g)(x) = √(√(25-x²)-4) SymPy",
    fog14_simplified == 0,
    f"simplify = {fog14_simplified}")

# ── Paso 5: Valor en extremos ─────────────────────────────────
print(f"\n{SEP}\n  Paso 5: Verificación en extremos\n{SEP}")

fog14_at0 = float(sqrt(sqrt(25) - 4))
fog14_at3 = float(sqrt(sqrt(25 - 9) - 4))
chk("14.P5a — (f∘g)(0) = √(5-4) = 1",
    abs(fog14_at0 - 1.0) < 1e-9,
    f"(f∘g)(0) = √(√25-4) = √1 = {fog14_at0}")

chk("14.P5b — (f∘g)(±3) = 0 (extremos del dominio)",
    abs(fog14_at3) < 1e-9,
    f"(f∘g)(3) = √(√16-4) = √0 = {fog14_at3}")

# ══════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("  EJERCICIO 15 — f(x)=√(4/√(x+2)-1), g(x)=x+1")
print(f"{'='*60}")

# ── Paso 1: Dom(f) — condición 1: x > -2 ────────────────────
print(f"\n{SEP}\n  Paso 1: Dom(f) — condición radicando exterior\n{SEP}")

sym15_c1 = solveset(x + 2 > 0, x, S.Reals)
chk("15.P1a — x+2 > 0 → x > -2",
    sym15_c1 == Interval.open(-2, oo),
    f"SymPy: {sym15_c1}")

# ── Paso 2: Dom(f) — condición 2: 4/√(x+2) ≥ 1 ─────────────
print(f"\n{SEP}\n  Paso 2: Dom(f) — condición radicando interior ≥ 0\n{SEP}")

# 4/√(x+2) ≥ 1  →  √(x+2) ≤ 4  →  x+2 ≤ 16  →  x ≤ 14
sym15_c2 = solveset(4/sqrt(x+2) - 1 >= 0, x, S.Reals)
chk("15.P2a — 4/√(x+2) >= 1 → x <= 14 (incluye condicion x>-2)",
    sym15_c2 == Interval.Lopen(-2, 14) or sym15_c2 == Interval(-oo, 14),
    f"SymPy: {sym15_c2}  (el intersecto con x>-2 da (-2,14])")  

# Paso intermedio: √(x+2) ≤ 4 → x+2 ≤ 16
sym15_sq = solveset(sqrt(x+2) <= 4, x, S.Reals)
chk("15.P2b — √(x+2) <= 4 → x <= 14  (x+2 <= 16)",
    sym15_sq == Interval(-oo, 14) or sym15_sq == Interval(-2, 14),
    f"SymPy: {sym15_sq}")

# ── Paso 3: Dom(f) = (-2, 14] ────────────────────────────────
print(f"\n{SEP}\n  Paso 3: Intersección → Dom(f) = (-2,14]\n{SEP}")

sym15_dom = sym15_c1 & sym15_c2
chk("15.P3a — Dom(f) = (-2,14] SymPy",
    sym15_dom == Interval.Lopen(-2, 14),
    f"Intersección: {sym15_dom}")

with np.errstate(divide='ignore', invalid='ignore'):
    c1_15 = PTS + 2 > 0
    inner15 = 4/np.sqrt(np.abs(PTS+2)) - 1
    c2_15 = inner15 >= 0
mask_d15_orig = c1_15 & c2_15
mask_d15_tex  = (PTS > -2) & (PTS <= 14)
chk("15.P3b — Dom(f) = (-2,14] NumPy",
    abs(np.mean(mask_d15_orig == mask_d15_tex)*100 - 100) < 1e-6)

# ── Paso 4: f decreciente ────────────────────────────────────
print(f"\n{SEP}\n  Paso 4: f estrictamente decreciente\n{SEP}")

x_in15 = np.linspace(-2+1e-9, 14, 500_000)
f15n   = np.sqrt(4/np.sqrt(x_in15+2) - 1)
chk("15.P4a — f decreciente NumPy (Δf ≤ 0)",
    bool(np.all(np.diff(f15n) <= 1e-10)),
    f"max(Δf) = {np.diff(f15n).max():.2e}")

# Argumento de cadena: x↑ → x+2↑ → √(x+2)↑ → 4/√(x+2)↓ → f↓
# Verificar cada eslabón
chk("15.P4b — x+2 crec en (-2,14]",
    bool(np.all(np.diff(x_in15+2) > 0)))

chk("15.P4c — √(x+2) crec en (-2,14]",
    bool(np.all(np.diff(np.sqrt(x_in15+2)) > 0)))

chk("15.P4d — 4/√(x+2) decrec en (-2,14]",
    bool(np.all(np.diff(4/np.sqrt(x_in15+2)) < 0)))

# ── Paso 5: Rec(f) = [0,+∞) ─────────────────────────────────
print(f"\n{SEP}\n  Paso 5: Recorrido\n{SEP}")

f15_at14 = float(sqrt(4/sqrt(14+2) - 1))
chk("15.P5a — f(14) = 0 (mínimo)",
    abs(f15_at14) < 1e-9,
    f"f(14) = √(4/4-1) = √0 = {f15_at14:.6f}")

lim15 = limit(sqrt(4/sqrt(x+2) - 1), x, -2, '+')
chk("15.P5b — f(x)→+∞ cuando x→-2⁺",
    lim15 == oo,
    f"límite en -2⁺ = {lim15}")

chk("15.P5c — Rec=[0,+∞) NumPy",
    abs(f15n[-1]) < 1e-5 and f15n[0] > 10,
    f"f(14)≈{f15n[-1]:.6f}≈0, f(-2+)≈{f15n[0]:.2f}")

# ── Paso 6: Dom(f∘g), g(x) = x+1 ────────────────────────────
print(f"\n{SEP}\n  Paso 6: Composición f∘g con g(x)=x+1\n{SEP}")

# g(x) = x+1 debe estar en Dom(f) = (-2,14]
# x+1 > -2  →  x > -3
# x+1 ≤ 14  →  x ≤ 13
# g(x)=x+1 en Dom(f)=(-2,14]: x+1 > -2 → x > -3 ; x+1 <= 14 → x <= 13
sym15_a = solveset(x + 1 > -2, x, S.Reals)
sym15_b = solveset(x + 1 <= 14, x, S.Reals)
sym15_fog = sym15_a & sym15_b
chk("15.P6a — Dom(f∘g) = (-3,13] SymPy",
    sym15_fog == Interval.Lopen(-3, 13),
    f"SymPy: {sym15_fog}")

with np.errstate(divide='ignore', invalid='ignore'):
    c1_fg = PTS + 1 > -2
    c2_fg = PTS + 1 <= 14
mask_fg15_orig = c1_fg & c2_fg
mask_fg15_tex  = (PTS > -3) & (PTS <= 13)
chk("15.P6b — Dom(f∘g) = (-3,13] NumPy",
    abs(np.mean(mask_fg15_orig == mask_fg15_tex)*100 - 100) < 1e-6)

# ── Paso 7: Fórmula (f∘g)(x) = √(4/√(x+3)-1) ───────────────
print(f"\n{SEP}\n  Paso 7: Regla de asignación f∘g\n{SEP}")

x_chk15 = np.linspace(-3+1e-7, 13, 200_000)
fog15_directo = np.sqrt(4/np.sqrt(x_chk15+1+2) - 1)
fog15_formula = np.sqrt(4/np.sqrt(x_chk15+3) - 1)
chk("15.P7a — (f∘g)(x) = √(4/√(x+3)-1) NumPy",
    np.allclose(fog15_directo, fog15_formula, atol=1e-12))

fog15_sym = sqrt(4/sqrt((x+1)+2) - 1)
fog15_simp = simplify(fog15_sym - sqrt(4/sqrt(x+3) - 1))
chk("15.P7b — (f∘g)(x) = √(4/√(x+3)-1) SymPy",
    fog15_simp == 0,
    f"simplify = {fog15_simp}")

# ══════════════════════════════════════════════════════════════
total  = len(steps)
passed = sum(steps.values())
failed = [k for k, v in steps.items() if not v]

print(f"\n{'═'*60}")
print(f"  RESULTADO FINAL: {passed}/{total} PASS")
if failed:
    print(f"  ✗ FALLIDOS: {failed}")
else:
    print(f"  ✔ TODOS LOS PASOS VALIDADOS — listos para el PDF")
print(f"{'═'*60}")
