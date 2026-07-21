"""
VALIDACIÓN — Guía 4 - Trigonometría Aplicada — Cálculo I
Librerías usadas: SymPy + NumPy / Math
"""

import math
from sympy import *
import numpy as np

# -------------------------------------------------------------
PASS = "PASS"
FAIL = "FAIL"
results = {}

def val(tag, ok_lib1, ok_lib2, solucion, detalle=""):
    """Registra y muestra el resultado de un test."""
    ok = ok_lib1 and ok_lib2
    results[tag] = ok
    print(f"  {'PASS' if ok else 'FAIL'}  [Ej. {tag}]  -> {solucion}")
    if detalle:
        print(f"        val: {detalle}")

# -- Ejercicio 1: Altura del arbol ------------------------------
print("\n[Ej. 1] Altura de un arbol a 10 m con angulo de 30 grados")
# Lib 1 - SymPy
h_sympy = 10 * tan(pi/6)
ok_lib1 = (h_sympy == 10*sqrt(3)/3)

# Lib 2 - NumPy/Math
h_math = 10 * math.tan(math.radians(30))
ok_lib2 = np.allclose(float(h_sympy), h_math)

val("1", ok_lib1, ok_lib2, f"h = 10*sqrt(3)/3 ~ {h_math:.4f} m",
    f"Lib1={h_sympy}, Lib2={h_math:.6f}")

# -- Ejercicio 2: Altura del triangulo equilatero ---------------
print("\n[Ej. 2] Altura h_c de triangulo equilatero de lado 2")
# Lib 1 - SymPy
hc_sympy = 2 * sin(pi/3)
ok_lib1 = (hc_sympy == sqrt(3))

# Lib 2 - NumPy/Math
hc_math = 2 * math.sin(math.radians(60))
ok_lib2 = np.allclose(float(hc_sympy), hc_math)

val("2", ok_lib1, ok_lib2, f"hc = sqrt(3) ~ {hc_math:.4f}",
    f"Lib1={hc_sympy}, Lib2={hc_math:.6f}")

# -- Ejercicio 3: Altura del cerro ------------------------------
print("\n[Ej. 3] Altura h del cerro (dos mediciones: 45 y 30 grados separadas por 0.5 km)")
# h = x * tan(45) = x
# h = (x + 0.5) * tan(30) => h = (h + 0.5) * tan(30)
# h * (1 - tan(30)) = 0.5 * tan(30)
# h = 0.5 * tan(30) / (1 - tan(30))

# Lib 1 - SymPy
h_var = symbols('h', real=True)
sol_sympy = solve(Eq(tan(pi/6), h_var / (h_var + S(1)/2)), h_var)[0]
ok_lib1 = (sol_sympy == (sqrt(3) + 1)/4)

# Lib 2 - NumPy/Math
tan30 = math.tan(math.radians(30))
h_cerro_math = 0.5 * tan30 / (1.0 - tan30)
ok_lib2 = np.allclose(float(sol_sympy), h_cerro_math)

val("3", ok_lib1, ok_lib2, f"h = (sqrt(3)+1)/4 km = 250*(sqrt(3)+1) m ~ {h_cerro_math*1000:.2f} m",
    f"Lib1={sol_sympy} km, Lib2={h_cerro_math:.6f} km")

# -- Ejercicio 4: Longitud del corte diagonal -------------------
print("\n[Ej. 4] Longitud del corte diagonal y (vertical 3 in, inclinacion 30 grados)")
# y * cos(30) = 3 => y = 3 / cos(30)

# Lib 1 - SymPy
y_var = symbols('y', real=True)
sol_y_sympy = solve(Eq(cos(pi/6), 3 / y_var), y_var)[0]
ok_lib1 = (sol_y_sympy == 2*sqrt(3))

# Lib 2 - NumPy/Math
y_math = 3.0 / math.cos(math.radians(30))
ok_lib2 = np.allclose(float(sol_y_sympy), y_math)

val("4", ok_lib1, ok_lib2, f"y = 2*sqrt(3) in ~ {y_math:.4f} in",
    f"Lib1={sol_y_sympy}, Lib2={y_math:.6f}")

# Muestreo de angulos para identidades (evitando divisiones por cero en tan/cot)
rng = np.random.default_rng(0)
test_angles = rng.uniform(-10, 10, 1000)
valid_angles = test_angles[np.abs(np.sin(2 * test_angles)) > 1e-4]

# -- Ejercicio 5: Identidad a -----------------------------------
print("\n[Ej. 5] Identidad: tan(theta)*cot(theta) - cos^2(theta) = sin^2(theta)")
theta = symbols('theta', real=True)
lhs_sympy_5 = tan(theta) * cot(theta) - cos(theta)**2
rhs_sympy_5 = sin(theta)**2

# Lib 1 - SymPy
ok_lib1 = (simplify(lhs_sympy_5 - rhs_sympy_5) == 0)

# Lib 2 - NumPy
lhs_np_5 = np.tan(valid_angles) * (1.0 / np.tan(valid_angles)) - np.cos(valid_angles)**2
rhs_np_5 = np.sin(valid_angles)**2
ok_lib2 = np.allclose(lhs_np_5, rhs_np_5)

val("5", ok_lib1, ok_lib2, "tan(theta)*cot(theta) - cos^2(theta) = sin^2(theta) [Identidad Confirmada]",
    f"SymPy simplificado = {simplify(lhs_sympy_5 - rhs_sympy_5)}, NumPy max_diff = {np.max(np.abs(lhs_np_5 - rhs_np_5)):.2e}")

# -- Ejercicio 6: Identidad b -----------------------------------
print("\n[Ej. 6] Identidad: sin(theta)*(cot(theta) + tan(theta)) = sec(theta)")
lhs_sympy_6 = sin(theta) * (cot(theta) + tan(theta))
rhs_sympy_6 = sec(theta)

# Lib 1 - SymPy
ok_lib1 = (simplify(lhs_sympy_6 - rhs_sympy_6) == 0)

# Lib 2 - NumPy
lhs_np_6 = np.sin(valid_angles) * (1.0 / np.tan(valid_angles) + np.tan(valid_angles))
rhs_np_6 = 1.0 / np.cos(valid_angles)
ok_lib2 = np.allclose(lhs_np_6, rhs_np_6)

val("6", ok_lib1, ok_lib2, "sin(theta)*(cot(theta) + tan(theta)) = sec(theta) [Identidad Confirmada]",
    f"SymPy simplificado = {simplify(lhs_sympy_6 - rhs_sympy_6)}, NumPy max_diff = {np.max(np.abs(lhs_np_6 - rhs_np_6)):.2e}")

# -- Resumen final ----------------------------------------------
total  = len(results)
passed = sum(results.values())
print(f"\n{'='*50}")
print(f"  RESULTADO: {passed}/{total} PASS")
failed = [k for k, v in results.items() if not v]
if failed:
    print(f"  FAIL: {failed}")
else:
    print(f"  ALL PASS - listos para el solucionario")
print(f"{'='*50}")
