"""
VALIDACIÓN — Guía 3 Unidad III — Álgebra II
Espacios Vectoriales y Transformaciones Lineales
Librerías: sympy (simbólico) + numpy / numpy.linalg (numérico)

Cada ejercicio se valida con DOS enfoques independientes.
"""

import sympy as sp
import numpy as np
import numpy.linalg as la

results = {}

def val(tag, ok1, ok2, solucion, detalle=""):
    ok = bool(ok1) and bool(ok2)
    results[tag] = ok
    print(f"  {'PASS' if ok else 'FAIL'}  [{tag}]  -> {solucion}")
    if detalle:
        print(f"        {detalle}")

rng = np.random.default_rng(0)

# ===========================================================
# Ej.1  W={(x,y,z): x-2y+z=0} subespacio de R^3  -> SI
# ===========================================================
# Lib1 sympy: condición homogénea lineal => subespacio
# cero pertenece, cerrado: probamos simbólicamente
x1,y1,z1,x2,y2,z2,a = sp.symbols('x1 y1 z1 x2 y2 z2 a')
f = lambda x,y,z: x-2*y+z
zero_ok = f(0,0,0)==0
suma_ok = sp.simplify(f(x1+x2,y1+y2,z1+z2) - (f(x1,y1,z1)+f(x2,y2,z2)))==0
esc_ok  = sp.simplify(f(a*x1,a*y1,a*z1) - a*f(x1,y1,z1))==0
ok1 = zero_ok and suma_ok and esc_ok
# Lib2 numpy: muestreo - combinaciones de vectores del conjunto siguen en el conjunto
def sample_plane(n):  # genera vectores que cumplen x-2y+z=0 : x=2y-z
    y = rng.uniform(-5,5,n); z = rng.uniform(-5,5,n); x = 2*y - z
    return np.stack([x,y,z],1)
V = sample_plane(2000)
al = rng.uniform(-3,3,(2000,1)); be = rng.uniform(-3,3,(2000,1))
comb = al*V + be*V[::-1]
ok2 = np.allclose(comb[:,0]-2*comb[:,1]+comb[:,2], 0)
val("1", ok1, ok2, "Sí es subespacio")

# ===========================================================
# Ej.2  W={x+y=1}  -> NO (no contiene el cero)
# ===========================================================
ok1 = (0+0 != 1)  # cero no cumple
# numpy: suma de dos elementos del conjunto NO cumple (no cerrado)
ya = rng.uniform(-5,5,1000); xa = 1-ya  # x+y=1
yb = rng.uniform(-5,5,1000); xb = 1-yb
sx = xa+xb; sy = ya+yb
ok2 = not np.allclose(sx+sy, 1)  # la suma da 2, no 1
val("2", ok1, ok2, "No es subespacio (no contiene el vector cero)")

# ===========================================================
# Ej.3  W={[[a,b],[c,d]]: a+d=0} subespacio de M2 -> SI
# ===========================================================
aa,bb,cc,dd,ee,ff,gg,hh = sp.symbols('aa bb cc dd ee ff gg hh')
g = lambda a,d: a+d
zero_ok = g(0,0)==0
suma_ok = sp.simplify(g(aa+ee,dd+hh)-(g(aa,dd)+g(ee,hh)))==0
esc_ok  = sp.simplify(g(a*aa,a*dd)-a*g(aa,dd))==0
ok1 = zero_ok and suma_ok and esc_ok
# numpy
A = rng.uniform(-5,5,(1000,2,2)); A[:,1,1] = -A[:,0,0]  # a+d=0
B = rng.uniform(-5,5,(1000,2,2)); B[:,1,1] = -B[:,0,0]
S = 2.5*A + (-1.3)*B
ok2 = np.allclose(S[:,0,0]+S[:,1,1], 0)
val("3", ok1, ok2, "Sí es subespacio")

