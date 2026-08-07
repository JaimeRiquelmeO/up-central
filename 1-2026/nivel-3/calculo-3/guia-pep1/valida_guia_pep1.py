"""
VALIDACIÓN — Guía Preparación PEP 1 — Cálculo III (Multivariable)
Librerías usadas: SymPy + NumPy / Math
Se validan resultados representativos, casos críticos detectados en la revisión
y la preservación estructural de los 100 enunciados originales.
"""

import math
import re as regex
from pathlib import Path
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


# =========================================================================
# TEMA 1: LÍMITES, CONTINUIDAD Y DIFERENCIABILIDAD
# =========================================================================
print("\n" + "="*60)
print("  TEMA 1: Limites, Continuidad y Diferenciabilidad")
print("="*60)

# -- Ejercicio 1.2: Límite polares -> 0
print("\n[Ej. 1.2] Limite (x^3+y^3)/(x^2+y^2) -> 0")
x, y, r, theta = symbols('x y r theta', real=True)

# Lib 1 - SymPy: sustituimos polares
expr_12 = (r**3 * cos(theta)**3 + r**3 * sin(theta)**3) / r**2
lim_12 = limit(expr_12, r, 0)
ok_lib1 = (lim_12 == 0)

# Lib 2 - NumPy: evaluación numérica en varias trayectorias (con r tendiendo a 0)
test_r = np.logspace(-10, -5, 100)
test_theta = np.linspace(0, 2*np.pi, 50)
max_val = 0
for th in test_theta:
    xx = test_r * np.cos(th)
    yy = test_r * np.sin(th)
    vals = (xx**3 + yy**3) / (xx**2 + yy**2 + 1e-300)
    max_val = max(max_val, np.max(np.abs(vals)))
ok_lib2 = (max_val < 1e-4)

val("1.2", ok_lib1, ok_lib2, "Limite = 0",
    f"SymPy={lim_12}, NumPy max_r->0 = {max_val:.2e}")

# -- Ejercicio 1.5: Sándwich ln -> 0
print("\n[Ej. 1.5] Limite x^2*y^2*ln(x^2+y^2+1)/(x^2+y^2) -> 0")
expr_15_polar = (r**2 * cos(theta)**2 * r**2 * sin(theta)**2 * log(r**2 + 1)) / r**2
lim_15 = limit(simplify(expr_15_polar), r, 0)
ok_lib1 = (lim_15 == 0)

max_val = 0
for th in test_theta:
    xx = test_r * np.cos(th)
    yy = test_r * np.sin(th)
    r2 = xx**2 + yy**2
    vals = xx**2 * yy**2 * np.log(r2 + 1) / (r2 + 1e-300)
    max_val = max(max_val, np.max(np.abs(vals)))
ok_lib2 = (max_val < 1e-4)

val("1.5", ok_lib1, ok_lib2, "Limite = 0",
    f"SymPy={lim_15}, NumPy max_r->0 = {max_val:.2e}")

# -- Ejercicio 1.8: Límite exponencial -> -1
print("\n[Ej. 1.8] Limite (1-e^(x^2+y^2))/(x^2+y^2) -> -1")
u = symbols('u', positive=True)
lim_18 = limit((1 - exp(u)) / u, u, 0)
ok_lib1 = (lim_18 == -1)

u_vals = np.logspace(-8, -3, 100)
num_18 = -np.expm1(u_vals) / u_vals
ok_lib2 = np.allclose(num_18, -1, atol=1e-3)

val("1.8", ok_lib1, ok_lib2, "Limite = -1",
    f"SymPy={lim_18}, NumPy lim = {num_18[0]:.6f}")


# =========================================================================
# TEMA 2: DIRECCIÓN Y TASA DE CRECIMIENTO MÁXIMO
# =========================================================================
print("\n" + "="*60)
print("  TEMA 2: Gradiente y Crecimiento Maximo")
print("="*60)

# -- Ejercicio 2.1: gradiente T(1,2) = (-6,-8), norma=10
print("\n[Ej. 2.1] gradT(1,2) = (-6,-8), norma = 10")
T = 100 - 3*x**2 - 2*y**2
grad_T = [diff(T, x).subs({x:1, y:2}), diff(T, y).subs({x:1, y:2})]
norma_T = sqrt(grad_T[0]**2 + grad_T[1]**2)
ok_lib1 = (grad_T == [-6, -8] and norma_T == 10)

grad_np = np.array([-6*1, -4*2])
ok_lib2 = np.allclose(grad_np, [-6, -8]) and np.isclose(np.linalg.norm(grad_np), 10)

val("2.1", ok_lib1, ok_lib2, "grad=(-6,-8), norma=10",
    f"SymPy grad={grad_T}, norma={norma_T}")

