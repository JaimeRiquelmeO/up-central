"""Validación cruzada de los resultados de la Guía 2.

Los valores se calculan de forma independiente con SciPy/NumPy, mpmath y
SymPy. Además se comprueban simbólicamente las identidades de los estimadores.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import special, stats


TOL = 2e-9


def grouped_quantile_numpy(bounds: np.ndarray, freq: np.ndarray, p: float) -> float:
    target = p * freq.sum()
    cumulative = np.cumsum(freq)
    index = int(np.searchsorted(cumulative, target, side="left"))
    previous = cumulative[index - 1] if index else 0.0
    return float(bounds[index, 0] + (target - previous) / freq[index] * np.diff(bounds[index])[0])


def scipy_numpy_results() -> dict[str, float]:
    sample = np.array([0.12, 0.25, 0.08, 0.35, 0.18])
    theta = -sample.size / np.log1p(-sample).sum() - 1

    bounds5 = np.array([[10, 15], [15, 20], [20, 25], [25, 30], [30, 35]], dtype=float)
    freq5 = np.array([6, 12, 18, 9, 5], dtype=float)
    q1_5 = grouped_quantile_numpy(bounds5, freq5, 0.25)
    q3_5 = grouped_quantile_numpy(bounds5, freq5, 0.75)
    ri5 = q3_5 - q1_5
    between5 = (12 * 2.5 / 5 + 18 + 9 * 3 / 5) / 50
    p80 = grouped_quantile_numpy(bounds5, freq5, 0.80)

    bounds7 = np.array([[40, 50], [50, 60], [60, 70], [70, 80], [80, 90]], dtype=float)
    freq7 = np.array([4, 10, 20, 11, 5], dtype=float)

    bounds8 = np.array([[100, 120], [120, 140], [140, 160], [160, 180], [180, 200]], dtype=float)
    freq8 = np.array([8, 15, 22, 11, 4], dtype=float)
    q1_8 = grouped_quantile_numpy(bounds8, freq8, 0.25)
    q3_8 = grouped_quantile_numpy(bounds8, freq8, 0.75)
    ri8 = q3_8 - q1_8

    n = 36
    sx = 518.4
    sx2 = 7532.16
    mean = sx / n
    s2 = (sx2 - sx**2 / n) / (n - 1)
    tcrit = stats.t.ppf(0.995, n - 1)
    mean_margin = tcrit * math.sqrt(s2 / n)
    var_low = (n - 1) * s2 / stats.chi2.ppf(0.975, n - 1)
    var_high = (n - 1) * s2 / stats.chi2.ppf(0.025, n - 1)

    z95 = stats.norm.ppf(0.975)
    z99 = stats.norm.ppf(0.995)
    n_raw = (z95 * 11.84 / 2.5) ** 2
    error99 = z99 * 11.84 / math.sqrt(50)

    phat = 18 / 50
    prop_margin = z95 * math.sqrt(phat * (1 - phat) / 50)

    var_b = 6.2**2
    var_b_low = 49 * var_b / stats.chi2.ppf(0.95, 49)
    var_b_high = 49 * var_b / stats.chi2.ppf(0.05, 49)

    return {
        "bias_coef_n5": math.exp(special.gammaln(5.5) - special.gammaln(5)) / math.sqrt(5),
        "2b_theta": float(theta),
        "5_q1": q1_5,
        "5_q3": q3_5,
        "5_ri": ri5,
        "5_pct": between5,
        "6_low": q1_5 - 1.5 * ri5,
        "6_high": q3_5 + 1.5 * ri5,
        "6_p80": p80,
        "7_q1": grouped_quantile_numpy(bounds7, freq7, 0.25),
        "7_me": grouped_quantile_numpy(bounds7, freq7, 0.50),
        "7_q3": grouped_quantile_numpy(bounds7, freq7, 0.75),
        "7_pct": (10 * 5 / 10 + 20 + 11 * 6 / 10) / 50,
        "8_q1": q1_8,
        "8_q3": q3_8,
        "8_ri": ri8,
        "8_low": q1_8 - 1.5 * ri8,
        "8_high": q3_8 + 1.5 * ri8,
        "9_mean": mean,
        "9_s2": s2,
        "9_mean_low": mean - mean_margin,
        "9_mean_high": mean + mean_margin,
        "9_var_low": var_low,
        "9_var_high": var_high,
        "10_n_raw": n_raw,
        "10_error99": error99,
        "11_prop_low": phat - prop_margin,
        "11_prop_high": phat + prop_margin,
        "12_cv_a": 12.4 / 145.2 * 100,
        "12_cv_b": 6.2 / 88.6 * 100,
        "12_var_low": var_b_low,
        "12_var_high": var_b_high,
    }


def mp_bisect_cdf(cdf, p: mp.mpf, low: mp.mpf, high: mp.mpf) -> mp.mpf:
    for _ in range(250):
        middle = (low + high) / 2
        if cdf(middle) < p:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def mp_t_ppf(p: mp.mpf, dof: int) -> mp.mpf:
    def cdf(x):
        z = dof / (dof + x**2)
        tail = mp.betainc(mp.mpf(dof) / 2, mp.mpf("0.5"), 0, z, regularized=True) / 2
        return 1 - tail if x >= 0 else tail

    return mp_bisect_cdf(cdf, p, mp.mpf(-20), mp.mpf(20))


def mp_chi2_ppf(p: mp.mpf, dof: int) -> mp.mpf:
    cdf = lambda x: mp.gammainc(mp.mpf(dof) / 2, 0, x / 2, regularized=True)
    return mp_bisect_cdf(cdf, p, mp.mpf(0), mp.mpf(200))


def grouped_quantile_mp(bounds, freq, p):
    target = p * sum(freq)
    previous = mp.mpf(0)
    for (low, high), count in zip(bounds, freq):
        if target <= previous + count:
            return low + (target - previous) / count * (high - low)
        previous += count
    raise ValueError("Percentil fuera del rango")


def mpmath_results() -> dict[str, float]:
    mp.mp.dps = 60
    sample = [mp.mpf(".12"), mp.mpf(".25"), mp.mpf(".08"), mp.mpf(".35"), mp.mpf(".18")]
    theta = -len(sample) / sum(mp.log(1 - x) for x in sample) - 1
    b5 = [(mp.mpf(a), mp.mpf(b)) for a, b in [(10, 15), (15, 20), (20, 25), (25, 30), (30, 35)]]
    f5 = list(map(mp.mpf, [6, 12, 18, 9, 5]))
    q1_5 = grouped_quantile_mp(b5, f5, mp.mpf(".25"))
    q3_5 = grouped_quantile_mp(b5, f5, mp.mpf(".75"))
    ri5 = q3_5 - q1_5
    b7 = [(mp.mpf(a), mp.mpf(b)) for a, b in [(40, 50), (50, 60), (60, 70), (70, 80), (80, 90)]]
    f7 = list(map(mp.mpf, [4, 10, 20, 11, 5]))
    b8 = [(mp.mpf(a), mp.mpf(b)) for a, b in [(100, 120), (120, 140), (140, 160), (160, 180), (180, 200)]]
    f8 = list(map(mp.mpf, [8, 15, 22, 11, 4]))
    q1_8 = grouped_quantile_mp(b8, f8, mp.mpf(".25"))
    q3_8 = grouped_quantile_mp(b8, f8, mp.mpf(".75"))
    ri8 = q3_8 - q1_8

    n = mp.mpf(36)
    mean = mp.mpf("518.4") / n
    s2 = (mp.mpf("7532.16") - mp.mpf("518.4") ** 2 / n) / 35
    tcrit = mp_t_ppf(mp.mpf(".995"), 35)
    margin = tcrit * mp.sqrt(s2 / n)
    chi975 = mp_chi2_ppf(mp.mpf(".975"), 35)
    chi025 = mp_chi2_ppf(mp.mpf(".025"), 35)
    z95 = mp.sqrt(2) * mp.erfinv(mp.mpf(".95"))
    z99 = mp.sqrt(2) * mp.erfinv(mp.mpf(".99"))
    phat = mp.mpf(18) / 50
    pmargin = z95 * mp.sqrt(phat * (1 - phat) / 50)
    chi49_95 = mp_chi2_ppf(mp.mpf(".95"), 49)
    chi49_05 = mp_chi2_ppf(mp.mpf(".05"), 49)

    result = {
        "bias_coef_n5": mp.gamma(mp.mpf("5.5")) / (mp.sqrt(5) * mp.gamma(5)),
        "2b_theta": theta,
        "5_q1": q1_5,
        "5_q3": q3_5,
        "5_ri": ri5,
        "5_pct": (mp.mpf(6) + 18 + mp.mpf("5.4")) / 50,
        "6_low": q1_5 - mp.mpf("1.5") * ri5,
        "6_high": q3_5 + mp.mpf("1.5") * ri5,
        "6_p80": grouped_quantile_mp(b5, f5, mp.mpf(".8")),
        "7_q1": grouped_quantile_mp(b7, f7, mp.mpf(".25")),
        "7_me": grouped_quantile_mp(b7, f7, mp.mpf(".5")),
        "7_q3": grouped_quantile_mp(b7, f7, mp.mpf(".75")),
        "7_pct": (mp.mpf(5) + 20 + mp.mpf("6.6")) / 50,
        "8_q1": q1_8,
        "8_q3": q3_8,
        "8_ri": ri8,
        "8_low": q1_8 - mp.mpf("1.5") * ri8,
        "8_high": q3_8 + mp.mpf("1.5") * ri8,
        "9_mean": mean,
        "9_s2": s2,
        "9_mean_low": mean - margin,
        "9_mean_high": mean + margin,
        "9_var_low": 35 * s2 / chi975,
        "9_var_high": 35 * s2 / chi025,
        "10_n_raw": (z95 * mp.mpf("11.84") / mp.mpf("2.5")) ** 2,
        "10_error99": z99 * mp.mpf("11.84") / mp.sqrt(50),
        "11_prop_low": phat - pmargin,
        "11_prop_high": phat + pmargin,
        "12_cv_a": mp.mpf("12.4") / mp.mpf("145.2") * 100,
        "12_cv_b": mp.mpf("6.2") / mp.mpf("88.6") * 100,
        "12_var_low": 49 * mp.mpf("6.2") ** 2 / chi49_95,
        "12_var_high": 49 * mp.mpf("6.2") ** 2 / chi49_05,
    }
    return {key: float(value) for key, value in result.items()}


def sp_t_ppf(p: sp.Expr, dof: int, guess: float) -> sp.Expr:
    x = sp.symbols("x", positive=True)
    z = sp.Rational(dof, 1) / (dof + x**2)
    cdf = 1 - sp.betainc(sp.Rational(dof, 2), sp.Rational(1, 2), 0, z) / (2 * sp.beta(sp.Rational(dof, 2), sp.Rational(1, 2)))
    return sp.nsolve(cdf - p, x, guess, tol=sp.Float("1e-50"), maxsteps=100)


def sp_chi2_ppf(p: sp.Expr, dof: int, guess: float) -> sp.Expr:
    x = sp.symbols("x", positive=True)
    cdf = sp.lowergamma(sp.Rational(dof, 2), x / 2) / sp.gamma(sp.Rational(dof, 2))
    return sp.nsolve(cdf - p, x, guess, tol=sp.Float("1e-50"), maxsteps=100)


def grouped_quantile_sp(bounds, freq, p):
    target = p * sum(freq)
    previous = sp.Integer(0)
    for (low, high), count in zip(bounds, freq):
        if bool(target <= previous + count):
            return low + (target - previous) / count * (high - low)
        previous += count
    raise ValueError("Percentil fuera del rango")


def sympy_results() -> dict[str, float]:
    sample = [sp.Rational(12, 100), sp.Rational(25, 100), sp.Rational(8, 100), sp.Rational(35, 100), sp.Rational(18, 100)]
    theta = -sp.Integer(5) / sum(sp.log(1 - value) for value in sample) - 1
    b5 = [(sp.Integer(a), sp.Integer(b)) for a, b in [(10, 15), (15, 20), (20, 25), (25, 30), (30, 35)]]
    f5 = list(map(sp.Integer, [6, 12, 18, 9, 5]))
    q1_5 = grouped_quantile_sp(b5, f5, sp.Rational(1, 4))
    q3_5 = grouped_quantile_sp(b5, f5, sp.Rational(3, 4))
    ri5 = q3_5 - q1_5
    b7 = [(sp.Integer(a), sp.Integer(b)) for a, b in [(40, 50), (50, 60), (60, 70), (70, 80), (80, 90)]]
    f7 = list(map(sp.Integer, [4, 10, 20, 11, 5]))
    b8 = [(sp.Integer(a), sp.Integer(b)) for a, b in [(100, 120), (120, 140), (140, 160), (160, 180), (180, 200)]]
    f8 = list(map(sp.Integer, [8, 15, 22, 11, 4]))
    q1_8 = grouped_quantile_sp(b8, f8, sp.Rational(1, 4))
    q3_8 = grouped_quantile_sp(b8, f8, sp.Rational(3, 4))
    ri8 = q3_8 - q1_8

    mean = sp.Rational(5184, 10) / 36
    s2 = (sp.Rational(753216, 100) - sp.Rational(5184, 10) ** 2 / 36) / 35
    tcrit = sp_t_ppf(sp.Rational(995, 1000), 35, 2.7)
    margin = tcrit * sp.sqrt(s2 / 36)
    chi975 = sp_chi2_ppf(sp.Rational(975, 1000), 35, 55)
    chi025 = sp_chi2_ppf(sp.Rational(25, 1000), 35, 20)
    z95 = sp.sqrt(2) * sp.erfinv(sp.Rational(95, 100))
    z99 = sp.sqrt(2) * sp.erfinv(sp.Rational(99, 100))
    phat = sp.Rational(18, 50)
    pmargin = z95 * sp.sqrt(phat * (1 - phat) / 50)
    chi49_95 = sp_chi2_ppf(sp.Rational(95, 100), 49, 66)
    chi49_05 = sp_chi2_ppf(sp.Rational(5, 100), 49, 34)

    result = {
        "bias_coef_n5": sp.gamma(sp.Rational(11, 2)) / (sp.sqrt(5) * sp.gamma(5)),
        "2b_theta": theta,
        "5_q1": q1_5,
        "5_q3": q3_5,
        "5_ri": ri5,
        "5_pct": sp.Rational(294, 500),
        "6_low": q1_5 - sp.Rational(3, 2) * ri5,
        "6_high": q3_5 + sp.Rational(3, 2) * ri5,
        "6_p80": grouped_quantile_sp(b5, f5, sp.Rational(4, 5)),
        "7_q1": grouped_quantile_sp(b7, f7, sp.Rational(1, 4)),
        "7_me": grouped_quantile_sp(b7, f7, sp.Rational(1, 2)),
        "7_q3": grouped_quantile_sp(b7, f7, sp.Rational(3, 4)),
        "7_pct": sp.Rational(316, 500),
        "8_q1": q1_8,
        "8_q3": q3_8,
        "8_ri": ri8,
        "8_low": q1_8 - sp.Rational(3, 2) * ri8,
        "8_high": q3_8 + sp.Rational(3, 2) * ri8,
        "9_mean": mean,
        "9_s2": s2,
        "9_mean_low": mean - margin,
        "9_mean_high": mean + margin,
        "9_var_low": 35 * s2 / chi975,
        "9_var_high": 35 * s2 / chi025,
        "10_n_raw": (z95 * sp.Rational(1184, 100) / sp.Rational(25, 10)) ** 2,
        "10_error99": z99 * sp.Rational(1184, 100) / sp.sqrt(50),
        "11_prop_low": phat - pmargin,
        "11_prop_high": phat + pmargin,
        "12_cv_a": sp.Rational(124, 10) / sp.Rational(1452, 10) * 100,
        "12_cv_b": sp.Rational(62, 10) / sp.Rational(886, 10) * 100,
        "12_var_low": 49 * sp.Rational(62, 10) ** 2 / chi49_95,
        "12_var_high": 49 * sp.Rational(62, 10) ** 2 / chi49_05,
    }
    return {key: float(sp.N(value, 18)) for key, value in result.items()}


def symbolic_checks() -> None:
    n = sp.symbols("n", integer=True, positive=True)
    theta = sp.symbols("theta", positive=True)
    sum_x2 = sp.symbols("S", positive=True)
    loglik1 = -2 * n * sp.log(theta) - sum_x2 / theta**2
    assert sp.solve(sp.diff(loglik1, theta), theta) == [sp.sqrt(sum_x2 / n)]
    assert sp.simplify((theta**2 * n) / n - theta**2) == 0

    i = sp.symbols("i", integer=True, positive=True)
    assert sp.simplify(sp.summation(2 * i / (n * (n + 1)), (i, 1, n))) == 1
    var3 = sp.summation((2 * i / (n * (n + 1))) ** 2, (i, 1, n))
    assert sp.simplify(var3 - 2 * (2 * n + 1) / (3 * n * (n + 1))) == 0

    lam, xbar = sp.symbols("lambda xbar", positive=True)
    score_per_obs = xbar / lam - 1 - 1 / (sp.exp(lam) - 1)
    implicit = xbar - lam / (1 - sp.exp(-lam))
    assert sp.simplify(score_per_obs * lam - implicit) == 0


def main() -> None:
    symbolic_checks()
    backends = {
        "SciPy/NumPy": scipy_numpy_results(),
        "mpmath": mpmath_results(),
        "SymPy": sympy_results(),
    }
    keys = list(backends["SciPy/NumPy"])
    print(f"{'resultado':<18} {'SciPy/NumPy':>15} {'mpmath':>15} {'SymPy':>15} {'dif. max.':>12}")
    for key in keys:
        values = [backends[name][key] for name in backends]
        spread = max(values) - min(values)
        if spread > TOL:
            raise AssertionError(f"{key}: desacuerdo entre bibliotecas: {values}")
        print(f"{key:<18} {values[0]:15.10f} {values[1]:15.10f} {values[2]:15.10f} {spread:12.2e}")

    assert math.ceil(backends["SciPy/NumPy"]["10_n_raw"]) == 87
    assert backends["SciPy/NumPy"]["11_prop_high"] > 0.25
    assert backends["SciPy/NumPy"]["12_cv_b"] < backends["SciPy/NumPy"]["12_cv_a"]
    assert backends["SciPy/NumPy"]["12_var_high"] > 50
    print(f"\nOK: {len(keys)} resultados numéricos coinciden en tres bibliotecas.")
    print("OK: identidades simbólicas de los ejercicios 1, 3 y 4 verificadas.")


if __name__ == "__main__":
    main()
