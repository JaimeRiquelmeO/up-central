"""Validación simbólica de la Guía de preparación - Taller.

Ejecutar con:
    python validar_resultados.py

El script comprueba, en orden, los resultados de los 18 ejercicios.
"""

from __future__ import annotations

import sympy as sp


def verificar(numero: int, descripcion: str, condicion: bool) -> None:
    """Registra una comprobación o detiene la ejecución si falla."""
    if not bool(condicion):
        raise AssertionError(f"Ejercicio {numero}: falló {descripcion}")
    print(f"[OK] {numero:02d} - {descripcion}")


x, t = sp.symbols("x t", real=True)

# 1. Sustitución directa.
resultado_1 = sp.limit((x**2 + 3 * x - 1) / (x + 1), x, 2)
verificar(1, "límite por sustitución", resultado_1 == 3)

# 2. Factorización.
resultado_2 = sp.limit((x**2 - 9) / (x - 3), x, 3)
verificar(2, "límite por factorización", resultado_2 == 6)

# 3. Racionalización.
resultado_3 = sp.limit((sp.sqrt(x) - 2) / (x - 4), x, 4)
verificar(3, "límite por racionalización", resultado_3 == sp.Rational(1, 4))

# 4. Límite trigonométrico fundamental.
resultado_4 = sp.limit(sp.sin(5 * x) / x, x, 0)
verificar(4, "límite trigonométrico", resultado_4 == 5)

# 5. Comportamiento al infinito.
resultado_5 = sp.limit((3 * x**2 - x + 4) / (2 * x**2 + 5), x, sp.oo)
verificar(5, "límite al infinito", resultado_5 == sp.Rational(3, 2))

# 6. Continuidad de una función por tramos.
a, c = sp.symbols("a c", real=True)
tramo_izquierdo = (sp.sqrt(3 * x + 1) - 2) / (x - 1)
tramo_derecho = a * (sp.sqrt(x + 3) - 2) / (x - 1)
limite_izquierdo = sp.limit(tramo_izquierdo, x, 1, dir="-")
limite_derecho = sp.limit(tramo_derecho, x, 1, dir="+")
solucion_continuidad = sp.solve(
    [sp.Eq(limite_izquierdo, c), sp.Eq(limite_derecho, c)],
    [a, c],
    dict=True,
)
verificar(
    6,
    "parámetros de continuidad",
    limite_izquierdo == sp.Rational(3, 4)
    and limite_derecho == a / 4
    and solucion_continuidad
    == [{a: 3, c: sp.Rational(3, 4)}],
)

# 7. f(x)=2 sen(3x)-1.
f_7 = 2 * sp.sin(3 * x) - 1
periodo_7 = 2 * sp.pi / 3
verificar(
    7,
    "amplitud, período y recorrido del seno",
    sp.simplify(f_7.subs(x, x + periodo_7) - f_7) == 0
    and f_7.subs(x, sp.pi / 6) == 1
    and f_7.subs(x, sp.pi / 2) == -3,
)

# 8. g(x)=-3 cos(x/2)+2.
g_8 = -3 * sp.cos(x / 2) + 2
periodo_8 = 4 * sp.pi
verificar(
    8,
    "amplitud, período y recorrido del coseno",
    sp.simplify(g_8.subs(x, x + periodo_8) - g_8) == 0
    and g_8.subs(x, 0) == -1
    and g_8.subs(x, 2 * sp.pi) == 5,
)

# 9. sen(x)=-sqrt(3)/2 en [0,2pi).
dominio_vuelta = sp.Interval.Ropen(0, 2 * sp.pi)
solucion_9 = sp.solveset(
    sp.Eq(sp.sin(x), -sp.sqrt(3) / 2), x, domain=dominio_vuelta
)
esperada_9 = sp.FiniteSet(4 * sp.pi / 3, 5 * sp.pi / 3)
verificar(9, "ecuación de seno", solucion_9 == esperada_9)