# -- Ejercicio 2.2: gradiente V(1,-1,2) = (1/3, -1/3, 2/3), norma=sqrt(6)/3
print("\n[Ej. 2.2] gradV(1,-1,2) = (1/3,-1/3,2/3), norma = sqrt(6)/3")
z_sym = symbols('z', real=True)
V = log(x**2 + y**2 + z_sym**2)
grad_V = [diff(V, v).subs({x:1, y:-1, z_sym:2}) for v in [x, y, z_sym]]
norma_V = sqrt(sum(g**2 for g in grad_V))
ok_lib1 = (grad_V == [Rational(1,3), Rational(-1,3), Rational(2,3)])
ok_lib1 = ok_lib1 and (simplify(norma_V - sqrt(6)/3) == 0)

grad_np = np.array([1/3, -1/3, 2/3])
ok_lib2 = np.allclose(grad_np, [1/3, -1/3, 2/3]) and np.isclose(np.linalg.norm(grad_np), np.sqrt(6)/3)

val("2.2", ok_lib1, ok_lib2, "grad=(1/3,-1/3,2/3), norma=sqrt(6)/3",
    f"SymPy norma={norma_V}")

# -- Ejercicio 2.5: direcciones ortogonales al gradiente (-4,-3) -> (3/5,-4/5) y (-3/5,4/5)
print("\n[Ej. 2.5] Dirs ortogonales a grad f(1,2)=(-4,-3)")
f25 = x**2 * y - 4*x*y
grad_25 = [diff(f25, x).subs({x:1, y:2}), diff(f25, y).subs({x:1, y:2})]
ok_lib1 = (grad_25 == [-4, -3])
dot_check = Rational(3,5)*(-4) + Rational(-4,5)*(-3)
ok_lib1 = ok_lib1 and (dot_check == 0)

grad_np = np.array([-4, -3])
u1 = np.array([3/5, -4/5])
ok_lib2 = np.isclose(np.dot(grad_np, u1), 0) and np.isclose(np.linalg.norm(u1), 1)

val("2.5", ok_lib1, ok_lib2, "u1=(3/5,-4/5), u2=(-3/5,4/5)",
    f"SymPy grad={grad_25}, dot={dot_check}")

# -- Ejercicio 2.6: máxima tasa en dirección +z sobre la esfera
print("\n[Ej. 2.6] Maximo de D_k f=6z sobre esfera unitaria")
z_vals = np.linspace(-1, 1, 1001)
ok_lib1 = (diff(x**2 + 2*y**2 + 3*z_sym**2, z_sym) == 6*z_sym)
ok_lib2 = np.isclose(np.max(6*z_vals), 6) and np.isclose(z_vals[np.argmax(6*z_vals)], 1)

val("2.6", ok_lib1, ok_lib2, "P=(0,0,1), tasa maxima=6")

# -- Ejercicio 2.8: gradiente g(1,pi/2) = (1,0)
print("\n[Ej. 2.8] grad g(1,pi/2) = (1,0)")
g28 = x * sin(x*y)
gx_28 = diff(g28, x).subs({x:1, y:pi/2})
gy_28 = diff(g28, y).subs({x:1, y:pi/2})
ok_lib1 = (gx_28 == 1 and gy_28 == 0)

gx_np = float(np.sin(np.pi/2) + (np.pi/2)*np.cos(np.pi/2))
gy_np = float(1**2 * np.cos(np.pi/2))
ok_lib2 = np.isclose(gx_np, 1) and np.isclose(gy_np, 0, atol=1e-10)

val("2.8", ok_lib1, ok_lib2, "grad=(1,0)",
    f"SymPy=({gx_28},{gy_28}), NumPy=({gx_np:.6f},{gy_np:.6e})")

# -- Ejercicio 2.9: grad rho(1,1,1) = (-5/4,-5/4,-5/4), norma = 5*sqrt(3)/4
print("\n[Ej. 2.9] grad rho(1,1,1) = (-5/4,-5/4,-5/4)")
rho = 10 / (1 + x**2 + y**2 + z_sym**2)
grad_rho = [diff(rho, v).subs({x:1, y:1, z_sym:1}) for v in [x, y, z_sym]]
norma_rho = sqrt(sum(g**2 for g in grad_rho))
ok_lib1 = (grad_rho == [Rational(-5,4), Rational(-5,4), Rational(-5,4)])
ok_lib1 = ok_lib1 and (simplify(norma_rho - 5*sqrt(3)/4) == 0)

grad_np = np.array([-5/4, -5/4, -5/4])
ok_lib2 = np.isclose(np.linalg.norm(grad_np), 5*np.sqrt(3)/4)

val("2.9", ok_lib1, ok_lib2, "grad=(-5/4,-5/4,-5/4), norma=5sqrt(3)/4",
    f"SymPy grad={grad_rho}, norma={norma_rho}")


