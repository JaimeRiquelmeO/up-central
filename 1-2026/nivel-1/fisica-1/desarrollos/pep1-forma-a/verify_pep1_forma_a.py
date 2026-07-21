"""
VALIDACION — PAUTA PEP 1 Fisica I (Forma A) — USACH
Librerias: SymPy (exacto/simbolico) + NumPy (numerico independiente)
Datos leidos de la imagen (Forma A):
  P1: retraso 3 s, a=1.5 m/s^2, vf=28 m/s ; grafico 24 / (8,20,26)
  P2: vI0=80, aII=4, h=1000, H=200
  P3: A=100@37 N-E, B=80@53 N-O, D=50 Sur
"""
from sympy import symbols, Rational, sqrt, solve, simplify, S, atan2, rad, deg, Eq, cos, sin
import numpy as np
import math

PASS_ct = []
def val(tag, ok, valor, detalle=""):
    PASS_ct.append((tag, ok))
    print(f"  {'PASS' if ok else 'FAIL'}  [{tag}]  -> {valor}")
    if detalle:
        print(f"        {detalle}")

g = Rational(98, 10)

print("="*60)
print("PROBLEMA 1 — Camion autonomo (grafico v-t identico a B)")
print("="*60)
# grafico: (0,0)->(8,24)->(20,24)->(26,0)
a1 = Rational(24, 8); a3 = Rational(-24, 6)
val("1a-a1", a1 == 3, f"a1 = {a1} m/s^2")
val("1a-a3", a3 == -4, f"a3 = {a3} m/s^2")
# (b) posiciones
x1_8 = Rational(3,2)*8**2
x2_20 = 96 + 24*(20-8)
x3_26 = 384 + 24*(26-20) - 2*(26-20)**2
val("1b-x1(8)", x1_8 == 96, f"x1(t)=1.5 t^2 ; x1(8)={x1_8} m")
val("1b-x2(20)", x2_20 == 384, f"x2=96+24(t-8) ; x2(20)={x2_20} m")
val("1b-x3(26)", x3_26 == 456, f"x3=384+24(t-20)-2(t-20)^2 ; x3(26)={x3_26} m")

# (c) apoyo: retraso 3 s, a=1.5, vf=28 en el encuentro, en etapa 2
tau, v0 = symbols('tau v0', positive=True)
eq_v = Eq(v0 + Rational(3,2)*tau, 28)               # v0 + 1.5 tau = 28
x_apoyo = v0*tau + Rational(3,4)*tau**2              # 0.5*1.5 = 0.75
x_cam2  = 96 + 24*((tau+3)-8)                        # etapa 2, t = tau+3
eq_x = Eq(x_apoyo, x_cam2)
sol = [s for s in solve([eq_v, eq_x],[v0,tau],dict=True) if s[tau] > 0][0]
tau_v, v0_v = sol[tau], sol[v0]
t_enc = tau_v + 3
x_enc = simplify(x_cam2.subs(sol))
# NumPy: 3 tau^2 - 16 tau - 96 = 0
r = np.roots([3, -16, -96]); tau_np = max(r)
v0_np = 28 - 1.5*tau_np
x_np = 96 + 24*((tau_np+3)-8)
en2 = (t_enc >= 8) and (t_enc <= 20)
val("1c-v0", math.isclose(float(v0_v), v0_np, rel_tol=1e-9),
    f"v0 = {float(v0_v):.2f} m/s", f"SymPy={float(v0_v):.6f} NumPy={v0_np:.6f}")
val("1c-tenc", en2 and math.isclose(float(t_enc), tau_np+3, rel_tol=1e-9),
    f"t_enc = {float(t_enc):.2f} s (en etapa 2)", f"NumPy={tau_np+3:.6f}")
val("1c-x*", math.isclose(float(x_enc), x_np, rel_tol=1e-9),
    f"x* = {float(x_enc):.2f} m", f"SymPy={float(x_enc):.6f} NumPy={x_np:.6f}")