# 10. 2cos^2(x)+3cos(x)+1=0 en [0,2pi).
ecuacion_10 = 2 * sp.cos(x) ** 2 + 3 * sp.cos(x) + 1
solucion_10 = sp.solveset(sp.Eq(ecuacion_10, 0), x, domain=dominio_vuelta)
esperada_10 = sp.FiniteSet(2 * sp.pi / 3, sp.pi, 4 * sp.pi / 3)
verificar(10, "ecuación cuadrática en coseno", solucion_10 == esperada_10)

# 11. Ángulo agudo: sen(alpha)=(1+cos(alpha))/2.
s, q = sp.symbols("s q", real=True)
candidatos_11 = sp.solve(
    [sp.Eq(s, (1 + q) / 2), sp.Eq(s**2 + q**2, 1)], [s, q], dict=True
)
candidatos_agudos = [
    sol
    for sol in candidatos_11
    if bool(sol[s] > 0) and bool(sol[q] > 0)
]
verificar(
    11,
    "identidad con ángulo agudo",
    candidatos_agudos == [{q: sp.Rational(3, 5), s: sp.Rational(4, 5)}],
)

# 12. h(t)=5+4sen(pi*t/6).
h_12 = 5 + 4 * sp.sin(sp.pi * t / 6)
criticos_12 = sp.solveset(
    sp.Eq(sp.diff(h_12, t), 0), t, domain=sp.Interval(0, 12)
)
verificar(
    12,
    "modelo periódico",
    sp.simplify(h_12.subs(t, t + 12) - h_12) == 0
    and criticos_12 == sp.FiniteSet(3, 9)
    and h_12.subs(t, 3) == 9
    and h_12.subs(t, 9) == 1,
)

# 13. log_2(32)+log_3(1/9).
resultado_13 = sp.log(32, 2) + sp.log(sp.Rational(1, 9), 3)
verificar(13, "evaluación de logaritmos", sp.simplify(resultado_13) == 3)

# 14. 3^(2x-1)=27.
solucion_14 = sp.solve(sp.Eq(3 ** (2 * x - 1), 27), x)
verificar(14, "ecuación exponencial con igual base", solucion_14 == [2])

# 15. log_2(x-1)+log_2(x-3)=3.
raices_15 = sp.solve(sp.Eq((x - 1) * (x - 3), 8), x)
solucion_15 = [raiz for raiz in raices_15 if bool(raiz > 3)]
verificar(
    15,
    "ecuación logarítmica y restricción de dominio",
    raices_15 == [-1, 5] and solucion_15 == [5],
)

# 16. 2e^x-5=0.
solucion_16 = sp.solve(sp.Eq(2 * sp.exp(x) - 5, 0), x)
verificar(
    16,
    "ecuación exponencial con logaritmo natural",
    solucion_16 == [sp.log(sp.Rational(5, 2))],
)

# 17. f(x)=ln(2x-4)+1.
f_17 = sp.log(2 * x - 4) + 1
cero_17 = 2 + 1 / (2 * sp.E)
y = sp.symbols("y", real=True)
inversa_17 = 2 + sp.exp(y - 1) / 2
verificar(
    17,
    "dominio, asíntota y cero de un logaritmo",
    sp.simplify(f_17.subs(x, cero_17)) == 0
    and sp.limit(f_17, x, 2, dir="+") == -sp.oo
    and (2 * cero_17 - 4) > 0
    and sp.simplify(f_17.subs(x, inversa_17) - y) == 0,
)

# 18. Modelo P(t)=A*2^(kt), P(0)=500 y P(6)=2000.
A, k = sp.symbols("A k", real=True)
modelo = A * 2 ** (k * t)
solucion_parametros = sp.solve(
    [sp.Eq(modelo.subs(t, 0), 500), sp.Eq(modelo.subs(t, 6), 2000)],
    [A, k],
    dict=True,
)
tiempo_objetivo = 3 * sp.log(10, 2)
modelo_final = 500 * 2 ** (t / 3)
verificar(
    18,
    "modelo exponencial y despeje logarítmico",
    solucion_parametros == [{A: 500, k: sp.Rational(1, 3)}]
    and sp.simplify(modelo_final.subs(t, tiempo_objetivo) - 5000) == 0
    and abs(float(sp.N(tiempo_objetivo)) - 9.965784284662087) < 1e-12,
)

print("\n18/18 verificaciones aprobadas.")