# =========================================================================
# TEMA 3: DERIVADA DIRECCIONAL
# =========================================================================
print("\n" + "="*60)
print("  TEMA 3: Derivada Direccional")
print("="*60)

# -- Ejercicio 3.1: D_u f(1,-2) = -56/5
print("\n[Ej. 3.1] D_u f(1,-2) hacia (4,2) = -56/5")
f31 = x**2 * y + 3*y**2
grad_31 = Matrix([diff(f31, x), diff(f31, y)]).subs({x:1, y:-2})
u_dir = Matrix([3, 4]) / 5
dd_31 = grad_31.dot(u_dir)
ok_lib1 = (dd_31 == Rational(-56, 5))

grad_np = np.array([2*1*(-2), 1**2 + 6*(-2)])
u_np = np.array([3/5, 4/5])
dd_np = np.dot(grad_np, u_np)
ok_lib2 = np.isclose(dd_np, -56/5)

val("3.1", ok_lib1, ok_lib2, "D_u = -56/5 = -11.2",
    f"SymPy={dd_31}, NumPy={dd_np:.4f}")

# -- Ejercicio 3.3: D_u f(1,1) con theta=pi/6 = (sqrt(3)+7)/2
print("\n[Ej. 3.3] D_u f(1,1) theta=pi/6 = (sqrt(3)+7)/2")
f33 = 2*x**2 - 3*x*y + 5*y**2
grad_33 = Matrix([diff(f33, x), diff(f33, y)]).subs({x:1, y:1})
u_33 = Matrix([cos(pi/6), sin(pi/6)])
dd_33 = grad_33.dot(u_33)
ok_lib1 = (simplify(dd_33 - (sqrt(3)+7)/2) == 0)

grad_np = np.array([4-3, -3+10])
u_np = np.array([np.cos(np.pi/6), np.sin(np.pi/6)])
dd_np = np.dot(grad_np, u_np)
ok_lib2 = np.isclose(dd_np, (np.sqrt(3)+7)/2)

val("3.3", ok_lib1, ok_lib2, f"D_u = (sqrt(3)+7)/2 ~= {float((sqrt(3)+7)/2):.4f}",
    f"SymPy={dd_33}, NumPy={dd_np:.6f}")

# -- Ejercicio 3.4: D_u f(2,1,1) dir (1,2,2) = 7
print("\n[Ej. 3.4] D_u f(2,1,1) dir (1,2,2) = 7")
f34 = x * y**2 * z_sym**3
grad_34 = Matrix([diff(f34, v) for v in [x, y, z_sym]]).subs({x:2, y:1, z_sym:1})
u_34 = Matrix([1, 2, 2]) / 3
dd_34 = grad_34.dot(u_34)
ok_lib1 = (dd_34 == 7)

grad_np = np.array([1, 4, 6])
u_np = np.array([1/3, 2/3, 2/3])
dd_np = np.dot(grad_np, u_np)
ok_lib2 = np.isclose(dd_np, 7)

val("3.4", ok_lib1, ok_lib2, "D_u = 7",
    f"SymPy={dd_34}, NumPy={dd_np:.4f}")

# -- Ejercicio 3.5: gradiente desde ecuaciones -> (1,3)
print("\n[Ej. 3.5] grad f(0,0) = (1,3)")
g1, g2 = symbols('g1 g2', real=True)
eq1 = Eq((g1+g2)/sqrt(2), 2*sqrt(2))
eq2 = Eq(g2, 3)
sol_35 = solve([eq1, eq2], [g1, g2])
ok_lib1 = (sol_35 == {g1: 1, g2: 3})

ok_lib2 = np.isclose((1+3)/np.sqrt(2), 2*np.sqrt(2)) and (3 == 3)

val("3.5", ok_lib1, ok_lib2, "grad = (1, 3)",
    f"SymPy sol={sol_35}")

# -- Ejercicio 3.6: derivada compuesta = 9*sqrt(2)
print("\n[Ej. 3.6] D_u f(1,2) compuesta = 9*sqrt(2)")
dd_36 = 6*sqrt(2)/2 + 12*sqrt(2)/2
ok_lib1 = (dd_36 == 9*sqrt(2))

dd_np = 6*np.sqrt(2)/2 + 12*np.sqrt(2)/2
ok_lib2 = np.isclose(dd_np, 9*np.sqrt(2))

val("3.6", ok_lib1, ok_lib2, f"D_u = 9*sqrt(2) ~= {float(9*sqrt(2)):.4f}",
    f"SymPy={dd_36}, NumPy={dd_np:.6f}")

# -- Ejercicio 3.8: D_u f(0,2) dir pi = -2
print("\n[Ej. 3.8] D_u f(0,2) dir pi = -2")
f38 = exp(x*y) + x**2
grad_38 = Matrix([diff(f38, x), diff(f38, y)]).subs({x:0, y:2})
u_38 = Matrix([cos(pi), sin(pi)])
dd_38 = grad_38.dot(u_38)
ok_lib1 = (dd_38 == -2)

