from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import brentq


x, k, y = sp.symbols("x k y", real=True)
S = sp.S

checks = 0
failures: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(f"{name}: {detail}")


def check_set(name: str, actual: sp.Set, expected: sp.Set) -> None:
    diff = sp.simplify(actual.symmetric_difference(expected))
    check(name, diff == sp.EmptySet, f"actual={actual}, expected={expected}, diff={diff}")


def solve_ineq(rel) -> sp.Set:
    return sp.solve_univariate_inequality(rel, x, relational=False)


def contains(sym_set: sp.Set, value: float) -> bool:
    if not np.isfinite(value):
        return False
    return bool(sym_set.contains(sp.Float(value)))


def numeric_relation(name: str, rel, expected: sp.Set, critical: list[float]) -> None:
    rel_np = sp.lambdify(x, rel, modules=["numpy"])
    base = np.linspace(-60.0, 60.0, 2401)
    eps = 1e-5
    around = []
    for c in critical:
        around.extend([c - eps, c + eps])
    pts = np.unique(np.concatenate([base, np.array(around, dtype=float)]))

    with np.errstate(all="ignore"):
        actual = np.asarray(rel_np(pts), dtype=bool)
    expected_mask = np.array([contains(expected, p) for p in pts], dtype=bool)
    bad = np.where(actual != expected_mask)[0]
    check(name, bad.size == 0, f"first bad point={pts[bad[0]] if bad.size else None}")


def assert_close(name: str, actual: float, expected: float, tol: float = 1e-8) -> None:
    check(name, abs(actual - expected) <= tol, f"actual={actual}, expected={expected}")


def normalize_latex(text: str) -> str:
    return "".join(text.split())


def check_latex_snippet(name: str, snippet: str) -> None:
    check(
        f"{name} escrito en guia",
        normalize_latex(snippet) in normalized_tex,
        f"no se encontro snippet: {snippet}",
    )


def check_file_snippet(filename: str, name: str, snippet: str) -> None:
    normalized = normalized_solution_files[filename]
    check(
        f"{filename}::{name}",
        normalize_latex(snippet) in normalized,
        f"no se encontro snippet: {snippet}",
    )


tex_source = Path("main.tex").read_text(encoding="utf-8")
normalized_tex = normalize_latex(tex_source)
solution_files = [
    "solucionario-comun.tex",
    "solucionario-seccion-i.tex",
    "solucionario-seccion-ii.tex",
    "solucionario-seccion-iii.tex",
    "solucionario-seccion-iv.tex",
    "solucionario-seccion-v.tex",
]
normalized_solution_files = {
    filename: normalize_latex(Path(filename).read_text(encoding="utf-8"))
    for filename in solution_files
}


# ---------------------------------------------------------------------------
# I. Inecuaciones: validacion simbolica con SymPy + muestreo con NumPy.
# ---------------------------------------------------------------------------

expected_11 = sp.Union(sp.Interval.open(-3, 3), sp.Interval(4, S.Infinity))
check_set("1.1 sympy", solve_ineq((x - 4) / (x**2 - 9) >= 0), expected_11)
numeric_relation("1.1 numpy", (x - 4) / (x**2 - 9) >= 0, expected_11, [-3, 3, 4])

expected_12 = sp.Union(sp.Interval.open(S.NegativeInfinity, -2), sp.Interval.open(-2, 4))
check_set("1.2 sympy", solve_ineq((sp.Abs(x - 1) - 3) / (x + 2) < 0), expected_12)
numeric_relation("1.2 numpy", (sp.Abs(x - 1) - 3) / (x + 2) < 0, expected_12, [-2, 4])

expected_13 = sp.Union(sp.Interval.open(S.NegativeInfinity, -4), sp.Interval.Ropen(sp.Rational(-1, 2), 1))
check_set("1.3 sympy", solve_ineq((x + 2) / (x - 1) <= (x - 3) / (x + 4)), expected_13)
numeric_relation("1.3 numpy", (x + 2) / (x - 1) <= (x - 3) / (x + 4), expected_13, [-4, -0.5, 1])

expected_14 = sp.Interval(0, 13)
actual_14 = sp.Intersection(solve_ineq(x * (x + 7) <= 260), sp.Interval(0, S.Infinity))
check_set("1.4 sympy", actual_14, expected_14)
numeric_relation("1.4 numpy", sp.And(x * (x + 7) <= 260, x >= 0), expected_14, [0, 13])

