"""Validación simbólica de la guía Preparación Control de Cálculo I."""

from __future__ import annotations

import sympy as sp


def verificar(numero: int, descripcion: str, condicion: bool) -> None:
    if not bool(condicion):
        raise AssertionError(f"Ejercicio {numero}: falló {descripcion}")
    print(f"[OK] {numero:02d} - {descripcion}")


x, h = sp.symbols("x h", real=True)

# 1. Potencias, suma y resta.
f1 = 5 * x**4 - 3 * x**2 + 7 * x - 9
verificar(1, "reglas básicas", sp.diff(f1, x) == 20 * x**3 - 6 * x + 7)

# 2. Derivadas elementales.
f2 = sp.sqrt(x) + 2 * sp.sin(x) - 3 * sp.cos(x) + sp.exp(x) + sp.log(x)
r2 = 1 / (2 * sp.sqrt(x)) + 2 * sp.cos(x) + 3 * sp.sin(x) + sp.exp(x) + 1 / x
verificar(2, "funciones elementales", sp.simplify(sp.diff(f2, x) - r2) == 0)

# 3. Producto.
f3 = (x**2 + 1) * (3 * x - 2)
verificar(3, "regla del producto", sp.expand(sp.diff(f3, x)) == 9 * x**2 - 4 * x + 3)

# 4. Cociente.
f4 = (2 * x + 1) / (x**2 + 4)
r4 = (-2 * x**2 - 2 * x + 8) / (x**2 + 4) ** 2
verificar(4, "regla del cociente", sp.simplify(sp.diff(f4, x) - r4) == 0)

# 5. Combinación de producto y suma.
f5 = x**3 - sp.pi / 3 - x**2 * sp.cos(x)
r5 = 3 * x**2 - 2 * x * sp.cos(x) + x**2 * sp.sin(x)
verificar(5, "producto con función trigonométrica", sp.simplify(sp.diff(f5, x) - r5) == 0)

# 6. Definición para una función polinómica.
f6 = x**2 - 4 * x + 1
cociente6 = sp.expand((f6.subs(x, x + h) - f6) / h)
limite6 = sp.limit(cociente6, h, 0)
verificar(6, "derivada por definición de un polinomio", limite6 == 2 * x - 4)

# 7. Definición para una función racional.
f7 = x / (x + 2)
limite7 = sp.limit((f7.subs(x, x + h) - f7) / h, h, 0)
verificar(7, "derivada por definición de un cociente", sp.simplify(limite7 - 2 / (x + 2) ** 2) == 0)

# 8. No diferenciabilidad de |x-3| en 3.
f8h = sp.Abs(h) / h
lim8_izq = sp.limit(f8h, h, 0, dir="-")
lim8_der = sp.limit(f8h, h, 0, dir="+")
verificar(8, "límites laterales del valor absoluto", lim8_izq == -1 and lim8_der == 1)

# 9. Recta tangente a -x^2+2x+2 en x=3.
f9 = -x**2 + 2 * x + 2
m9 = sp.diff(f9, x).subs(x, 3)
recta9 = sp.expand(m9 * (x - 3) + f9.subs(x, 3))
verificar(9, "recta tangente polinómica", m9 == -4 and recta9 == -4 * x + 11)

# 10. Recta tangente a x+1/x en x=1.
f10 = x + 1 / x
m10 = sp.diff(f10, x).subs(x, 1)
recta10 = sp.expand(m10 * (x - 1) + f10.subs(x, 1))
verificar(10, "recta tangente horizontal", m10 == 0 and recta10 == 2)

# 11. Producto con exponencial.
f11 = (x**2 - 1) * sp.exp(x)
r11 = sp.exp(x) * (x**2 + 2 * x - 1)
verificar(11, "producto con exponencial", sp.simplify(sp.diff(f11, x) - r11) == 0)

# 12. Cociente trigonométrico.
f12 = sp.sin(x) / (x**2 + 1)
r12 = ((x**2 + 1) * sp.cos(x) - 2 * x * sp.sin(x)) / (x**2 + 1) ** 2
verificar(12, "cociente trigonométrico", sp.simplify(sp.diff(f12, x) - r12) == 0)

# 13. Regla de la cadena en una potencia.
f13 = (3 - 2 * x) ** 5
r13 = -10 * (3 - 2 * x) ** 4
verificar(13, "cadena en potencia", sp.expand(sp.diff(f13, x) - r13) == 0)

# 14. Cadena reiterada con seno y raíz.
f14 = sp.sin(sp.sqrt(2 * x + 1))
r14 = sp.cos(sp.sqrt(2 * x + 1)) / sp.sqrt(2 * x + 1)
verificar(14, "cadena con seno y raíz", sp.simplify(sp.diff(f14, x) - r14) == 0)