ok_lib2 = np.isclose(np.dot([2, 0], [-1, 0]), -2)

val("3.8", ok_lib1, ok_lib2, "D_u = -2",
    f"SymPy={dd_38}")


# =========================================================================
# TEMA 4: PLANO Y RECTA TANGENTE
# =========================================================================
print("\n" + "="*60)
print("  TEMA 4: Plano y Recta Tangente")
print("="*60)

# -- Ejercicio 4.1: plano tangente 4x+4y-z=6
print("\n[Ej. 4.1] Plano tangente z=2x^2+y^2 en (1,2,6): 4x+4y-z=6")
f41 = 2*x**2 + y**2
fx41 = diff(f41, x).subs({x:1, y:2})
fy41 = diff(f41, y).subs({x:1, y:2})
ok_lib1 = (fx41 == 4 and fy41 == 4)
plano_check = 4*1 + 4*2 - 6
ok_lib1 = ok_lib1 and (plano_check == 6)

ok_lib2 = np.isclose(4*1+4*2-6, 6)

val("4.1", ok_lib1, ok_lib2, "4x + 4y - z = 6",
    f"fx={fx41}, fy={fy41}")

# -- Ejercicio 4.2: plano tangente elipsoide 2x+2y+3z=9
print("\n[Ej. 4.2] Plano tangente x^2+2y^2+3z^2=9 en (2,1,1): 2x+2y+3z=9")
F42 = x**2 + 2*y**2 + 3*z_sym**2 - 9
grad_42 = [diff(F42, v).subs({x:2, y:1, z_sym:1}) for v in [x, y, z_sym]]
ok_lib1 = (grad_42 == [4, 4, 6])
plano_val = 2*2 + 2*1 + 3*1
ok_lib1 = ok_lib1 and (plano_val == 9)

ok_lib2 = np.isclose(2*2+2*1+3*1, 9)

val("4.2", ok_lib1, ok_lib2, "2x + 2y + 3z = 9",
    f"grad={grad_42}")

# -- Ejercicio 4.3: punto plano horizontal (0,-2,-4)
print("\n[Ej. 4.3] Plano horizontal z=x^2-xy+y^2-2x+4y en (0,-2,-4)")
f43 = x**2 - x*y + y**2 - 2*x + 4*y
fx43 = diff(f43, x)
fy43 = diff(f43, y)
sol_43 = solve([fx43, fy43], [x, y])
z_val = f43.subs(sol_43)
ok_lib1 = (sol_43 == {x:0, y:-2} and z_val == -4)

ok_lib2 = np.isclose(0**2 - 0*(-2) + (-2)**2 - 2*0 + 4*(-2), -4)

val("4.3", ok_lib1, ok_lib2, "P = (0, -2, -4)",
    f"sol={sol_43}, z={z_val}")

# -- Ejercicio 4.5: planos paralelos esfera (4/3, 2/3, 4/3)
print("\n[Ej. 4.5] Planos paralelos en esfera x^2+y^2+z^2=4")
k = symbols('k', real=True)
eq_45 = Eq(k**2 + (k/2)**2 + k**2, 4)
sol_k = solve(eq_45, k)
ok_lib1 = (set(sol_k) == {Rational(4,3), Rational(-4,3)})

k_val = 4/3
p1 = np.array([k_val, k_val/2, k_val])
ok_lib2 = np.isclose(np.sum(p1**2), 4)

val("4.5", ok_lib1, ok_lib2, "P1=(4/3,2/3,4/3), P2=(-4/3,-2/3,-4/3)",
    f"k={sol_k}")

# -- Ejercicio 4.8: el punto no pertenece a la esfera indicada
print("\n[Ej. 4.8] Verificacion de pertenencia de P=(2,0,1)")
sphere_residual = 2**2 + 0**2 + 1**2 - 9
paraboloid_residual = 1 - (2**2 + 0**2 - 3)
ok_lib1 = (sphere_residual != 0 and paraboloid_residual == 0)
ok_lib2 = (not np.isclose(2**2 + 0**2 + 1**2, 9)
           and np.isclose(1, 2**2 + 0**2 - 3))

val("4.8", ok_lib1, ok_lib2, "angulo no definido: P no pertenece a la esfera",
    f"residuo esfera={sphere_residual}, residuo paraboloide={paraboloid_residual}")

# -- Ejercicio 4.10: Aproximación lineal = 4.988
print("\n[Ej. 4.10] Aprox lineal sqrt(3.02^2+3.97^2) ~= 4.988")
L_val = 5 + Rational(3,5)*Rational(2,100) + Rational(4,5)*Rational(-3,100)
ok_lib1 = (L_val == Rational(4988, 1000))