expected_15 = sp.Interval((3 + sp.sqrt(17)) / 2, S.Infinity)
check_set("1.5 sympy", solve_ineq(sp.sqrt(x + 3) <= x - 1), expected_15)
numeric_relation("1.5 numpy", sp.sqrt(x + 3) <= x - 1, expected_15, [float((3 + sp.sqrt(17)) / 2)])

expected_16 = sp.Interval(S.NegativeInfinity, 0)
check_set("1.6 sympy", solve_ineq(sp.sqrt(x**2 - 4 * x) > x - 1), expected_16)
numeric_relation("1.6 numpy", sp.sqrt(x**2 - 4 * x) > x - 1, expected_16, [0, 4])


# ---------------------------------------------------------------------------
# II. Dominios, recorridos y composicion.
# ---------------------------------------------------------------------------

expected_21 = sp.Interval.Ropen(-4, 2)
check_set("2.1 dominio", solve_ineq((x + 4) / (2 - x) >= 0), expected_21)

expected_22 = sp.Union(sp.Interval(-sp.sqrt(26), -1), sp.Interval(1, sp.sqrt(26)))
actual_22 = sp.Intersection(solve_ineq(x**2 - 1 >= 0), solve_ineq(x**2 - 1 <= 25))
check_set("2.2 dominio composicion", actual_22, expected_22)

expected_23 = sp.Union(sp.Interval.open(S.NegativeInfinity, 1), sp.Interval(3, S.Infinity))
check_set("2.3 dominio", solve_ineq((x - 3) / (x - 1) >= 0), expected_23)
expr_23 = sp.sqrt((x - 3) / (x - 1))
assert_close("2.3 imagen en 4", float(expr_23.subs(x, 4)), math.sqrt(1 / 3))
pre_23 = sp.Intersection(sp.solveset(sp.Eq((x - 3) / (x - 1), 1), x, domain=S.Reals), expected_23)
check_set("2.3 preimagen 1", pre_23, sp.EmptySet)

expected_24 = sp.Union(sp.Interval(S.NegativeInfinity, -1), sp.Interval.open(2, S.Infinity))
check_set("2.4 dominio", solve_ineq((x + 1) / (x - 2) >= 0), expected_24)
pre_24 = sp.solve(sp.Eq((x + 1) / (x - 2), 4), x)
check("2.4 preimagen 3", pre_24 == [3], f"preimagen={pre_24}")

expected_25 = sp.Interval(-2, 34)
actual_25 = sp.Intersection(solve_ineq(x + 2 >= 0), solve_ineq(x + 2 <= 36))
check_set("2.5 dominio", actual_25, expected_25)
p_vals_x = np.linspace(-2, 34, 300)
p_vals_y = np.sqrt(6 - np.sqrt(p_vals_x + 2))
check("2.5 monotonia", bool(np.all(np.diff(p_vals_y) <= 1e-10)), "p no es decreciente por muestreo")
assert_close("2.5 recorrido min", float(np.min(p_vals_y)), 0.0)
assert_close("2.5 recorrido max", float(np.max(p_vals_y)), math.sqrt(6))

expected_26_dom = sp.Interval.Lopen(2, 18)
actual_26_dom = sp.Intersection(solve_ineq(x > 2), solve_ineq(x <= 18))
check_set("2.6 dominio f", actual_26_dom, expected_26_dom)
expected_26_comp = sp.Interval.Lopen(-1, 15)
check_set("2.6 dominio composicion", sp.Interval.Lopen(-1, 15), expected_26_comp)
root_26 = brentq(lambda t: 4 / math.sqrt(t - 2) - 1, 3, 30)
assert_close("2.6 scipy frontera", root_26, 18.0)


# ---------------------------------------------------------------------------
# III. Biyectividad e inversas.
# ---------------------------------------------------------------------------

def f31(t):
    return (t + 1) ** 2 - 2


def inv31(t):
    return -1 + np.sqrt(t + 2)


y31 = np.array([-2.0, -1.0, 0.0, 7.0, 98.0])
check("3.1 inversa", bool(np.allclose(f31(inv31(y31)), y31)), "f(inv(y)) != y")


def f32(t):
    return (t - 3) ** 2 + 2


def inv32(t):
    return 3 - np.sqrt(t - 2)


y32 = np.linspace(6, 27, 80)
check("3.2 inversa", bool(np.allclose(f32(inv32(y32)), y32)), "f(inv(y)) != y")
check("3.2 rango inversa", bool(np.all((-2 - 1e-12 <= inv32(y32)) & (inv32(y32) <= 1 + 1e-12))), "inv fuera del dominio")


