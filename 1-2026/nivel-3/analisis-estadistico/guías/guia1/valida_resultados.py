"""Valida los resultados de la guia con SciPy, mpmath y SymPy.

Cada backend calcula independientemente los mismos valores numericos. Las
identidades funcionales (densidades, marginales y CDF) se validan mediante
normalizacion, momentos y evaluaciones representativas.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import integrate, special, stats


TOL = 5e-11


def scipy_results() -> dict[str, float]:
    p_rechazo = stats.norm.cdf((976 - 1000) / 15)
    tabla = np.array(
        [
            [0.05, 0.08, 0.07, 0.05],
            [0.08, 0.12, 0.10, 0.05],
            [0.10, 0.15, 0.10, 0.05],
        ]
    )
    marginal_x = tabla.sum(axis=1)
    marginal_y = tabla.sum(axis=0)
    ex = float(np.dot(np.arange(3), marginal_x))
    ey = float(np.dot(np.arange(4), marginal_y))
    p15 = stats.norm.cdf(-1)

    dens3 = lambda x: 4 / x**5
    dens8 = lambda y, x: 6 / 5 * (x**2 + y)
    dens11 = lambda x: x - x**3 / 4

    return {
        "1a": p_rechazo,
        "1b": stats.binom.cdf(2, 12, p_rechazo),
        "2a": stats.poisson.sf(2, 6),
        "2b": stats.poisson.pmf(2, 1.5) / stats.poisson.sf(0, 1.5),
        "3_norm": integrate.quad(dens3, 1, np.inf)[0],
        "3_f_2": dens3(2),
        "3_media": integrate.quad(lambda x: x * dens3(x), 1, np.inf)[0],
        "3_var": integrate.quad(lambda x: x**2 * dens3(x), 1, np.inf)[0]
        - integrate.quad(lambda x: x * dens3(x), 1, np.inf)[0] ** 2,
        "4a": (1 - p_rechazo) ** 4 * p_rechazo,
        "4b": (1 - p_rechazo) ** 3,
        "5_norm": float(tabla.sum()),
        "5a": float(tabla[1:, :3].sum() / tabla[1:, :].sum()),
        "5b_ex": ex,
        "6a": stats.expon.cdf(0.5, scale=2),
        "6b": stats.expon.cdf(0.5, scale=2) ** 3,
        "7a": special.comb(9, 2) * 0.15**3 * 0.85**7,
        "7b": stats.binom.cdf(2, 5, 0.15),
        "8_norm": integrate.dblquad(dens8, 0, 1, 0, 1)[0],
        "8_fx_0_4": integrate.quad(lambda y: dens8(y, 0.4), 0, 1)[0],
        "8b": integrate.quad(lambda y: dens8(y, 0.4), 0.5, 1)[0]
        / integrate.quad(lambda y: dens8(y, 0.4), 0, 1)[0],
        "9a_ey": ey,
        "9b_ec": 200 * ex + 350 * ey + 50,
        "10a": stats.norm.cdf(1.8) - stats.norm.cdf(-1.8),
        "10b": 1 - (stats.norm.cdf(1.8) - stats.norm.cdf(-1.8)),
        "11_norm": integrate.quad(dens11, 0, 2)[0],
        "11_f_1_5": integrate.quad(dens11, 0, 1.5)[0],
        "11b": integrate.quad(dens11, 0.5, 1.5)[0]
        / integrate.quad(dens11, 0.5, 2)[0],
        "12_media": 120 + 80,
        "12_var": 9 + 16,
        "12b": stats.norm.cdf((195 - 200) / 5),
        "13a": stats.expon.cdf(6, scale=4) - stats.expon.cdf(2, scale=4),
        "13b": stats.expon.sf(7, scale=4) / stats.expon.sf(3, scale=4),
        "14a": stats.hypergeom.pmf(2, 40, 8, 6),
        "14b": stats.hypergeom.sf(1, 40, 8, 6),
        "15a_x": p15,
        "15a_y": p15,
        "15b": 1 - (1 - p15) ** 2,
        "16_k": 1 / integrate.dblquad(
            lambda y, x: np.exp(-0.2 * x - 0.4 * y), 0, np.inf, 0, np.inf
        )[0],
        "16_fx_1": integrate.quad(lambda y: 0.08 * np.exp(-0.2 - 0.4 * y), 0, np.inf)[0],
        "16_fy_1": integrate.quad(lambda x: 0.08 * np.exp(-0.2 * x - 0.4), 0, np.inf)[0],
        "16_factor_1_1": 0.2 * np.exp(-0.2) * 0.4 * np.exp(-0.4),
    }


def mpmath_results() -> dict[str, float]:
    mp.mp.dps = 50
    phi = lambda z: (1 + mp.erf(z / mp.sqrt(2))) / 2
    p_rechazo = phi(mp.mpf(-8) / 5)
    poisson = lambda k, lam: mp.e**(-lam) * lam**k / mp.factorial(k)
    tabla = [
        [mp.mpf(".05"), mp.mpf(".08"), mp.mpf(".07"), mp.mpf(".05")],
        [mp.mpf(".08"), mp.mpf(".12"), mp.mpf(".10"), mp.mpf(".05")],
        [mp.mpf(".10"), mp.mpf(".15"), mp.mpf(".10"), mp.mpf(".05")],
    ]
    mx = [sum(row) for row in tabla]
    my = [sum(tabla[i][j] for i in range(3)) for j in range(4)]
    ex = sum(i * mx[i] for i in range(3))
    ey = sum(j * my[j] for j in range(4))
    f11 = lambda x: x - x**3 / 4
    hyper = lambda x: mp.binomial(8, x) * mp.binomial(32, 6 - x) / mp.binomial(40, 6)
    p15 = phi(-1)

    result = {
        "1a": p_rechazo,
        "1b": sum(mp.binomial(12, k) * p_rechazo**k * (1 - p_rechazo) ** (12 - k) for k in range(3)),
        "2a": 1 - sum(poisson(k, 6) for k in range(3)),
        "2b": poisson(2, mp.mpf("1.5")) / (1 - poisson(0, mp.mpf("1.5"))),
        "3_norm": mp.quad(lambda x: 4 / x**5, [1, mp.inf]),
        "3_f_2": mp.mpf(4) / 2**5,
        "3_media": mp.quad(lambda x: 4 / x**4, [1, mp.inf]),
        "3_var": mp.quad(lambda x: 4 / x**3, [1, mp.inf])
        - mp.quad(lambda x: 4 / x**4, [1, mp.inf]) ** 2,
        "4a": (1 - p_rechazo) ** 4 * p_rechazo,
        "4b": (1 - p_rechazo) ** 3,
        "5_norm": sum(mx),
        "5a": sum(sum(tabla[i][j] for j in range(3)) for i in range(1, 3)) / sum(mx[1:]),
        "5b_ex": ex,
        "6a": 1 - mp.e ** (-mp.mpf(".25")),
        "6b": (1 - mp.e ** (-mp.mpf(".25"))) ** 3,
        "7a": mp.binomial(9, 2) * mp.mpf(".15") ** 3 * mp.mpf(".85") ** 7,
        "7b": sum(mp.binomial(5, k) * mp.mpf(".15") ** k * mp.mpf(".85") ** (5 - k) for k in range(3)),
        "8_norm": mp.quad(lambda x: mp.quad(lambda y: mp.mpf(6) / 5 * (x**2 + y), [0, 1]), [0, 1]),
        "8_fx_0_4": mp.quad(lambda y: mp.mpf(6) / 5 * (mp.mpf(".4") ** 2 + y), [0, 1]),
        "8b": mp.quad(lambda y: mp.mpf(6) / 5 * (mp.mpf(".4") ** 2 + y), [mp.mpf(".5"), 1])
        / mp.quad(lambda y: mp.mpf(6) / 5 * (mp.mpf(".4") ** 2 + y), [0, 1]),
        "9a_ey": ey,
        "9b_ec": 200 * ex + 350 * ey + 50,
        "10a": phi(mp.mpf("1.8")) - phi(mp.mpf("-1.8")),
        "10b": 1 - (phi(mp.mpf("1.8")) - phi(mp.mpf("-1.8"))),
        "11_norm": mp.quad(f11, [0, 2]),
        "11_f_1_5": mp.quad(f11, [0, mp.mpf("1.5")]),
        "11b": mp.quad(f11, [mp.mpf(".5"), mp.mpf("1.5")]) / mp.quad(f11, [mp.mpf(".5"), 2]),
        "12_media": 200,
        "12_var": 25,
        "12b": phi(-1),
        "13a": mp.e ** (-mp.mpf(".5")) - mp.e ** (-mp.mpf("1.5")),
        "13b": mp.e ** (-1),
        "14a": hyper(2),
        "14b": sum(hyper(k) for k in range(2, 7)),
        "15a_x": p15,
        "15a_y": p15,
        "15b": 1 - (1 - p15) ** 2,
        "16_k": 1 / mp.quad(lambda x: mp.quad(lambda y: mp.e ** (-mp.mpf(".2") * x - mp.mpf(".4") * y), [0, mp.inf]), [0, mp.inf]),
        "16_fx_1": mp.quad(lambda y: mp.mpf(".08") * mp.e ** (-mp.mpf(".2") - mp.mpf(".4") * y), [0, mp.inf]),
        "16_fy_1": mp.quad(lambda x: mp.mpf(".08") * mp.e ** (-mp.mpf(".2") * x - mp.mpf(".4")), [0, mp.inf]),
        "16_factor_1_1": mp.mpf(".2") * mp.e ** (-mp.mpf(".2")) * mp.mpf(".4") * mp.e ** (-mp.mpf(".4")),
    }
    return {key: float(value) for key, value in result.items()}


def sympy_results() -> dict[str, float]:
    x, y = sp.symbols("x y", positive=True)
    phi = lambda z: (1 + sp.erf(z / sp.sqrt(2))) / 2
    p_rechazo = phi(sp.Rational(-8, 5))
    poisson = lambda k, lam: sp.exp(-lam) * lam**k / sp.factorial(k)
    tabla = sp.Matrix(
        [
            [sp.Rational(5, 100), sp.Rational(8, 100), sp.Rational(7, 100), sp.Rational(5, 100)],
            [sp.Rational(8, 100), sp.Rational(12, 100), sp.Rational(10, 100), sp.Rational(5, 100)],
            [sp.Rational(10, 100), sp.Rational(15, 100), sp.Rational(10, 100), sp.Rational(5, 100)],
        ]
    )
    mx = [sum(tabla[i, j] for j in range(4)) for i in range(3)]
    my = [sum(tabla[i, j] for i in range(3)) for j in range(4)]
    ex = sum(i * mx[i] for i in range(3))
    ey = sum(j * my[j] for j in range(4))
    f11 = x - x**3 / 4
    hyper = lambda k: sp.binomial(8, k) * sp.binomial(32, 6 - k) / sp.binomial(40, 6)
    p15 = phi(-1)

    result = {
        "1a": p_rechazo,
        "1b": sum(sp.binomial(12, k) * p_rechazo**k * (1 - p_rechazo) ** (12 - k) for k in range(3)),
        "2a": 1 - sum(poisson(k, 6) for k in range(3)),
        "2b": poisson(2, sp.Rational(3, 2)) / (1 - poisson(0, sp.Rational(3, 2))),
        "3_norm": sp.integrate(4 / x**5, (x, 1, sp.oo)),
        "3_f_2": sp.Rational(1, 8),
        "3_media": sp.integrate(4 / x**4, (x, 1, sp.oo)),
        "3_var": sp.integrate(4 / x**3, (x, 1, sp.oo)) - sp.Rational(4, 3) ** 2,
        "4a": (1 - p_rechazo) ** 4 * p_rechazo,
        "4b": (1 - p_rechazo) ** 3,
        "5_norm": sum(mx),
        "5a": sum(sum(tabla[i, j] for j in range(3)) for i in range(1, 3)) / sum(mx[1:]),
        "5b_ex": ex,
        "6a": 1 - sp.exp(sp.Rational(-1, 4)),
        "6b": (1 - sp.exp(sp.Rational(-1, 4))) ** 3,
        "7a": sp.binomial(9, 2) * sp.Rational(15, 100) ** 3 * sp.Rational(85, 100) ** 7,
        "7b": sum(sp.binomial(5, k) * sp.Rational(15, 100) ** k * sp.Rational(85, 100) ** (5 - k) for k in range(3)),
        "8_norm": sp.integrate(sp.Rational(6, 5) * (x**2 + y), (x, 0, 1), (y, 0, 1)),
        "8_fx_0_4": sp.integrate(sp.Rational(6, 5) * (sp.Rational(2, 5) ** 2 + y), (y, 0, 1)),
        "8b": sp.integrate(sp.Rational(6, 5) * (sp.Rational(2, 5) ** 2 + y), (y, sp.Rational(1, 2), 1))
        / sp.integrate(sp.Rational(6, 5) * (sp.Rational(2, 5) ** 2 + y), (y, 0, 1)),
        "9a_ey": ey,
        "9b_ec": 200 * ex + 350 * ey + 50,
        "10a": phi(sp.Rational(9, 5)) - phi(sp.Rational(-9, 5)),
        "10b": 1 - (phi(sp.Rational(9, 5)) - phi(sp.Rational(-9, 5))),
        "11_norm": sp.integrate(f11, (x, 0, 2)),
        "11_f_1_5": sp.integrate(f11, (x, 0, sp.Rational(3, 2))),
        "11b": sp.integrate(f11, (x, sp.Rational(1, 2), sp.Rational(3, 2)))
        / sp.integrate(f11, (x, sp.Rational(1, 2), 2)),
        "12_media": 200,
        "12_var": 25,
        "12b": phi(-1),
        "13a": sp.exp(sp.Rational(-1, 2)) - sp.exp(sp.Rational(-3, 2)),
        "13b": sp.exp(-1),
        "14a": hyper(2),
        "14b": sum(hyper(k) for k in range(2, 7)),
        "15a_x": p15,
        "15a_y": p15,
        "15b": 1 - (1 - p15) ** 2,
        "16_k": 1 / sp.integrate(sp.exp(-sp.Rational(1, 5) * x - sp.Rational(2, 5) * y), (x, 0, sp.oo), (y, 0, sp.oo)),
        "16_fx_1": sp.integrate(sp.Rational(2, 25) * sp.exp(-sp.Rational(1, 5) - sp.Rational(2, 5) * y), (y, 0, sp.oo)),
        "16_fy_1": sp.integrate(sp.Rational(2, 25) * sp.exp(-sp.Rational(1, 5) * x - sp.Rational(2, 5)), (x, 0, sp.oo)),
        "16_factor_1_1": sp.Rational(1, 5) * sp.exp(-sp.Rational(1, 5)) * sp.Rational(2, 5) * sp.exp(-sp.Rational(2, 5)),
    }
    return {key: float(sp.N(value, 16)) for key, value in result.items()}


def main() -> None:
    backends = {
        "SciPy": scipy_results(),
        "mpmath": mpmath_results(),
        "SymPy": sympy_results(),
    }
    keys = list(backends["SciPy"])
    print(f"{'resultado':<18} {'SciPy':>15} {'mpmath':>15} {'SymPy':>15} {'dif. max.':>12}")
    for key in keys:
        values = [backends[name][key] for name in backends]
        spread = max(values) - min(values)
        if spread > TOL:
            raise AssertionError(f"{key}: desacuerdo entre bibliotecas: {values}")
        print(f"{key:<18} {values[0]:15.10f} {values[1]:15.10f} {values[2]:15.10f} {spread:12.2e}")
    print(f"\nOK: {len(keys)} comprobaciones coinciden con tolerancia {TOL:g}.")


if __name__ == "__main__":
    main()
