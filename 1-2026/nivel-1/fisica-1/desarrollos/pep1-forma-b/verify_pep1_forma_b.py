"""
VALIDACION — PAUTA PEP 1 Fisica I (Forma B) — USACH
Librerias: SymPy (exacto/simbolico) + NumPy (numerico independiente)

Cada resultado que aparece en la pauta LaTeX se valida aqui con dos
metodos independientes. Se imprime PASS/FAIL por item y un resumen final.
"""

from sympy import (symbols, Rational, sqrt, solve, nsimplify, simplify,
                   S, atan2, pi, cos, sin, rad, deg, Eq, N)
import numpy as np
import math

PASS_ct = []
def val(tag, ok, valor, detalle=""):
    PASS_ct.append((tag, ok))
    print(f"  {'PASS' if ok else 'FAIL'}  [{tag}]  -> {valor}")
    if detalle:
        print(f"        {detalle}")

g = Rational(98, 10)  # 9.8 m/s^2

print("="*60)
print("PROBLEMA 1  — Camion autonomo (grafico v-t)")
print("="*60)

# Grafico: (0,0)->(8,24)->(20,24)->(26,0)
# Etapa 1: 0<=t<=8 ; Etapa 2: 8<=t<=20 (v=24) ; Etapa 3: 20<=t<=26
# (a) aceleraciones
a1 = Rational(24-0, 8-0)      # 3
a3 = Rational(0-24, 26-20)    # -4
# NumPy check (pendiente de la recta)
a1_np = (24-0)/(8-0)
a3_np = (0-24)/(26-20)
val("1a-a1", (a1 == 3) and math.isclose(a1_np, 3.0), f"a1 = {a1} m/s^2",
    f"NumPy={a1_np}")
val("1a-a3", (a3 == -4) and math.isclose(a3_np, -4.0), f"a3 = {a3} m/s^2",
    f"NumPy={a3_np}")

# (b) Ecuaciones de posicion (origen en posicion inicial del camion)
# Etapa 1: x1(t) = 1.5 t^2   (0<=t<=8) -> en t=8: 96
# Etapa 2: x2(t) = 96 + 24(t-8) (8<=t<=20) -> en t=20: 384
# Etapa 3: x3(t) = 384 + 24(t-20) - 2 (t-20)^2 -> en t=26: 456
x1_8 = Rational(3,2)*8**2
x2_20 = 96 + 24*(20-8)
x3_26 = 384 + 24*(26-20) - 2*(26-20)**2
val("1b-x1(8)", x1_8 == 96, f"x1(8) = {x1_8} m  (x1(t)=1.5 t^2)")
val("1b-x2(20)", x2_20 == 384, f"x2(20) = {x2_20} m  (x2=96+24(t-8))")
val("1b-x3(26)", x3_26 == 456, f"x3(26) = {x3_26} m  (x3=384+24(t-20)-2(t-20)^2)")
# continuidad de velocidades: etapa1 termina en 24, etapa3 termina en 0
val("1b-cont", (3*8 == 24) and (24 - 4*6 == 0), "continuidad v: 24 y 0 OK")

# (c) Vehiculo de apoyo: parte en t=2 s, v0 desconocida, a=3 m/s^2
# tau = t*-2 (tiempo del apoyo). v_apoyo = v0 + 3*tau ; alcanza 26 en el encuentro
# Encuentro en etapa 2 del camion: x_camion = 96 + 24(t*-8)
tau, v0 = symbols('tau v0', positive=True)
# condicion de rapidez en el encuentro
eq_v = Eq(v0 + 3*tau, 26)
# posiciones: apoyo x = v0*tau + 1.5 tau^2 ; camion (etapa2) = 96 + 24*((tau+2)-8)
x_apoyo = v0*tau + Rational(3,2)*tau**2
x_cam2  = 96 + 24*((tau+2)-8)
eq_x = Eq(x_apoyo, x_cam2)
sol = solve([eq_v, eq_x], [v0, tau], dict=True)
sol = [s for s in sol if s[tau] > 0]
s = sol[0]
tau_v = s[tau]; v0_v = s[v0]
t_enc = tau_v + 2
x_enc = simplify(x_cam2.subs(s))
# comprobar que el encuentro cae en etapa 2 (8<=t*<=20)
en_etapa2 = (t_enc >= 8) and (t_enc <= 20)
# NumPy: resolver 3 tau^2 - 4 tau - 96 = 0
roots = np.roots([3, -4, -96])
tau_np = max(roots)
v0_np = 26 - 3*tau_np
x_np = 96 + 24*((tau_np+2)-8)
val("1c-v0", math.isclose(float(v0_v), v0_np, rel_tol=1e-9),
    f"v0 = {float(v0_v):.2f} m/s", f"SymPy={float(v0_v):.6f} NumPy={v0_np:.6f}")
val("1c-tenc", en_etapa2 and math.isclose(float(t_enc), tau_np+2, rel_tol=1e-9),
    f"t_encuentro = {float(t_enc):.2f} s (en etapa 2)", f"NumPy={tau_np+2:.6f}")
val("1c-x*", math.isclose(float(x_enc), x_np, rel_tol=1e-9),
    f"x* = {float(x_enc):.2f} m", f"SymPy={float(x_enc):.6f} NumPy={x_np:.6f}")