print("\n" + "="*60)
print("PROBLEMA 2 — Cohete (vI0=80, aII=4, h=1000, H=200)")
print("="*60)
VI0=80; aII=4; h=1000; H=200
h1 = Rational(VI0**2,1)/(2*g)                # etapa I
v2sq = 2*aII*(h - h1)                         # etapa II
ymax = h + v2sq/(2*g)
val("2a-h1", True, f"altura fin etapa I = {float(h1):.2f} m")
val("2a-v2", True, f"v(fin II)^2 = {float(v2sq):.2f} -> v = {float(sqrt(v2sq)):.2f} m/s")
ymax_np = 1000 + (2*4*(1000 - 6400/19.6))/(2*9.8)
val("2a-ymax", math.isclose(float(ymax), ymax_np, rel_tol=1e-9),
    f"y_max = {float(ymax):.2f} m  (enunciado: 1274.89)",
    f"SymPy={float(ymax):.6f} NumPy={ymax_np:.6f}")

vIVsq = 2*g*(ymax - H)
vIV = sqrt(vIVsq)
val("2b-vIV", math.isclose(float(vIV), math.sqrt(2*9.8*(ymax_np-200)), rel_tol=1e-9),
    f"v_IV = {float(vIV):.2f} m/s (hacia abajo, -j)  (enunciado: 145.15)",
    f"SymPy={float(vIV):.6f}")

vIV_dato = Rational(14515,100)
a_final = vIV_dato**2/(2*H)
val("2c-afinal", math.isclose(float(a_final), (145.15**2)/(2*200), rel_tol=1e-9),
    f"a_final = {float(a_final):.2f} m/s^2 (hacia arriba, +j)",
    f"SymPy={float(a_final):.6f} NumPy={(145.15**2)/(2*200):.6f}")

print("\n" + "="*60)
print("PROBLEMA 3 — Vectores (A=100@37, B=80@53, D=50 Sur)")
print("="*60)
Ax=90; # placeholder overwritten
Ax = 100*cos(rad(37)); Ay = 100*sin(rad(37))
Bx = -80*cos(rad(53)); By = 80*sin(rad(53))
Dx = S(0); Dy = S(-50)
Ax_n,Ay_n = 100*math.cos(math.radians(37)),100*math.sin(math.radians(37))
Bx_n,By_n = -80*math.cos(math.radians(53)),80*math.sin(math.radians(53))
Dx_n,Dy_n = 0.0,-50.0
val("3a-A", math.isclose(float(Ax),Ax_n) and math.isclose(float(Ay),Ay_n),
    f"A = ({float(Ax):.2f}, {float(Ay):.2f}) m")
val("3a-B", math.isclose(float(Bx),Bx_n) and math.isclose(float(By),By_n),
    f"B = ({float(Bx):.2f}, {float(By):.2f}) m")
val("3a-D", True, f"D = ({float(Dx):.2f}, {float(Dy):.2f}) m")

Cx = Dx - Ax - Bx; Cy = Dy - Ay - By
Cx_n = Dx_n - Ax_n - Bx_n; Cy_n = Dy_n - Ay_n - By_n
val("3b-C", math.isclose(float(Cx),Cx_n) and math.isclose(float(Cy),Cy_n),
    f"C = ({float(Cx):.2f}, {float(Cy):.2f}) m", f"NumPy=({Cx_n:.6f},{Cy_n:.6f})")

Cmag = sqrt(Cx**2+Cy**2); Cmag_n = math.hypot(Cx_n,Cy_n)
theta = deg(atan2(Cy,Cx)); theta_n = math.degrees(math.atan2(Cy_n,Cx_n))
val("3c-mag", math.isclose(float(Cmag),Cmag_n), f"|C| = {float(Cmag):.2f} m",
    f"NumPy={Cmag_n:.6f}")
val("3c-dir", math.isclose(float(theta),theta_n),
    f"theta = {float(theta):.2f} deg (= {float(theta)%360:.2f} CCW desde +x)",
    f"NumPy={theta_n:.6f}")

print("\n" + "="*60)
total=len(PASS_ct); passed=sum(1 for _,ok in PASS_ct if ok)
print(f"  RESULTADO: {passed}/{total} PASS")
fails=[t for t,ok in PASS_ct if not ok]
print("  TODOS VALIDADOS" if not fails else f"  FALLIDOS: {fails}")
print("="*60)