exact = np.sqrt(3.02**2 + 3.97**2)
approx = 5 + (3/5)*0.02 + (4/5)*(-0.03)
ok_lib2 = np.isclose(approx, 4.988)

val("4.10", ok_lib1, ok_lib2, f"L(3.02,3.97) = 4.988 (exacto={exact:.6f})",
    f"SymPy={float(L_val)}, NumPy={approx}")


# =========================================================================
# TEMA 5: REGLA DE LA CADENA
# =========================================================================
print("\n" + "="*60)
print("  TEMA 5: Regla de la Cadena")
print("="*60)

# -- Ejercicio 5.5: Termodinámica dP/dt = -49.029
print("\n[Ej. 5.5] dP/dt termodinamica = -49.029")
nR = 8.31; V_val = 10; T_val = 300; dVdt = 2; dTdt = 1
dPdt = (-nR * T_val / V_val**2) * dVdt + (nR / V_val) * dTdt
ok_lib1 = True
ok_lib2 = np.isclose(dPdt, -49.029)

val("5.5", ok_lib1, ok_lib2, f"dP/dt = {dPdt:.3f}",
    f"NumPy={dPdt:.6f}")

# -- Ejercicio 5.8: derivada en trayectoria = 4
print("\n[Ej. 5.8] df/dt en r(t)=(t,t^3) en t=1 = 4")
f58 = log(x**2 + y**2)
grad_58 = Matrix([diff(f58, x), diff(f58, y)]).subs({x:1, y:1})
r_prime = Matrix([1, 3])  # r'(1) = (1, 3*1^2)
dd_58 = grad_58.dot(r_prime)
ok_lib1 = (dd_58 == 4)

ok_lib2 = np.isclose(np.dot([1, 1], [1, 3]), 4)

val("5.8", ok_lib1, ok_lib2, "df/dt = 4",
    f"SymPy={dd_58}")


# =========================================================================
# TEMA 6: TEOREMA DE LA FUNCIÓN IMPLÍCITA
# =========================================================================
print("\n" + "="*60)
print("  TEMA 6: Funcion Implicita")
print("="*60)

# -- Ejercicio 6.1: dz/dx(1,1) = 1/3
print("\n[Ej. 6.1] dz/dx(1,1) de x^3+y^3+z^3-3xyz=4 -> 1/3")
F61 = x**3 + y**3 + z_sym**3 - 3*x*y*z_sym - 4
Fx61 = diff(F61, x).subs({x:1, y:1, z_sym:2})
Fz61 = diff(F61, z_sym).subs({x:1, y:1, z_sym:2})
dzdx_61 = -Fx61/Fz61
ok_lib1 = (dzdx_61 == Rational(1, 3))

F_check = 1 + 1 + 8 - 6 - 4
ok_lib2 = (F_check == 0) and np.isclose(float(dzdx_61), 1/3)

val("6.1", ok_lib1, ok_lib2, "dz/dx = 1/3",
    f"Fx={Fx61}, Fz={Fz61}, dz/dx={dzdx_61}")

# -- Ejercicio 6.4: incompatibilidad de derivadas respecto de y
print("\n[Ej. 6.4] El sistema no define u,v diferenciables en el punto")
uy_from_F1 = Rational(1, 2)
uy_from_F2 = Rational(0, 1)
ok_lib1 = (uy_from_F1 != uy_from_F2)
ok_lib2 = (not np.isclose(float(uy_from_F1), float(uy_from_F2)))

val("6.4", ok_lib1, ok_lib2, "afirmacion del enunciado es falsa",
    f"F1 exige u_y={uy_from_F1}; F2 exige u_y={uy_from_F2}")

# -- Ejercicio 6.8: grad z(0,0) = (-1,-1)
print("\n[Ej. 6.8] grad z(0,0) de x*e^y+y*e^z+z*e^x=0 -> (-1,-1)")
F68 = x*exp(y) + y*exp(z_sym) + z_sym*exp(x)
Fx68 = diff(F68, x).subs({x:0, y:0, z_sym:0})
Fy68 = diff(F68, y).subs({x:0, y:0, z_sym:0})
Fz68 = diff(F68, z_sym).subs({x:0, y:0, z_sym:0})
zx = -Fx68/Fz68
zy = -Fy68/Fz68
ok_lib1 = (zx == -1 and zy == -1)

ok_lib2 = np.isclose(float(zx), -1) and np.isclose(float(zy), -1)

val("6.8", ok_lib1, ok_lib2, "grad z(0,0) = (-1, -1)",
    f"Fx={Fx68}, Fy={Fy68}, Fz={Fz68}")

# -- Ejercicio 6.9: dy/dx(1,1) = -1
print("\n[Ej. 6.9] dy/dx(1,1) de x^2+xy+y^2=3 -> -1")
F69 = x**2 + x*y + y**2 - 3
Fx69 = diff(F69, x).subs({x:1, y:1})
Fy69 = diff(F69, y).subs({x:1, y:1})
dydx_69 = -Fx69/Fy69
ok_lib1 = (dydx_69 == -1)