# 15. Cadena con exponencial.
f15 = sp.exp(x**2 - 3 * x)
r15 = (2 * x - 3) * sp.exp(x**2 - 3 * x)
verificar(15, "cadena con exponencial", sp.simplify(sp.diff(f15, x) - r15) == 0)

# 16. Cadena reiterada con logaritmo.
f16 = sp.log((x**2 + 1) ** 3)
r16 = 6 * x / (x**2 + 1)
verificar(16, "cadena con logaritmo", sp.simplify(sp.diff(f16, x) - r16) == 0)

# 17. Operaciones con valores de f, g y sus derivadas en x=2.
f_val, fp_val, g_val, gp_val = 1, -2, 3, 4
r17a = 5 * fp_val - 2 * gp_val
r17b = fp_val * g_val + f_val * gp_val
r17c = sp.Rational(fp_val * g_val - f_val * gp_val, g_val**2)
verificar(17, "datos de funciones derivables", (r17a, r17b, r17c) == (-18, -2, sp.Rational(-10, 9)))

# 18. Parámetro fijado por la pendiente de la tangente.
a = sp.symbols("a", real=True)
f18 = sp.sqrt(a * x + 4)
m18 = sp.diff(f18, x).subs(x, 0)
sol18 = sp.solve(sp.Eq(m18, sp.Rational(3, 4)), a)
verificar(18, "parámetro y recta tangente", sol18 == [3] and f18.subs({a: 3, x: 0}) == 2)

# 19. Diferenciabilidad de una función por tramos en x=1.
a19, b19 = sp.symbols("a19 b19", real=True)
continuidad19 = sp.Eq(1 + a19, b19 + 1)
derivadas19 = sp.Eq(2, b19)
sol19 = sp.solve([continuidad19, derivadas19], [a19, b19], dict=True)
verificar(19, "parámetros de diferenciabilidad", sol19 == [{a19: 2, b19: 2}])

# 20. Función tomada de un control anterior, restringida al temario actual.
f20 = (x**2 - 3) / (x - 2)
r20 = (x**2 - 4 * x + 3) / (x - 2) ** 2
m20 = sp.diff(f20, x).subs(x, 3)
recta20 = sp.expand(m20 * (x - 3) + f20.subs(x, 3))
verificar(
    20,
    "cociente y recta tangente de control anterior",
    sp.simplify(sp.diff(f20, x) - r20) == 0 and m20 == 0 and recta20 == 6,
)

# 21. Potencias con exponentes enteros y fraccionarios.
f21 = x**5 - 2 / x + 3 * sp.sqrt(x)
r21 = 5 * x**4 + 2 / x**2 + sp.Rational(3, 2) / sp.sqrt(x)
verificar(21, "potencias enteras y fraccionarias", sp.simplify(sp.diff(f21, x) - r21) == 0)

# 22. Producto polinómico-trigonométrico.
f22 = (2 * x**2 - 3 * x + 1) * sp.sin(x)
r22 = (4 * x - 3) * sp.sin(x) + (2 * x**2 - 3 * x + 1) * sp.cos(x)
verificar(22, "producto polinómico-trigonométrico", sp.simplify(sp.diff(f22, x) - r22) == 0)

# 23. Cociente con exponencial.
f23 = (sp.exp(x) + 1) / (x - 1)
r23 = (sp.exp(x) * (x - 2) - 1) / (x - 1) ** 2
verificar(23, "cociente con exponencial", sp.simplify(sp.diff(f23, x) - r23) == 0)

# 24. Derivada de 1/x mediante la definición.
f24 = 1 / x
limite24 = sp.limit((f24.subs(x, x + h) - f24) / h, h, 0)
verificar(24, "definición para el recíproco", sp.simplify(limite24 + 1 / x**2) == 0)

# 25. Derivada de sqrt(x) mediante la definición.
f25 = sp.sqrt(x)
limite25 = sp.limit((f25.subs(x, x + h) - f25) / h, h, 0)
verificar(25, "definición para la raíz cuadrada", sp.simplify(limite25 - 1 / (2 * sp.sqrt(x))) == 0)

# 26. No diferenciabilidad de |2x+1| en -1/2.
c = sp.Rational(-1, 2)
cociente26 = sp.Abs(2 * (c + h) + 1) / h
lim26_izq = sp.limit(cociente26, h, 0, dir="-")
lim26_der = sp.limit(cociente26, h, 0, dir="+")
verificar(26, "límites laterales de un valor absoluto trasladado", lim26_izq == -2 and lim26_der == 2)

# 27. Tangente a sqrt(4x+5) en x=1.
f27 = sp.sqrt(4 * x + 5)
m27 = sp.diff(f27, x).subs(x, 1)
recta27 = sp.expand(m27 * (x - 1) + f27.subs(x, 1))
verificar(27, "tangente a una raíz compuesta", m27 == sp.Rational(2, 3) and recta27 == 2 * x / 3 + sp.Rational(7, 3))