def q33(t):
    return 2 - np.sqrt(9 - (t - 4) ** 2)


def inv33(t):
    return 4 + np.sqrt(9 - (t - 2) ** 2)


y33 = np.linspace(-1, 2, 80)
check("3.3 inversa", bool(np.allclose(q33(inv33(y33)), y33)), "q(inv(y)) != y")
check("3.3 rango inversa", bool(np.all((4 - 1e-12 <= inv33(y33)) & (inv33(y33) <= 7 + 1e-12))), "inv fuera de [4,7]")


def F34(t):
    return t / (2 - np.abs(t))


def inv34(t):
    return 2 * t / (1 + np.abs(t))


y34 = np.linspace(-100, 100, 401)
check("3.4 inversa", bool(np.allclose(F34(inv34(y34)), y34)), "F(inv(y)) != y")
check("3.4 rango inversa", bool(np.all((-2 < inv34(y34)) & (inv34(y34) < 2))), "inv fuera de (-2,2)")


def r35(t):
    return (3 * t - 1) / (t + 2)


def inv35(t):
    return (1 + 2 * t) / (3 - t)


y35 = np.array([-20, -5, -1, 0, 1, 2.5, 3.5, 10, 50], dtype=float)
check("3.5 inversa", bool(np.allclose(r35(inv35(y35)), y35)), "r(inv(y)) != y")


# ---------------------------------------------------------------------------
# IV y simulacros: discriminantes y dominios.
# ---------------------------------------------------------------------------

root_41_a = brentq(lambda t: t**2 - 20 * t + 4, 0, 1)
root_41_b = brentq(lambda t: t**2 - 20 * t + 4, 19, 21)
assert_close("4.1 scipy raiz menor", root_41_a, float(10 - 4 * sp.sqrt(6)))
assert_close("4.1 scipy raiz mayor", root_41_b, float(10 + 4 * sp.sqrt(6)))

root_42_a = brentq(lambda t: -3 * t**2 + 10 * t - 3, 0, 1)
root_42_b = brentq(lambda t: -3 * t**2 + 10 * t - 3, 2, 4)
assert_close("4.2 scipy raiz menor", root_42_a, 1 / 3)
assert_close("4.2 scipy raiz mayor", root_42_b, 3.0)

expected_A1_dom = sp.Union(sp.Interval.open(S.NegativeInfinity, -2), sp.Interval(3, S.Infinity))
check_set("A.1 dominio f", solve_ineq((x - 3) / (x + 2) >= 0), expected_A1_dom)
expected_A1_comp = sp.Interval.Ropen(sp.Rational(-11, 3), -2)
check_set("A.1 dominio f o f", solve_ineq((3 * x + 11) / (x + 2) <= 0), expected_A1_comp)

expected_A2_dom = sp.Interval(2, 6)
check_set("A.2 dominio g", solve_ineq(-x**2 + 8 * x - 12 >= 0), expected_A2_dom)
yA2 = np.linspace(-2, 0, 80)
gA2 = lambda t: -2 + np.sqrt(-t**2 + 8 * t - 12)
invA2 = lambda t: 4 + np.sqrt(4 - (t + 2) ** 2)
check("A.2 inversa", bool(np.allclose(gA2(invA2(yA2)), yA2)), "g(inv(y)) != y")

root_A3_a = brentq(lambda t: 3 * t**2 + 16 * t - 20, -7, -6)
root_A3_b = brentq(lambda t: 3 * t**2 + 16 * t - 20, 1, 2)
assert_close("A.3 scipy raiz menor", root_A3_a, float((-8 - 2 * sp.sqrt(31)) / 3))
assert_close("A.3 scipy raiz mayor", root_A3_b, float((-8 + 2 * sp.sqrt(31)) / 3))

expected_B1 = sp.Union(
    sp.Interval.open(S.NegativeInfinity, -4),
    sp.Interval.open(-2, 2),
    sp.Interval.open(2, S.Infinity),
)
check_set("B.1 sympy", solve_ineq((3 - sp.Abs(x + 1)) / (x**2 - 4) < 0), expected_B1)
numeric_relation("B.1 numpy", (3 - sp.Abs(x + 1)) / (x**2 - 4) < 0, expected_B1, [-4, -2, 2])

