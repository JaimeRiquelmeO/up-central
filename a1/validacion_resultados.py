"""Validacion independiente de la Guia 6 con SymPy, NumPy y mpmath."""

import mpmath as mp
import numpy as np
import sympy as sp


mp.mp.dps = 80
k, b, n, c = sp.symbols("k b n c", integer=True)

resultados = {}

# 1. Se despeja la suma total a partir de la segunda identidad.
suma_total = sp.solve(sp.Eq(4 * 196 - 12 * sp.Symbol("T") + 9 * 10, 1130), sp.Symbol("T"))[0]
resultados[1] = sp.simplify(suma_total - (-3 - 3 + 5))
assert resultados[1] == -sp.Rational(61, 3)

# 2. Calculo simbolico exacto.
lhs2 = sp.summation((2 * b - 4) / ((5 * k - 9) * (5 * k + 1)), (k, 2, 8))
resultados[2] = sp.solve(sp.Eq(lhs2, sp.Rational(329, 1476)), b)
assert resultados[2] == [3]

# 3. Con la convencion de suma vacia, ambos miembros valen cero para p entero negativo.
def suma_vacia(inicio, fin, termino):
    return sum((termino(j) for j in range(inicio, fin + 1)), 0)

for p in range(-20, 0):
    assert suma_vacia(2, p + 2, lambda j: sp.Rational(j - 2 * p, 2)) == 0
    assert suma_vacia(4, p + 4, lambda j: 3 * p + 1) == 0
resultados[3] = "todo p entero negativo"

# 4. Ambos lados en forma exacta.
rhs4 = sp.summation(sp.Rational(115, 1) / (8 * k**2 - 2), (k, 3, 11))
lhs4 = sp.simplify(n**2 / 2)
resultados[4] = [x for x in sp.solve(sp.Eq(lhs4, rhs4), n) if x.is_positive]
assert rhs4 == sp.Rational(9, 2) and resultados[4] == [3]

# 5. Verificacion entera independiente con NumPy.
i_np = np.arange(10, 41, dtype=np.int64)
resultados[5] = int(np.sum(i_np * (i_np + 1) ** 2))
assert resultados[5] == 714860

# 6. Parte polinomica exacta con NumPy y parte geometrica con SymPy/mpmath.
j_np = np.arange(101, 202, dtype=np.int64)
parte_polinomica = int(np.sum(j_np**2))
resultados[6] = sp.Rational(1, 2) * (1 - sp.Rational(1, 3) ** 99) + parte_polinomica
assert parte_polinomica == 2388751
valor6_mp = mp.fsum([mp.power(3, -q) for q in range(1, 100)]) + mp.fsum(
    [mp.mpf(q + 1) ** 2 for q in range(100, 201)]
)
assert abs(valor6_mp - mp.mpf(str(sp.N(resultados[6], 80)))) < mp.mpf("1e-70")

# 7. Identidad simbolica.
resultados[7] = sp.simplify(sp.summation(3 * k - 2, (k, 1, n)) - n * (3 * n - 1) / 2)
assert resultados[7] == 0

# 8. Geometrica: comprobacion numerica de alta precision.
resultados[8] = 1 - sp.Rational(1, 2) ** 100
assert abs(
    mp.fsum([mp.power(2, -q) for q in range(1, 101)])
    - mp.mpf(str(sp.N(resultados[8], 80)))
) < mp.mpf("1e-70")

# 9. Suma directa con NumPy y telescopica con mpmath.
primera9 = int(np.sum(np.arange(2, 9, dtype=np.int64) ** 2 + 2 * np.arange(2, 9, dtype=np.int64)))
segunda9 = mp.fsum([mp.root(3 * q, 3) - mp.root(3 * q + 3, 3) for q in range(9, 72)])
resultados[9] = primera9 + int(mp.nint(segunda9))
assert primera9 == 273 and mp.almosteq(segunda9, -3) and resultados[9] == 270

# 10. El indice superior exige c natural: la unica solucion admisible es 5.
primera10 = int(np.sum(np.arange(1, 21, dtype=np.int64) ** 2 - 10))
raices_formales = sp.solve(sp.Eq(c * (c + 1) / 2 + 9 * c, primera10 - 2610), c)
resultados[10] = [x for x in raices_formales if x.is_nonnegative]
assert primera10 == 2670 and set(raices_formales) == {-24, 5} and resultados[10] == [5]

# 11. Uso de sumas parciales.
A = lambda q: 2 * q**2 + 3 * q
resultados[11] = sp.Rational(A(20) - A(6) - 14 * 5, 2)
assert resultados[11] == 350

# 12. Tres calculos exactos.
resultados[12] = (160 + 6**2 + 8**2, (160 + 6**2) - 2 * (120 + 6), (6 - 1) ** 2 + (8 - 1) ** 2)
assert resultados[12] == (260, -56, 74)

# 13. Telescopica; mpmath comprueba la suma original.
resultados[13] = sp.sqrt(81) - sp.sqrt(16)
suma13_mp = mp.fsum([1 / (mp.sqrt(q) + mp.sqrt(q + 1)) for q in range(16, 81)])
assert resultados[13] == 5 and mp.almosteq(suma13_mp, 5)

print("Validacion completada con SymPy, NumPy y mpmath.")
for numero, valor in resultados.items():
    print(f"{numero:>2}: {valor}")
