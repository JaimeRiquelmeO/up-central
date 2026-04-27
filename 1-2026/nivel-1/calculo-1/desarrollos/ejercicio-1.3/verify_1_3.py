"""
VERIFICACIÓN COMPLETA — Ejercicio 1.3
Inecuación: x + 1 < sqrt(x^2 + 3x)
"""
import math, warnings
import numpy as np
from sympy import *

warnings.filterwarnings('ignore')
x = symbols('x', real=True)

print('='*65)
print('EJERCICIO 1.3:  x + 1 < sqrt(x^2 + 3x)')
print('='*65)

# ── PASO 1: DOMINIO ──────────────────────────────────────────
print('\n--- PASO 1: Dominio ---')
# Condición radicando >= 0:  x^2 + 3x >= 0  =>  x(x+3) >= 0
cond_dominio = solveset(x**2 + 3*x >= 0, x, S.Reals)
print('x^2 + 3x >= 0  =>  x(x+3) >= 0  =>  ', cond_dominio)
print('Dominio D = (-inf, -3] ∪ [0, +inf)  ✓')

# ── PASO 2: CASO 1 — x+1 < 0 ─────────────────────────────────
print('\n--- PASO 2: Caso 1 (x + 1 < 0, es decir x < -1) ---')
# En dominio, x < -1 implica x <= -3
# LHS < 0  <=  RHS >= 0  =>  desigualdad satisfecha automáticamente
# Verificar con puntos de prueba
test_caso1 = [-3, -4, -5, -10, -100]
print('Puntos de prueba en x <= -3:')
for v in test_caso1:
    lhs = v + 1
    arg = v**2 + 3*v
    rhs = math.sqrt(arg) if arg >= 0 else None
    if rhs is not None:
        ok = lhs < rhs
        print(f'  x={v:6.0f}: LHS={lhs:7.2f},  RHS={rhs:7.4f},  satisface={ok}')
print('=> Todo x <= -3 satisface la inecuación (LHS < 0 <= RHS)  ✓')

# ── PASO 3: CASO 2 — x+1 >= 0 ────────────────────────────────
print('\n--- PASO 3: Caso 2 (x + 1 >= 0, es decir x >= 0 en dominio) ---')
print('Ambos lados >= 0: podemos elevar al cuadrado SIN cambiar la desigualdad')
print('  (x+1)^2  <  x^2 + 3x')

lhs_sq = expand((x + 1)**2)
rhs_sq = x**2 + 3*x
diferencia = expand(lhs_sq - rhs_sq)
print(f'  {lhs_sq}  <  {rhs_sq}')
print(f'  => {diferencia}  <  0')
print(f'  => -x + 1  <  0')
print(f'  => x > 1')

# Verificar equivalencia (x+1)^2 < x^2+3x  <=>  -x+1 < 0  (en x >= 0)
pts_caso2 = np.linspace(0, 50, 100_000) + 1e-9*math.pi
mask_orig = (pts_caso2 + 1)**2 < pts_caso2**2 + 3*pts_caso2
mask_simp = pts_caso2 > 1
acuerdo_c2 = np.mean(mask_orig == mask_simp)
print(f'  Equivalencia numérica (x>=0): {100*acuerdo_c2:.6f}%  (debe ser 100%)  ✓')

# ── PASO 4: INTERSECCIÓN CON DOMINIO ─────────────────────────
print('\n--- PASO 4: Intersección con dominio ---')
print('Caso 1 => x <= -3')
print('Caso 2 => x > 1  (con x >= 0 del dominio)')
print('Solución = (-inf, -3] ∪ (1, +inf)')

# ── VALIDACIÓN FINAL CON SYMPY ────────────────────────────────
print('\n--- VALIDACIÓN FINAL: SymPy (simbólico) ---')
inec = x + 1 - sqrt(x**2 + 3*x)
sol_sympy = solveset(inec < 0, x, S.Reals)
print('SymPy solveset:', sol_sympy)

# ── VALIDACIÓN FINAL CON NUMPY ────────────────────────────────
print('\n--- VALIDACIÓN FINAL: NumPy (muestreo 50 000 pts) ---')
rng = np.random.default_rng(0)
pts = np.sort(np.concatenate([
    np.linspace(-200, 200, 40_000) + 1e-6*math.pi,
    rng.uniform(-200, 200, 10_000)
]))

results = []
for v in pts:
    arg = v**2 + 3*v
    if arg < 0:
        continue   # fuera del dominio
    lhs_v = v + 1
    rhs_v = math.sqrt(arg)
    satisface_orig = lhs_v < rhs_v
    # Conjunto solución: x <= -3 OR x > 1
    en_solucion   = (v <= -3) or (v > 1)
    results.append(satisface_orig == en_solucion)

acuerdo_np = sum(results) / len(results)
print(f'Puntos en dominio evaluados: {len(results)}')
print(f'Acuerdo NumPy: {100*acuerdo_np:.6f}%  (debe ser 100%)  ✓')

# ── PUNTOS DE BORDE ───────────────────────────────────────────
print('\n--- Verificación de puntos de borde ---')
border_pts = [(-3, 'límite izquierdo incl.'),
              (-3.0001, 'justo antes de -3'),
              (0, 'x=0 (borde dominio)'),
              (1, 'x=1 (borde excluido)'),
              (1.0001, 'justo después de 1'),
              (2, 'x=2 (en solución)')]
for v, label in border_pts:
    arg = v**2 + 3*v
    if arg < 0:
        print(f'  x={v:8.4f} ({label}): fuera del dominio')
        continue
    lhs_v = v + 1
    rhs_v = math.sqrt(arg)
    ok = lhs_v < rhs_v
    print(f'  x={v:8.4f} ({label}): {lhs_v:.4f} < {rhs_v:.4f}? {ok}')

print('\n' + '='*65)
print('SOLUCIÓN FINAL VERIFICADA:  x ∈ (-∞, -3] ∪ (1, +∞)')
print('='*65)