# 28. Punto cuya tangente tiene pendiente dada.
f28 = x**2 - 2 * x + 3
sol28 = sp.solve(sp.Eq(sp.diff(f28, x), 4), x)
recta28 = sp.expand(4 * (x - 3) + f28.subs(x, 3))
verificar(28, "punto con pendiente prescrita", sol28 == [3] and recta28 == 4 * x - 6)

# 29. Potencia compuesta con exponente negativo.
f29 = (x**2 - x + 1) ** -7
r29 = -7 * (2 * x - 1) * (x**2 - x + 1) ** -8
verificar(29, "cadena con exponente negativo", sp.simplify(sp.diff(f29, x) - r29) == 0)

# 30. Potencia de una función coseno.
f30 = sp.cos(2 * x - 1) ** 3
r30 = -6 * sp.cos(2 * x - 1) ** 2 * sp.sin(2 * x - 1)
verificar(30, "cadena trigonométrica reiterada", sp.simplify(sp.diff(f30, x) - r30) == 0)

# 31. Raíz de un polinomio.
f31 = sp.sqrt(3 * x**2 + x + 2)
r31 = (6 * x + 1) / (2 * sp.sqrt(3 * x**2 + x + 2))
verificar(31, "cadena con raíz de polinomio", sp.simplify(sp.diff(f31, x) - r31) == 0)

# 32. Logaritmo de un cociente.
f32 = sp.log((2 * x - 1) / (x + 3))
r32 = 7 / ((2 * x - 1) * (x + 3))
verificar(32, "logaritmo de cociente", sp.simplify(sp.diff(f32, x) - r32) == 0)

# 33. Exponencial de una raíz.
f33 = sp.exp(sp.sqrt(x + 1))
r33 = sp.exp(sp.sqrt(x + 1)) / (2 * sp.sqrt(x + 1))
verificar(33, "exponencial de raíz", sp.simplify(sp.diff(f33, x) - r33) == 0)

# 34. Producto con exponencial compuesta.
f34 = sp.sin(x) * sp.exp(x**2 + 1)
r34 = sp.exp(x**2 + 1) * (sp.cos(x) + 2 * x * sp.sin(x))
verificar(34, "producto y cadena", sp.simplify(sp.diff(f34, x) - r34) == 0)

# 35. Derivada de una composición a partir de datos.
fp3, gm1, gpm1 = -4, 3, 5
verificar(35, "datos para derivada de composición", fp3 * gpm1 == -20 and gm1 == 3)

# 36. Parámetro determinado por una pendiente.
a36 = sp.symbols("a36", real=True)
f36 = (a36 * x - 1) ** 4
m36 = sp.diff(f36, x).subs(x, 0)
sol36 = sp.solve(sp.Eq(m36, 8), a36)
recta36 = 8 * x + f36.subs({a36: -2, x: 0})
verificar(36, "parámetro en potencia compuesta", sol36 == [-2] and recta36 == 8 * x + 1)

# 37. Diferenciabilidad de una función por tramos en x=0.
a37, b37 = sp.symbols("a37 b37", real=True)
sol37 = sp.solve([sp.Eq(b37, 1), sp.Eq(a37, 1)], [a37, b37], dict=True)
verificar(37, "parámetros para diferenciabilidad en cero", sol37 == [{a37: 1, b37: 1}])

# 38. Dos puntos con una misma pendiente.
f38 = x / (x + 1)
sol38 = sp.solve(sp.Eq(sp.diff(f38, x), sp.Rational(1, 4)), x)
recta38a = sp.expand(sp.Rational(1, 4) * (x - 1) + f38.subs(x, 1))
recta38b = sp.expand(sp.Rational(1, 4) * (x + 3) + f38.subs(x, -3))
verificar(
    38,
    "puntos y tangentes con pendiente prescrita",
    sol38 == [-3, 1]
    and recta38a == x / 4 + sp.Rational(1, 4)
    and recta38b == x / 4 + sp.Rational(9, 4),
)

# 39. Cociente dentro de una potencia.
f39 = ((x**2 + 1) / (x - 1)) ** 3
r39 = 3 * (x**2 + 1) ** 2 * (x**2 - 2 * x - 1) / (x - 1) ** 4
verificar(39, "cociente dentro de una potencia", sp.simplify(sp.diff(f39, x) - r39) == 0)

# 40. Producto con potencia compuesta y su tangente.
f40 = (2 * x - 1) ** 4 * sp.exp(x)
r40 = sp.exp(x) * (2 * x - 1) ** 3 * (2 * x + 7)
m40 = sp.diff(f40, x).subs(x, 0)
recta40 = sp.expand(m40 * x + f40.subs(x, 0))
verificar(40, "problema integrado de derivada y tangente", sp.simplify(sp.diff(f40, x) - r40) == 0 and m40 == -7 and recta40 == 1 - 7 * x)

print("\n40/40 verificaciones aprobadas.")
