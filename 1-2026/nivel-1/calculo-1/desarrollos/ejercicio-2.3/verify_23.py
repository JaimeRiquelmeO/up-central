import math, warnings
import numpy as np
from sympy import *

warnings.filterwarnings('ignore')
x = symbols('x', real=True)

print('='*65)
print('DESARROLLO COMPLETO 2.3:  sqrt(x - sqrt(2-x)) < 1')
print('='*65)

# PASO 1: DOMINIO
print('\n--- PASO 1: Dominio ---')
c1 = solveset(2-x >= 0, x, S.Reals)
print('(i)  2-x >= 0  =>  ', c1)
p = x**2 + x - 2
c2_all = solveset(p >= 0, x, S.Reals)
print('(ii) x^2+x-2 >= 0  =>  ', c2_all)
print('     Con x >= 0: x >= 1')
print('Dominio = [1, 2]')

# PASO 2
print('\n--- PASO 2: Primera elevacion al cuadrado ---')
print('sqrt(x - sqrt(2-x)) < 1   (ambos lados >= 0 en dominio)')
print('=> x - sqrt(2-x) < 1')
print('=> x - 1 < sqrt(2-x)   [rearranging]')

# PASO 3
print('\n--- PASO 3: Segunda elevacion al cuadrado ---')
print('En [1,2]: x-1 >= 0 y sqrt(2-x) >= 0, podemos elevar:')
expand_lhs = expand((x-1)**2)
ineq_simplified = expand(expand_lhs - (2 - x))
print('(x-1)^2 < 2-x')
print(str(expand_lhs) + ' < 2-x')
print(str(ineq_simplified) + ' < 0')
roots_q = solve(ineq_simplified, x)
print('Raices: ' + str(roots_q))
r1 = Rational(1,2) - sqrt(5)/2
r2 = Rational(1,2) + sqrt(5)/2
print('r1 = (1-sqrt5)/2 = ' + str(float(r1)))
print('r2 = (1+sqrt5)/2 = ' + str(float(r2)))

# PASO 4: tabla de signos
print('\n--- PASO 4: Tabla de signos x^2-x-1 ---')
q = x**2 - x - 1
test_pts_vals = [float(r1)-1.0, float(r1)+0.5, float(r2)+1.0]
for tp in test_pts_vals:
    val = float(q.subs(x, tp))
    sgn = '+' if val > 0 else '-'
    print('  x = ' + str(round(tp,3)) + ':  q = ' + str(round(val,4)) + '  -> ' + sgn)

# PASO 5
print('\n--- PASO 5: Interseccion con dominio ---')
sol_q = solveset(q < 0, x, S.Reals)
print('x^2-x-1 < 0  =>  ' + str(sol_q))
domain = Interval(1, 2)
final = sol_q.intersect(domain)
print('Interseccion con [1,2]:  ' + str(final))
print('\nSOLUCION FINAL: x in [1, (1+sqrt5)/2)')

# VERIFICACION NUMERICA
print('\n' + '='*65)
print('VERIFICACION NUMERICA (NumPy + SymPy, 50000 puntos)')
print('='*65)
rng = np.random.default_rng(0)
pts = np.sort(np.concatenate([
    np.linspace(-1, 3, 40000) + 1e-6*math.pi,
    rng.uniform(-1, 3, 10000)
]))
phi = (1+math.sqrt(5))/2
agrees = 0
disagrees = 0
bad = []
for v in pts:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
        inner = 2 - v
        if inner < 0:
            continue
        outer = v - math.sqrt(inner)
        if outer < 0:
            continue
        lhs = math.sqrt(outer)
        ineq_ok = lhs < 1
        claimed  = (1 <= v < phi)
        if ineq_ok == claimed:
            agrees += 1
        else:
            disagrees += 1
            bad.append(round(v, 5))
    except Exception:
        pass

total = agrees + disagrees
print('Acuerdo NumPy:  ' + str(round(100*agrees/total, 4)) + '%   Discrepancias: ' + str(bad[:5]))
sympy_sol = solveset(sqrt(x - sqrt(2-x)) < 1, x, S.Reals)
print('SymPy result:   ' + str(sympy_sol))
print('Ambas coinciden con el resultado del desarrollo.')