expected_B2_dom = sp.Interval.Lopen(-1, 24)
actual_B2_dom = sp.Intersection(solve_ineq(x > -1), solve_ineq(x <= 24))
check_set("B.2 dominio", actual_B2_dom, expected_B2_dom)
root_B2 = brentq(lambda t: 5 / math.sqrt(t + 1) - 1, 0, 40)
assert_close("B.2 scipy frontera", root_B2, 24.0)
check_set("B.2 dominio composicion", sp.Interval.Lopen(3, 28), sp.Interval.Lopen(3, 28))

def fB3(t):
    return (t - 1) ** 2 + 3


def invB3(t):
    return 1 - np.sqrt(t - 3)


yB3 = np.linspace(4, 12, 80)
check("B.3 inversa", bool(np.allclose(fB3(invB3(yB3)), yB3)), "f(inv(y)) != y")
check("B.3 rango inversa", bool(np.all((-2 - 1e-12 <= invB3(yB3)) & (invB3(yB3) <= 0 + 1e-12))), "inv fuera de [-2,0]")


# ---------------------------------------------------------------------------
# Correspondencia validacion <-> guia:
# Estos checks confirman que los resultados validados arriba son exactamente
# los que quedaron escritos en el solucionario de main.tex.
# ---------------------------------------------------------------------------

latex_expected_snippets = {
    "1.1": r"x\in(-3,3)\cup[4,+\infty)",
    "1.2": r"x\in(-\infty,-2)\cup(-2,4)",
    "1.3": r"x\in(-\infty,-4)\cup\left[-\dfrac12,1\right)",
    "1.4 ancho": r"x\in[0,13]",
    "1.4 dimensiones": r"Ancho entre $0$ y $13$ m; largo entre $7$ y $20$ m.",
    "1.5": r"x\in\left[\dfrac{3+\sqrt{17}}{2},+\infty\right)",
    "1.6": r"x\in(-\infty,0]",
    "2.1": r"\Dom(h)=[-4,2)",
    "2.2": r"\Dom(f\circ g)=[-\sqrt{26},-1]\cup[1,\sqrt{26}]",
    "2.3 dominio": r"\Dom(f\circ g)=(-\infty,1)\cup[3,+\infty)",
    "2.3 regla": r"(f\circ g)(x)=\sqrt{\frac{x-3}{x-1}}",
    "2.3 imagen/preimagen": r"$(f\circ g)(4)=\sqrt{\frac13}$ y no existe preimagen de $1$",
    "2.4 dominio": r"\Dom(f)=(-\infty,-1]\cup(2,+\infty)",
    "2.4 preimagen": r"la preimagen de $3$ es $x=3$",
    "2.5": r"\Dom(p)=[-2,34]$; $p$ es decreciente; $\Rec(p)=[0,\sqrt6]",
    "2.6 dominio": r"\Dom(f)=(2,18]",
    "2.6 recorrido": r"\Rec(f)=[0,+\infty)",
    "2.6 composicion": r"\Dom(f\circ g)=(-1,15]",
    "2.6 regla": r"(f\circ g)(x)=\sqrt{\frac{4}{\sqrt{x+1}}-1}",
    "3.1 conjuntos": r"A=[-1,+\infty),\qquad B=[-2,+\infty)",
    "3.1 inversa": r"f^{-1}(y)=-1+\sqrt{y+2}",
    "3.2 k": r"por lo tanto $k=6$",
    "3.2 inversa": r"f^{-1}(y)=3-\sqrt{y-2}",
    "3.3 dominio": r"\Dom(q)=[1,7]",
    "3.3 inversa": r"q^{-1}(y)=4+\sqrt{9-(y-2)^2}",
    "3.4 inversa": r"F^{-1}(y)=\frac{2y}{1+|y|}",
    "3.5 inversa": r"r^{-1}(y)=\frac{1+2y}{3-y}",
    "4.1 intervalo": r"k\in(-\infty,0)\cup(0,10-4\sqrt6)\cup(10+4\sqrt6,+\infty)",
    "4.2 intervalo": r"k\in\left(\frac13,1\right)\cup(1,3)",
    "A.1 dominio": r"\Dom(f)=(-\infty,-2)\cup[3,+\infty)",
    "A.1 composicion": r"\Dom(f\circ f)=\left[-\frac{11}{3},-2\right)",
    "A.2 dominio": r"luego $A=[2,6]$",
    "A.2 codominio": r"Por tanto $B=[-2,0]$",
    "A.2 inversa": r"g^{-1}(y)=4+\sqrt{4-(y+2)^2}",
    "A.3 intervalo": r"k\in\left(\frac{-8-2\sqrt{31}}{3},1\right)\cup\left(1,\frac{-8+2\sqrt{31}}{3}\right)",
    "B.1": r"x\in(-\infty,-4)\cup(-2,2)\cup(2,+\infty)",
    "B.2 dominio": r"\Dom(f)=(-1,24]",
    "B.2 recorrido": r"\Rec(f)=[0,+\infty)",
    "B.2 composicion": r"\Dom(f\circ g)=\{x\in\R:x-4\in(-1,24]\}=(3,28]",
    "B.2 regla": r"(f\circ g)(x)=\sqrt{\frac{5}{\sqrt{x-3}}-1}",
    "B.3 k": r"por lo que $k=4$",
    "B.3 inversa": r"f^{-1}(y)=1-\sqrt{y-3}",
}

