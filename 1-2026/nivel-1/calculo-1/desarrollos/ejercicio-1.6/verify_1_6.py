from sympy import *
import numpy as np, math

x = symbols('x', real=True)

print("=" * 60)
print("EJERCICIO 1.6 — sqrt(x^2 - 1) / (x - 2) > 0")
print("=" * 60)

# ── PASO 1: Dominio ─────────────────────────────────────────
print("\n--- PASO 1: Dominio ---")
dom_raiz = solveset(x**2 - 1 >= 0, x, S.Reals)
print("  x^2 - 1 >= 0:", dom_raiz)
print("  x != 2  (denominador no nulo)")
print("  Dominio: (-inf,-1] U [1,2) U (2,+inf)")

# ── PASO 2: Ceros del numerador ────────────────────────────
print("\n--- PASO 2: Ceros del numerador sqrt(x^2-1) ---")
raices_num = solveset(x**2 - 1, x, S.Reals)
print("  x^2 - 1 = 0 =>", raices_num)
print("  En x = +-1 la fraccion vale 0  (NO cumple estricto > 0)")

# ── PASO 3: Condicion para fraccion > 0 ───────────────────
print("\n--- PASO 3: Condicion fraccion > 0 ---")
sol_num_pos = solveset(x**2 - 1 > 0, x, S.Reals)
print("  Numerador > 0 (x^2-1 > 0):", sol_num_pos)
print("  Denominador > 0: x > 2")
print("  Interseccion: x > 2  =>  (2, +inf)")

# ── RESULTADO FINAL: SymPy (simbolico) ────────────────────
print("\n--- RESULTADO: Libreria 1 — SymPy ---")
expr = sqrt(x**2 - 1) / (x - 2)
sol_sympy = solveset(expr > 0, x, S.Reals)
print("  SymPy solucion:", sol_sympy)

# ── RESULTADO FINAL: NumPy (muestreo) ─────────────────────
print("\n--- RESULTADO: Libreria 2 — NumPy ---")
rng = np.random.default_rng(0)
pts = np.sort(np.concatenate([
    np.linspace(-20, 20, 40_000) + 1e-6 * math.pi,
    rng.uniform(-20, 20, 10_000)
]))

# Solo puntos en dominio: x^2-1 >= 0 AND x != 2
in_domain = (pts**2 - 1 >= 0) & (np.abs(pts - 2) > 1e-9)
dom_pts = pts[in_domain]

numerador  = np.sqrt(dom_pts**2 - 1)
denominador = dom_pts - 2
fraccion   = numerador / denominador

mask_ineq = fraccion > 0   # inecuacion original en dominio
mask_sol  = dom_pts > 2    # solucion esperada

acuerdo = np.mean(mask_ineq == mask_sol)
print(f"  Puntos evaluados en dominio: {len(dom_pts)}")
print(f"  Acuerdo NumPy: {100*acuerdo:.6f}%")

# Verificacion puntual
print("\n--- Verificacion puntual ---")
for val in [-3.0, -1.0, 1.0, 1.5, 2.5, 3.0, 5.0]:
    if val**2 - 1 >= 0 and abs(val - 2) > 1e-9:
        num_v = math.sqrt(val**2 - 1)
        den_v = val - 2
        frac_v = num_v / den_v
        ok = "✓ > 0" if frac_v > 0 else "✗ <= 0"
        print(f"  x = {val:+5.1f}:  frac = {frac_v:+.4f}   {ok}")
    else:
        print(f"  x = {val:+5.1f}:  fuera de dominio")

print("\n=> Conjunto solucion: x in (2, +inf)")