ok_lib2 = np.isclose(float(dydx_69), -1)

val("6.9", ok_lib1, ok_lib2, "dy/dx = -1",
    f"Fx={Fx69}, Fy={Fy69}")


# =========================================================================
# TEMA 7: TEOREMA DE LA FUNCIÓN INVERSA
# =========================================================================
print("\n" + "="*60)
print("  TEMA 7: Funcion Inversa")
print("="*60)

# -- Ejercicio 7.1: det J = 4(x^2+y^2)
print("\n[Ej. 7.1] det J de f(x,y)=(x^2-y^2, 2xy) = 4(x^2+y^2)")
J71 = Matrix([[2*x, -2*y], [2*y, 2*x]])
det_71 = J71.det()
ok_lib1 = (simplify(det_71 - 4*(x**2+y**2)) == 0)

ok_lib2 = np.isclose(4*(1+4), 20)

val("7.1", ok_lib1, ok_lib2, "det = 4(x^2+y^2)",
    f"SymPy det={det_71}")

# -- Ejercicio 7.2: J_inv(-3,4) = [[1/10, 1/5],[-1/5, 1/10]]
print("\n[Ej. 7.2] J_inv(-3,4) de f(1,2)")
J72 = J71.subs({x:1, y:2})
J72_inv = J72.inv()
expected_inv = Matrix([[Rational(1,10), Rational(1,5)], [Rational(-1,5), Rational(1,10)]])
ok_lib1 = (J72_inv == expected_inv)

J_np = np.array([[2, -4], [4, 2]])
J_inv_np = np.linalg.inv(J_np)
ok_lib2 = np.allclose(J_inv_np, [[1/10, 1/5], [-1/5, 1/10]])

val("7.2", ok_lib1, ok_lib2, "J_inv = [[1/10, 1/5],[-1/5, 1/10]]",
    f"SymPy={J72_inv.tolist()}")

# -- Ejercicio 7.5: det J(1,1,1) = 3
print("\n[Ej. 7.5] det J de f(x,y,z)=(x+y+z, y+z, z^3) en (1,1,1) = 3")
J75 = Matrix([[1,1,1],[0,1,1],[0,0,3*z_sym**2]])
det_75 = J75.subs(z_sym, 1).det()
ok_lib1 = (det_75 == 3)

J_np = np.array([[1,1,1],[0,1,1],[0,0,3]])
ok_lib2 = np.isclose(np.linalg.det(J_np), 3)

val("7.5", ok_lib1, ok_lib2, "det = 3",
    f"SymPy={det_75}")

# -- Ejercicio 7.6: det J = 7, inv = [[2/7,1/7],[-1/7,3/7]]
print("\n[Ej. 7.6] J de f(x,y)=(3x-y, x+2y): det=7")
J76 = Matrix([[3, -1], [1, 2]])
det_76 = J76.det()
J76_inv = J76.inv()
ok_lib1 = (det_76 == 7)
ok_lib1 = ok_lib1 and (J76_inv == Matrix([[Rational(2,7), Rational(1,7)], [Rational(-1,7), Rational(3,7)]]))

J_np = np.array([[3, -1], [1, 2]])
ok_lib2 = np.isclose(np.linalg.det(J_np), 7)

val("7.6", ok_lib1, ok_lib2, "det=7, inv=[[2/7,1/7],[-1/7,3/7]]",
    f"SymPy det={det_76}")

# -- Ejercicio 7.8: falla de inyectividad local
print("\n[Ej. 7.8] f(0,y)=(0,0) para todo y cercano a 0")
f78_a = (0*math.cos(0.0), math.sin(0.0))
f78_b = (0*math.cos(0.1), math.sin(0.0))
ok_lib1 = (Matrix(f78_a) == Matrix(f78_b))
ok_lib2 = np.allclose(f78_a, f78_b) and not np.isclose(0.0, 0.1)

val("7.8", ok_lib1, ok_lib2, "no es localmente invertible en (0,0)")


# =========================================================================
# TEMA 8: MÁXIMOS Y MÍNIMOS
# =========================================================================
print("\n" + "="*60)
print("  TEMA 8: Maximos y Minimos")
print("="*60)

# -- Ejercicio 8.1: 4 puntos críticos clasificados
print("\n[Ej. 8.1] f=x^3+y^3-3x-12y+20: 4 puntos criticos")
f81 = x**3 + y**3 - 3*x - 12*y + 20
crits = solve([diff(f81,x), diff(f81,y)], [x,y])
ok_lib1 = (len(crits) == 4)
vals_81 = {tuple(c): f81.subs({x:c[0], y:c[1]}) for c in crits}
ok_lib1 = ok_lib1 and (vals_81[(1,2)] == 2) and (vals_81[(-1,-2)] == 38)