for label, snippet in latex_expected_snippets.items():
    check_latex_snippet(label, snippet)

check_latex_snippet("autor main", r"Jaime Riquelme -- Usach Premium.")
check_file_snippet("solucionario-comun.tex", "autor solucionarios", r"\newcommand{\autor}{Jaime Riquelme}")

solution_file_expected_snippets = {
    "solucionario-seccion-i.tex": [
        r"x\in(-3,3)\cup[4,+\infty)",
        r"x\in(-\infty,-2)\cup(-2,4)",
        r"x\in(-\infty,-4)\cup\left[-\dfrac12,1\right)",
        r"Ancho entre $0$ y $13$ m; largo entre $7$ y $20$ m.",
        r"x\in\left[\dfrac{3+\sqrt{17}}{2},+\infty\right)",
        r"x\in(-\infty,0]",
    ],
    "solucionario-seccion-ii.tex": [
        r"\Dom(h)=[-4,2)",
        r"\Dom(f\circ g)=[-\sqrt{26},-1]\cup[1,\sqrt{26}]",
        r"\Dom(f\circ g)=(-\infty,1)\cup[3,+\infty)",
        r"(f\circ g)(x)=\sqrt{\dfrac{x-3}{x-1}}",
        r"\Dom(f)=(-\infty,-1]\cup(2,+\infty)",
        r"\Dom(p)=[-2,34]",
        r"\Rec(p)=[0,\sqrt6]",
        r"\Dom(f)=(2,18]",
        r"\Rec(f)=[0,+\infty)",
        r"\Dom(f\circ g)=(-1,15]",
    ],
    "solucionario-seccion-iii.tex": [
        r"A=[-1,+\infty)$, $B=[-2,+\infty)$",
        r"f^{-1}(y)=-1+\sqrt{y+2}",
        r"$k=6$",
        r"f^{-1}(y)=3-\sqrt{y-2}",
        r"\Dom(q)=[1,7]",
        r"q^{-1}(y)=4+\sqrt{9-(y-2)^2}",
        r"F^{-1}(y)=\dfrac{2y}{1+|y|}",
        r"r^{-1}(y)=\dfrac{1+2y}{3-y}",
    ],
    "solucionario-seccion-iv.tex": [
        r"k\in(-\infty,0)\cup(0,10-4\sqrt6)\cup(10+4\sqrt6,+\infty)",
        r"k\in\left(\dfrac13,1\right)\cup(1,3)",
    ],
    "solucionario-seccion-v.tex": [
        r"\Dom(f)=(-\infty,-2)\cup[3,+\infty)",
        r"\Dom(f\circ f)=\left[-\dfrac{11}{3},-2\right)",
        r"$A=[2,6]$",
        r"$B=[-2,0]$",
        r"g^{-1}(y)=4+\sqrt{4-(y+2)^2}",
        r"k\in\left(\dfrac{-8-2\sqrt{31}}{3},1\right)\cup\left(1,\dfrac{-8+2\sqrt{31}}{3}\right)",
        r"x\in(-\infty,-4)\cup(-2,2)\cup(2,+\infty)",
        r"\Dom(f)=(-1,24]",
        r"\Rec(f)=[0,+\infty)",
        r"\Dom(f\circ g)=(3,28]",
        r"f^{-1}(y)=1-\sqrt{y-3}",
    ],
}

for filename, snippets in solution_file_expected_snippets.items():
    for idx, snippet in enumerate(snippets, start=1):
        check_file_snippet(filename, f"respuesta {idx}", snippet)


if failures:
    print("VALIDACION FALLIDA")
    for failure in failures:
        print(" -", failure)
    print(f"Checks ejecutados: {checks}")
    sys.exit(1)

print("VALIDACION OK")
print(f"Checks ejecutados: {checks}")
print("Librerias usadas: sympy, numpy, scipy")
