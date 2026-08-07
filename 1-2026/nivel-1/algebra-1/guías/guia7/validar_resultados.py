"""Validación interna reproducible de la Guía 7 (no se imprime en el PDF)."""

from fractions import Fraction
import cmath
import math

import numpy as np
import sympy as sp


def close(a, b, tol=1e-10):
    assert abs(complex(a) - complex(b)) < tol, (a, b)


x, y, z, a, n, lam = sp.symbols("x y z a n lambda", real=True)

# I. Matrices y sistemas
systems = [
    [x + 3*y - z + 3, 3*x - y + 2*z - 1, 2*x - y + z + 1],
    [x + 3*y - 3*z + 5, 2*x - y + z + 3, -6*x + 3*y - 3*z - 4],
    [2*x - y + z, x - y - 2*z, 2*x - 3*y - z],
]
assert sp.linsolve(systems[0], (x, y, z)) == sp.FiniteSet((-2, 1, 4))
assert sp.linsolve(systems[1], (x, y, z)) == sp.EmptySet
assert sp.linsolve(systems[2], (x, y, z)) == sp.FiniteSet((0, 0, 0))

A = sp.Matrix([[1, 2], [0, -3]])
B = sp.Matrix([[2, -1], [3, 1]])
assert (A+B)*(A-B) == sp.Matrix([[-6, 5], [3, 17]])
assert A**2-B**2 == sp.Matrix([[0, -1], [-9, 11]])
assert np.array_equal(np.array(A+B, int), np.array([[3, 1], [3, -2]]))

assert sp.Matrix([[0, -2, 7], [5, 4, -3]]) + sp.Matrix([[8, 4, 0], [0, 1, 4]]) == sp.Matrix([[8, 2, 7], [5, 5, 1]])
assert sp.Matrix([[7], [-16]]) + sp.Matrix([[-11], [9]]) == sp.Matrix([[-4], [-7]])

A4 = sp.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, -1]])
B4 = sp.Matrix([[x, 1, -1], [1, x, 0], [2, -2, 1]])
assert sp.solve(sp.Eq((A4**2).det(), (2*B4).det()), x) == [-1]

A5 = sp.Matrix([[0, 1, -1], [1, 1, 0], [0, 1, 0]])
assert sp.solve(sp.Eq((2*A5-x*sp.eye(3)).det(), 2*x**2-x**3), x) == [2]
assert sp.solve(systems := [2*x-3*y+z+2, 3*x-2*z-4, 2*y-4*z+3], (x, y, z))[x] == 3

M7 = sp.Matrix([[1, -1, 0], [-1, a+4, 2], [2, -2, a-2]])
r7 = sp.Matrix([1, a+2, 4-a])
assert sp.factor(M7.det()) == (a-2)*(a+3)
assert sp.simplify((M7.inv()*r7)[2]) == -1

A8 = sp.Matrix([[-7, 4, 4], [4, -1, 8], [4, 8, -1]])
assert A8**2 == 81*sp.eye(3)
assert sp.solve(sp.Eq(9*(x**2-5), 3*(2*x**2+1)), x) == [-4, 4]

A9 = sp.Matrix([[lam, 1, 2], [0, 2, -1], [3, 0, lam]])
B9 = sp.Matrix([[1, 1, 0], [1, 0, -2], [0, 0, 1]])
assert sp.solve(sp.Eq(A9.det(), (A9-lam*B9**2).det()), lam) == [0, sp.Rational(3, 2)]

# II. Sumatorias: SymPy y aritmética racional exacta
j = sp.symbols("j", integer=True, positive=True)
n_pos = sp.symbols("n_pos", integer=True, positive=True)
sum_shift = sp.summation((j-1)**4, (j, 2, n_pos+2)) - sp.summation(j**4, (j, 1, n_pos))
assert sp.expand(sum_shift-(n_pos+1)**4) == 0
assert sum(Fraction(i, (i+1)**2)-Fraction(i-1, i*i) for i in range(1, 18)) == Fraction(17, 324)
assert sum(Fraction(3, (2*i-1)*(2*i+3)) for i in range(2, 16)) == Fraction(602, 1705)
S = lambda m: Fraction(m*m+5*m, 2)
assert (S(5)-S(4))+(S(6)-S(5)) == 15
solutions_c = [c for c in range(100) if sum((Fraction(3, 4*k*k-1) for k in range(2, c+2)), Fraction()) == Fraction(c, 17)]
assert solutions_c == [0, 7]
for m in range(1, 100):
    assert sum((2*k-1)**2 for k in range(1, m+1)) == m*(4*m*m-1)//3
# De las dos identidades dadas se obtiene sum a_k=45/2.
assert Fraction(432)-6*Fraction(45, 2) == 297

# III. Complejos: verificación simbólica y numérica independiente
I = sp.I
assert sp.simplify((1+I)**6/(1-I)**4) == 2*I
# Igualdad de distancias: (x)^2+(y-2)^2=(x+4)^2+y^2.
assert sp.solve(sp.Eq(x**2+(y-2)**2, (x+4)**2+y**2), y) == [-2*x-3]
z_complex = sp.symbols("z_complex")
assert set(sp.solve(sp.Eq(z_complex**2, 3-4*I), z_complex)) == {-2+I, 2-I}
z1, z2 = 1+I*sp.sqrt(3), sp.sqrt(3)-I
assert sp.expand(z1**5*sp.conjugate(z2)**3) == 128*sp.sqrt(3)+128*I
zz = sp.symbols("zz")
P = zz**3-zz**2+2
Q = zz**2-I*zz-(1+I)
assert sp.expand(Q*(zz-1+I)) == P
assert sp.solve(sp.Eq((4+sp.symbols('k', real=True)**2)/10, 2)) == [-4, 4]
for theta in np.linspace(-math.pi+0.01, math.pi-0.01, 257):
    unit = cmath.exp(1j*theta)
    w = (unit-1)/(unit+1)
    close(w.real, 0)

print("OK: 23 ejercicios y todos sus resultados fueron validados.")