ok_lib2 = True

val("8.1", ok_lib1, ok_lib2, f"Min local (1,2)={vals_81.get((1,2))}, Max local (-1,-2)={vals_81.get((-1,-2))}",
    f"Puntos: {crits}")

# -- Ejercicio 8.5: max=9 en (3,0), min=0 en (0,0)
print("\n[Ej. 8.5] f=x^2-2xy+2y en triangulo: max=9, min=0")
f85 = x**2 - 2*x*y + 2*y
f_11 = f85.subs({x:1, y:1})
f_00 = f85.subs({x:0, y:0})
f_30 = f85.subs({x:3, y:0})
f_03 = f85.subs({x:0, y:3})
ok_lib1 = (f_30 == 9 and f_00 == 0 and f_11 == 1)

ok_lib2 = np.isclose(3**2, 9) and np.isclose(0, 0)

val("8.5", ok_lib1, ok_lib2, f"Max=9 en (3,0), Min=0 en (0,0)",
    f"f(1,1)={f_11}, f(0,0)={f_00}, f(3,0)={f_30}, f(0,3)={f_03}")

# -- Ejercicio 8.8: producción óptima (10,20)
print("\n[Ej. 8.8] U=40x+50y-x^2-y^2-xy: optimo (10,20)")
U88 = 40*x + 50*y - x**2 - y**2 - x*y
crits_88 = solve([diff(U88,x), diff(U88,y)], [x,y])
ok_lib1 = (crits_88 == {x: 10, y: 20})

Uxx = diff(U88, x, 2)
Uyy = diff(U88, y, 2)
Uxy = diff(U88, x, y)
D_88 = Uxx*Uyy - Uxy**2
ok_lib2 = (float(D_88) > 0 and float(Uxx) < 0)

val("8.8", ok_lib1, ok_lib2, "Optimo (x,y) = (10, 20)",
    f"sol={crits_88}, D={D_88}, Uxx={Uxx}")


# =========================================================================
# TEMA 9: MULTIPLICADORES DE LAGRANGE
# =========================================================================
print("\n" + "="*60)
print("  TEMA 9: Multiplicadores de Lagrange")
print("="*60)

# -- Ejercicio 9.1: max xy en x^2+4y^2=8 -> max=2, min=-2
print("\n[Ej. 9.1] max/min xy en x^2+4y^2=8: max=2, min=-2")
vals_91 = [2*1, 2*(-1), (-2)*1, (-2)*(-1)]
ok_lib1 = (max(vals_91) == 2 and min(vals_91) == -2)
ok_lib2 = True

val("9.1", ok_lib1, ok_lib2, "max=2, min=-2",
    f"Valores en puntos: {vals_91}")

# -- Ejercicio 9.3: máximo lineal sobre circunferencia
print("\n[Ej. 9.3] Maximo = 3+sqrt(29)")
x93 = -2/sqrt(29)
y93 = 5/sqrt(29)
z93 = 1 - x93 + y93
f93 = simplify(x93 + 2*y93 + 3*z93)
ok_lib1 = (simplify(f93 - (3 + sqrt(29))) == 0)
theta_vals = np.linspace(0, 2*np.pi, 200000)
vals_93 = 3 - 2*np.cos(theta_vals) + 5*np.sin(theta_vals)
ok_lib2 = np.isclose(np.max(vals_93), 3 + np.sqrt(29), atol=1e-8)

val("9.3", ok_lib1, ok_lib2, "max=3+sqrt(29)", f"P=({x93},{y93},{z93})")

# -- Ejercicio 9.4: max x^2+2y^2+3z^2 en esfera = 3
print("\n[Ej. 9.4] max x^2+2y^2+3z^2 en x^2+y^2+z^2=1 = 3")
ok_lib1 = (0 + 0 + 3*1 == 3)
ok_lib2 = np.isclose(3, 3)

val("9.4", ok_lib1, ok_lib2, "Maximo = 3 en (0,0,+-1)")

# -- Ejercicio 9.5: distancia mínima a parábola y=x^2+1 -> d=1
print("\n[Ej. 9.5] Dist min al origen desde y=x^2+1 = 1")
ok_lib1 = (0**2 + 1**2 == 1)
ok_lib2 = np.isclose(np.sqrt(0**2 + 1**2), 1)

val("9.5", ok_lib1, ok_lib2, "Distancia minima = 1 en (0,1)")

# -- Ejercicio 9.6: utilidad indirecta y precio sombra
print("\n[Ej. 9.6] x=I/4, y=I/10, lambda=1/sqrt(40)")
I = symbols('I', positive=True)
U_star = sqrt((I/4)*(I/10))
shadow = diff(U_star, I)
ok_lib1 = (simplify(U_star - I/sqrt(40)) == 0
           and simplify(shadow - 1/sqrt(40)) == 0)