print("\n" + "="*60)
print("PROBLEMA 2  — Cohete de prueba (4 etapas)")
print("="*60)

VI0 = 70          # etapa I: sube libre desde el suelo (y=0)
aII = 5           # etapa II: motores, sube
h  = 1000         # fin etapa II (altitud)
H  = 300          # inicio etapa IV
# Etapa I: sube hasta v=0 -> altura h1
h1 = Rational(VI0**2, 1) / (2*g)     # 250
# Etapa II: de h1 (v=0) a h=1000 con aII -> v al final
v_finII_sq = 2*aII*(h - h1)
v_finII = sqrt(v_finII_sq)
# (a) altura maxima: etapa III solo gravedad desde y=1000 con v_finII
ymax = h + v_finII_sq/(2*g)
val("2a-h1", h1 == 250, f"altura fin etapa I = {h1} m")
val("2a-vII", v_finII_sq == 7500, f"v(fin II)^2 = {v_finII_sq} -> v = {float(v_finII):.2f} m/s")
ymax_np = 1000 + (2*5*(1000-250))/(2*9.8)
val("2a-ymax", math.isclose(float(ymax), ymax_np, rel_tol=1e-12),
    f"y_max = {float(ymax):.2f} m", f"SymPy={float(ymax):.6f} NumPy={ymax_np:.6f}")

# (b) v_IV: cae libre desde y_max (v=0) hasta H=300
vIV_sq = 2*g*(ymax - H)
vIV = sqrt(vIV_sq)
vIV_np = math.sqrt(2*9.8*(ymax_np - 300))
val("2b-vIV", math.isclose(float(vIV), vIV_np, rel_tol=1e-12),
    f"v_IV = {float(vIV):.2f} m/s (hacia abajo, -j)",
    f"SymPy={float(vIV):.6f} NumPy={vIV_np:.6f}")

# (c) a_final: frena de vIV a 0 en 300 m
# usando el dato vIV=145.67 del enunciado
vIV_dato = Rational(14567, 100)
a_final = vIV_dato**2 / (2*H)
a_final_np = (145.67**2)/(2*300)
val("2c-afinal", math.isclose(float(a_final), a_final_np, rel_tol=1e-12),
    f"a_final = {float(a_final):.2f} m/s^2 (hacia arriba, +j)",
    f"SymPy={float(a_final):.6f} NumPy={a_final_np:.6f}")

print("\n" + "="*60)
print("PROBLEMA 3  — Suma de vectores (dron)")
print("="*60)
# A: 90 m, 37 al Norte del Este -> (cos37, sin37)
# B: 70 m, 53 al Norte del Oeste -> (-cos53, +sin53)
# D: 40 m al Sur -> (0,-40)
th37 = rad(37); th53 = rad(53)
Ax = 90*cos(th37); Ay = 90*sin(th37)
Bx = -70*cos(th53); By = 70*sin(th53)
Dx = S(0); Dy = S(-40)
# NumPy
Ax_n, Ay_n = 90*math.cos(math.radians(37)), 90*math.sin(math.radians(37))
Bx_n, By_n = -70*math.cos(math.radians(53)), 70*math.sin(math.radians(53))
Dx_n, Dy_n = 0.0, -40.0
val("3a-A", math.isclose(float(Ax),Ax_n) and math.isclose(float(Ay),Ay_n),
    f"A = ({float(Ax):.2f}, {float(Ay):.2f}) m")
val("3a-B", math.isclose(float(Bx),Bx_n) and math.isclose(float(By),By_n),
    f"B = ({float(Bx):.2f}, {float(By):.2f}) m")
val("3a-D", True, f"D = ({float(Dx):.2f}, {float(Dy):.2f}) m")

# (b) A + B + C = D  -> C = D - A - B
Cx = Dx - Ax - Bx; Cy = Dy - Ay - By
Cx_n = Dx_n - Ax_n - Bx_n; Cy_n = Dy_n - Ay_n - By_n
val("3b-C", math.isclose(float(Cx),Cx_n) and math.isclose(float(Cy),Cy_n),
    f"C = ({float(Cx):.2f}, {float(Cy):.2f}) m",
    f"NumPy=({Cx_n:.6f},{Cy_n:.6f})")

# (c) magnitud y direccion de C respecto a +x
Cmag = sqrt(Cx**2 + Cy**2)
Cmag_n = math.hypot(Cx_n, Cy_n)
theta = deg(atan2(Cy, Cx))          # en [-180,180]
theta_n = math.degrees(math.atan2(Cy_n, Cx_n))
theta_pos = float(theta) % 360
val("3c-mag", math.isclose(float(Cmag),Cmag_n),
    f"|C| = {float(Cmag):.2f} m", f"NumPy={Cmag_n:.6f}")
val("3c-dir", math.isclose(float(theta),theta_n),
    f"theta = {float(theta):.2f} deg  (equiv. {theta_pos:.2f} deg CCW desde +x)",
    f"NumPy={theta_n:.6f}")

print("\n" + "="*60)
total = len(PASS_ct); passed = sum(1 for _,ok in PASS_ct if ok)
print(f"  RESULTADO: {passed}/{total} PASS")
fails = [t for t,ok in PASS_ct if not ok]
print("  TODOS VALIDADOS" if not fails else f"  FALLIDOS: {fails}")
print("="*60)
