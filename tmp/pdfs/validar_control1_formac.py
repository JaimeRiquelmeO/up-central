from sympy import I, sqrt, simplify, conjugate, re, im, solve, symbols


z = (1 - 7 * I) / (2 + I)
w = (6 + 2 * I) / (2 - I)

assert simplify(z - (-1 - 3 * I)) == 0
assert simplify(w - (2 + 2 * I)) == 0

parte_real = simplify(re(3 * conjugate(z) - 2 * conjugate(w)))
parte_imaginaria = simplify(im(z**3))
resultado_1 = simplify(parte_real + parte_imaginaria)

assert parte_real == -7
assert parte_imaginaria == 18
assert resultado_1 == 11

u = symbols("u")
esperadas = [2 - sqrt(2) * I, -2 + sqrt(2) * I]

soluciones = solve(u**2 - 2 + 4 * I * sqrt(2), u)
assert len(soluciones) == 2
assert esperadas[0] != esperadas[1]
assert all(simplify(sol**2 - 2 + 4 * I * sqrt(2)) == 0 for sol in esperadas)

pares = sorted(
    [(simplify(re(sol)), simplify(im(sol))) for sol in esperadas],
    key=lambda par: float(par[0]),
)
assert pares == [(-2, sqrt(2)), (2, -sqrt(2))]

print("Ejercicio 1:", z, w, parte_real, parte_imaginaria, resultado_1)
print("Ejercicio 2:", esperadas)
print("Validaciones simbólicas exactas superadas.")