# ===========================================================
# Ej.4  W={a0-a1+a2=0} en R2[x] -> SI
# ===========================================================
a0,a1,a2,b0,b1,b2 = sp.symbols('a0 a1 a2 b0 b1 b2')
h = lambda c0,c1,c2: c0-c1+c2
zero_ok = h(0,0,0)==0
suma_ok = sp.simplify(h(a0+b0,a1+b1,a2+b2)-(h(a0,a1,a2)+h(b0,b1,b2)))==0
esc_ok  = sp.simplify(h(a*a0,a*a1,a*a2)-a*h(a0,a1,a2))==0
ok1 = zero_ok and suma_ok and esc_ok
P = rng.uniform(-5,5,(1000,3)); P[:,0] = P[:,1]-P[:,2]  # a0=a1-a2
Q = rng.uniform(-5,5,(1000,3)); Q[:,0] = Q[:,1]-Q[:,2]
R = 2*P-0.7*Q
ok2 = np.allclose(R[:,0]-R[:,1]+R[:,2], 0)
val("4", ok1, ok2, "Sí es subespacio")

# ===========================================================
# Ej.5  W={x+y-z=0} generador {(-1,1,0),(1,0,1)}
# ===========================================================
gens = np.array([[-1,1,0],[1,0,1]], float)
# Lib1: cada gen cumple la ecuación  y  rango=2 (dim del plano)
ok1 = all(v[0]+v[1]-v[2]==0 for v in gens) and (la.matrix_rank(gens)==2)
# Lib2: el span de gens cubre el plano: tomar puntos del plano x+y-z=0 (z=x+y)
def sample_plane5(n):
    xx = rng.uniform(-5,5,n); yy = rng.uniform(-5,5,n); zz = xx+yy
    return np.stack([xx,yy,zz],1)
pts = sample_plane5(500)
M = gens.T  # 3x2
# resolver least squares y comprobar residuo ~0
coef,res,rk,sv = la.lstsq(M, pts.T, rcond=None)
recon = (M@coef).T
ok2 = np.allclose(recon, pts, atol=1e-9)
val("5", ok1, ok2, "{(-1,1,0),(1,0,1)}")

# ===========================================================
# Ej.6  W={x-y+t=0} en R^4, gen {(1,1,0,0),(0,0,1,0),(-1,0,0,1)}
# ===========================================================
gens6 = np.array([[1,1,0,0],[0,0,1,0],[-1,0,0,1]], float)
cond6 = lambda v: v[0]-v[1]+v[3]
ok1 = all(cond6(v)==0 for v in gens6) and la.matrix_rank(gens6)==3
# muestreo del subespacio: x=y-t
n=500
y=rng.uniform(-5,5,n); z=rng.uniform(-5,5,n); t=rng.uniform(-5,5,n); xv=y-t
pts6 = np.stack([xv,y,z,t],1)
M6 = gens6.T
coef,_,_,_ = la.lstsq(M6, pts6.T, rcond=None)
ok2 = np.allclose((M6@coef).T, pts6, atol=1e-9)
val("6", ok1, ok2, "{(1,1,0,0),(0,0,1,0),(-1,0,0,1)}")

# ===========================================================
# Ej.7  W={a=d} en M2, gen {I,[[0,1],[0,0]],[[0,0],[1,0]]}
# ===========================================================
g7 = [np.array([[1,0],[0,1]]),np.array([[0,1],[0,0]]),np.array([[0,0],[1,0]])]
g7f = np.array([m.flatten() for m in g7], float)
ok1 = all(m[0,0]==m[1,1] for m in g7) and la.matrix_rank(g7f)==3
# muestreo: matrices con a=d
n=500
av=rng.uniform(-5,5,n); bv=rng.uniform(-5,5,n); cv=rng.uniform(-5,5,n)
Wm = np.stack([av,bv,cv,av],1)  # [a,b,c,d=a]
coef,_,_,_ = la.lstsq(g7f.T, Wm.T, rcond=None)
ok2 = np.allclose((g7f.T@coef).T, Wm, atol=1e-9)
val("7", ok1, ok2, "{I, E12, E21}")