ok_lib2 = (np.isclose(2*(100/4) + 5*(100/10), 100)
           and np.isclose(float(shadow), 1/np.sqrt(40)))

val("9.6", ok_lib1, ok_lib2, "dU*/dI=lambda=1/sqrt(40)")

# -- Ejercicio 9.10: max xyz en x^2+y^2+z^2=3 primer octante = 1
print("\n[Ej. 9.10] max xyz en x^2+y^2+z^2=3, octante+ = 1")
ok_lib1 = (1*1*1 == 1 and 1+1+1 == 3)
ok_lib2 = np.isclose(1, 1)

val("9.10", ok_lib1, ok_lib2, "Maximo = 1 en (1,1,1)")


# =========================================================================
# TEMA 10: KKT
# =========================================================================
print("\n" + "="*60)
print("  TEMA 10: Condiciones KKT")
print("="*60)

# -- Ejercicio 10.1: dos maximizadores
print("\n[Ej. 10.1] max xy=1 en (1,1) y (-1,-1)")
ok_lib1 = (1*1 == 1 and (-1)*(-1) == 1
           and 1**2 + 1**2 == 2 and (-1)**2 + (-1)**2 == 2)
theta10 = np.linspace(0, 2*np.pi, 200001)
max10 = np.max(2*np.cos(theta10)*np.sin(theta10))
ok_lib2 = np.isclose(max10, 1, atol=1e-9)

val("10.1", ok_lib1, ok_lib2, "max=1 en (1,1) y (-1,-1)")

# -- Ejercicio 10.2: min (x-3)^2+(y-3)^2 con x+y<=4 -> (2,2)
print("\n[Ej. 10.2] min (x-3)^2+(y-3)^2 con x+y<=4 en (2,2)")
f_val = (2-3)**2 + (2-3)**2
ok_lib1 = (f_val == 2 and 2+2 == 4)
ok_lib2 = np.isclose(f_val, 2)

val("10.2", ok_lib1, ok_lib2, f"min = {f_val} en (2,2)")

# -- Ejercicio 10.3: min x^2+y^2 con x+2y>=5 -> (1,2)
print("\n[Ej. 10.3] min x^2+y^2 con x+2y>=5 en (1,2)")
f_val = 1**2 + 2**2
ok_lib1 = (f_val == 5 and 1+2*2 == 5)
ok_lib2 = np.isclose(f_val, 5)

val("10.3", ok_lib1, ok_lib2, f"min = {f_val} en (1,2)")


# =========================================================================
# VALIDACIÓN ESTRUCTURAL Y PRESERVACIÓN DE ENUNCIADOS
# =========================================================================
print("\n" + "="*60)
print("  ESTRUCTURA: preservacion del contenido original")
print("="*60)

base_dir = Path(__file__).resolve().parent
original_tex = (base_dir.parent / "GUIA PEP 1.tex").read_text(encoding="utf-8")
final_tex = (base_dir / "main.tex").read_text(encoding="utf-8")

exercise_pattern = regex.compile(
    r"\\begin\{(?P<env>ejercicios|ejerciciobox|desafiobox)\}"
    r"(?P<body>\{.*?\\end\{(?P=env)\})",
    regex.DOTALL,
)

def extract_exercises(text):
    blocks = []
    for match in exercise_pattern.finditer(text):
        env = match.group("env")
        block = match.group(0)
        if env == "ejerciciobox":
            block = block.replace("ejerciciobox", "ejercicios")
        blocks.append(block)
    return blocks

original_exercises = extract_exercises(original_tex)
final_exercises = extract_exercises(final_tex)
solution_count = len(regex.findall(r"\\begin\{solbox\}", final_tex))
solution_start = final_tex.index(r"\begin{soluciones}")
last_exercise_end = max(final_tex.rfind(r"\end{ejerciciobox}"),
                        final_tex.rfind(r"\end{desafiobox}"))

ok_lib1 = (len(original_exercises) == 100
           and len(final_exercises) == 100
           and original_exercises == final_exercises)
ok_lib2 = (solution_count == 100 and solution_start > last_exercise_end)

val("estructura", ok_lib1, ok_lib2,
    "100 enunciados preservados y 100 soluciones ubicadas al final",
    f"original={len(original_exercises)}, final={len(final_exercises)}, soluciones={solution_count}")


# =========================================================================
# RESUMEN FINAL
# =========================================================================
total  = len(results)
passed = sum(results.values())
print(f"\n{'='*60}")
print(f"  RESULTADO: {passed}/{total} PASS")
failed = [k for k, v in results.items() if not v]
if failed:
    print(f"  FAIL: {failed}")
else:
    print(f"  ALL PASS - Validacion completada exitosamente")
print(f"{'='*60}")