# ===========================================================
# Ej.8  W={p(1)=0} en R2[x], gen {-1+x, -1+x^2}
# repr coef (a0,a1,a2): {(-1,1,0),(-1,0,1)}
# ===========================================================
g8 = np.array([[-1,1,0],[-1,0,1]], float)
p_at_1 = lambda c: c[0]+c[1]+c[2]
ok1 = all(p_at_1(v)==0 for v in g8) and la.matrix_rank(g8)==2
n=500
a1v=rng.uniform(-5,5,n); a2v=rng.uniform(-5,5,n); a0v=-a1v-a2v
P8 = np.stack([a0v,a1v,a2v],1)
coef,_,_,_ = la.lstsq(g8.T, P8.T, rcond=None)
ok2 = np.allclose((g8.T@coef).T, P8, atol=1e-9)
val("8", ok1, ok2, "{-1+x, -1+x^2}")

# ===========================================================
# Ej.9  {(1,2),(2,4)} -> LD
# ===========================================================
Mat9 = sp.Matrix([[1,2],[2,4]])
ok1 = Mat9.rank() < 2
ok2 = la.matrix_rank(np.array([[1,2],[2,4]],float)) < 2
val("9", ok1, ok2, "Linealmente dependiente")

# ===========================================================
# Ej.10 {(1,0,1),(0,1,2),(2,1,4)} -> LD
# ===========================================================
Mat10 = sp.Matrix([[1,0,1],[0,1,2],[2,1,4]])
ok1 = Mat10.rank() < 3
ok2 = la.matrix_rank(np.array([[1,0,1],[0,1,2],[2,1,4]],float)) < 3
val("10", ok1, ok2, "Linealmente dependiente")

# ===========================================================
# Ej.11 {(1,0,λ),(2,1,1),(0,λ,1)} base de R^3 para todo λ
# det = 2λ^2-λ+1, discriminante <0 => nunca 0
# ===========================================================
lam = sp.symbols('lambda')
Mat11 = sp.Matrix([[1,2,0],[0,1,lam],[lam,1,1]])  # vectores como columnas
det11 = sp.expand(Mat11.det())
ok1 = (det11 == 2*lam**2 - lam + 1) and (sp.solveset(det11,lam,domain=sp.S.Reals)==sp.S.EmptySet)
# numpy: probar muchos λ, det nunca 0
lams = np.linspace(-50,50,100000)
dets = 2*lams**2 - lams + 1
ok2 = np.all(np.abs(dets) > 1e-9)
val("11", ok1, ok2, f"Base para todo λ∈R  (det={det11})")

# ===========================================================
# Ej.12 W={x+y-z+t=0, 2x-y+z=0} base {(0,1,1,0),(-1,-2,0,3)} dim 2
# ===========================================================
A12 = sp.Matrix([[1,1,-1,1],[2,-1,1,0]])
ns12 = A12.nullspace()
dim12 = len(ns12)
base12 = np.array([[0,1,1,0],[-1,-2,0,3]], float)
c1 = lambda v: v[0]+v[1]-v[2]+v[3]
c2 = lambda v: 2*v[0]-v[1]+v[2]
ok1 = (dim12==2) and all(c1(v)==0 and c2(v)==0 for v in base12) and la.matrix_rank(base12)==2
# numpy: nullspace via SVD rank
A12n = np.array([[1,1,-1,1],[2,-1,1,0]],float)
ok2 = (4 - la.matrix_rank(A12n) == 2)
val("12", ok1, ok2, "base {(0,1,1,0),(-1,-2,0,3)}, dim=2")

# ===========================================================
# Ej.13 V=<(1,0,1,0),(2,1,0,1),(3,1,1,1)> base {v1,v2} dim 2
# v1+v2=v3
# ===========================================================
v1=np.array([1,0,1,0]);v2=np.array([2,1,0,1]);v3=np.array([3,1,1,1])
M13 = sp.Matrix([[1,0,1,0],[2,1,0,1],[3,1,1,1]])
ok1 = (M13.rank()==2) and np.array_equal(v1+v2, v3)
ok2 = (la.matrix_rank(np.array([[1,0,1,0],[2,1,0,1],[3,1,1,1]],float))==2)
val("13", ok1, ok2, "base {(1,0,1,0),(2,1,0,1)}, dim=2")

# ===========================================================
# Ej.14 T(x,y)=(x+y,2x-y,x) lineal -> SI
# ===========================================================
xs,ys,xt,yt = sp.symbols('xs ys xt yt')
T14 = lambda x,y: sp.Matrix([x+y,2*x-y,x])
add_ok = sp.simplify(T14(xs+xt,ys+yt)-(T14(xs,ys)+T14(xt,yt)))==sp.zeros(3,1)
sc_ok  = sp.simplify(T14(a*xs,a*ys)-a*T14(xs,ys))==sp.zeros(3,1)
ok1 = add_ok and sc_ok
# numpy: T es lineal sii matriz fija; comprobar T(u+v)=Tu+Tv
Mt = np.array([[1,1],[2,-1],[1,0]],float)
u=rng.uniform(-5,5,(1000,2)); v=rng.uniform(-5,5,(1000,2))
ok2 = np.allclose((Mt@(u+v).T).T, (Mt@u.T).T+(Mt@v.T).T)
val("14", ok1, ok2, "Sí es transformación lineal")

# ===========================================================
# Ej.15 T(x,y)=(x-y,2x+y,3y)  T(1,2),T(2,-1),T(a,b)
# ===========================================================
T15 = lambda x,y: (x-y,2*x+y,3*y)
r_a = T15(1,2); r_b = T15(2,-1)
ok1 = (r_a==(-1,4,6)) and (r_b==(3,3,-3))
M15 = np.array([[1,-1],[2,1],[0,3]],float)
ok2 = np.allclose(M15@np.array([1,2]), [-1,4,6]) and np.allclose(M15@np.array([2,-1]), [3,3,-3])
val("15", ok1, ok2, "T(1,2)=(-1,4,6), T(2,-1)=(3,3,-3), T(a,b)=(a-b,2a+b,3b)")

# ===========================================================
# Ej.16 T(x,y,z)=(x+y-z,2x-y+z) ker=<(0,1,1)> dim 1
# ===========================================================
M16 = sp.Matrix([[1,1,-1],[2,-1,1]])
ns16 = M16.nullspace()
ok1 = (len(ns16)==1)
# verificar generador (0,1,1)
kv = np.array([0,1,1],float)
M16n = np.array([[1,1,-1],[2,-1,1]],float)
ok2 = (3-la.matrix_rank(M16n)==1) and np.allclose(M16n@kv,0)
val("16", ok1, ok2, "ker=<(0,1,1)>, dim(ker)=1")

# ===========================================================
# Ej.17 T(x,y,z)=(x+y,y+z,x+z) ker={0}, Im=R^3, dim Im=3
# ===========================================================
M17 = sp.Matrix([[1,1,0],[0,1,1],[1,0,1]])
ok1 = (M17.det()!=0) and (len(M17.nullspace())==0) and (M17.rank()==3)
M17n = np.array([[1,1,0],[0,1,1],[1,0,1]],float)
ok2 = (abs(la.det(M17n))>1e-9) and (la.matrix_rank(M17n)==3)
val("17", ok1, ok2, "ker={0}, dim(Im)=3")

# ===========================================================
# Ej.18 T(x,y,z)=(x+2y-z,2x+y+z,x-y+2z)
# ker=<(-1,1,1)> dim 1, dim Im=2, NO iny/sob/biy/iso
# ===========================================================
M18 = sp.Matrix([[1,2,-1],[2,1,1],[1,-1,2]])
ns18 = M18.nullspace()
det18 = M18.det()
rank18 = M18.rank()
ok1 = (det18==0) and (len(ns18)==1) and (rank18==2)
M18n = np.array([[1,2,-1],[2,1,1],[1,-1,2]],float)
kv18 = np.array([-1,1,1],float)
ok2 = (abs(la.det(M18n))<1e-9) and (la.matrix_rank(M18n)==2) and np.allclose(M18n@kv18,0)
val("18", ok1, ok2, "ker=<(-1,1,1)>, dim(ker)=1, dim(Im)=2; NO iny/sob/biy/iso")

# ===========================================================
print("\n" + "="*55)
total=len(results); passed=sum(results.values())
print(f"  RESULTADO: {passed}/{total} PASS")
failed=[k for k,v in results.items() if not v]
print("  FALLIDOS:", failed if failed else "ninguno")
print("="*55)
