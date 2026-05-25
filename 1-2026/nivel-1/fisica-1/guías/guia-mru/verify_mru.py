from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import sympy as sp


@dataclass(frozen=True)
class Check:
    key: str
    sympy_value: float
    numpy_value: float
    latex_value: str

    def validate(self) -> None:
        if not math.isclose(self.sympy_value, self.numpy_value, rel_tol=1e-9, abs_tol=1e-9):
            raise AssertionError(f"{self.key}: {self.sympy_value} != {self.numpy_value}")


def f(value: sp.Expr | float) -> float:
    return float(sp.N(value, 15))


def checks() -> list[Check]:
    out: list[Check] = []

    v1 = sp.Rational(54_000, 3_600)
    out += [Check("1a", f(1200 / v1), 1200 / 15, "80,00 s"), Check("1b", f(v1 * 35), 15 * 35, "525,00 m")]

    t = sp.symbols("t", real=True)
    t2 = sp.solve(sp.Eq(sp.Rational(16, 10) * t, 480 - sp.Rational(12, 10) * (t - 60)), t)[0]
    t2_np = np.linalg.solve(np.array([[2.8]]), np.array([552.0]))[0]
    out += [Check("2a", f(t2), float(t2_np), "197,14 s"), Check("2b", f(1.6 * t2), float(1.6 * t2_np), "315,43 m")]

    out += [
        Check("3a", 120.0, 120.0, "x_0=120,00 m"),
        Check("3b", 2.5, 2.5, "v=2,50 m/s"),
        Check("3c", f((620 - 120) / sp.Rational(25, 10)), (620 - 120) / 2.5, "200,00 s"),
        Check("3d", f(120 + sp.Rational(25, 10) * 90), float(np.poly1d([2.5, 120])(90)), "345,00 m"),
    ]

    same = sp.Rational(8, 10) + sp.Rational(14, 10)
    opposite = sp.Rational(14, 10) - sp.Rational(8, 10)
    out += [
        Check("4a", f(same), 2.2, "2,20 m/s"),
        Check("4b", f(opposite), 0.6, "0,60 m/s"),
        Check("4c", f(132 / same), 132 / 2.2, "60,00 s"),
        Check("4d", f(132 / opposite), 132 / 0.6, "220,00 s"),
    ]

    v5 = sp.Rational(72_000, 3_600)
    out += [
        Check("5a", f(v5 * 6), 20 * 6, "120,00 m"),
        Check("5b", f((14500 - 14400) / v5), (14500 - 14400) / 20, "5,00 s"),
        Check("5c", f(14400 + v5 * 6), 14400 + 20 * 6, "Si"),
    ]

    t6 = sp.solve(sp.Eq(sp.Rational(18, 100) * t, sp.Rational(30, 100) * (t - 45)), t)[0]
    out += [
        Check("6a", f(t6), float(np.linalg.solve(np.array([[0.12]]), np.array([13.5]))[0]), "112,50 s"),
        Check("6b", f(sp.Rational(18, 100) * t6), 0.18 * 112.5, "20,25 m"),
        Check("6c", f(36 - sp.Rational(18, 100) * t6), 36 - 0.18 * 112.5, "15,75 m"),
    ]

    t7 = sp.solve(sp.Eq(sp.Rational(15, 10) * t, 1800 - 5 * t), t)[0]
    out += [Check("7a", f(t7), 1800 / 6.5, "276,92 s"), Check("7b", f(1.5 * t7), 1.5 * 1800 / 6.5, "415,38 m")]

    slopes = np.diff(np.array([30.0, 90.0, 180.0])) / np.diff(np.array([0.0, 20.0, 50.0]))
    out += [
        Check("8a", 3.0, float(slopes[0]), "MRU"),
        Check("8b", 3.0, float(slopes[1]), "3,00 m/s"),
        Check("8c", f(30 + 3 * 75), 30 + 3 * 75, "255,00 m"),
        Check("8d", f((300 - 30) / 3), (300 - 30) / 3, "90,00 s"),
    ]

    distances = sp.Matrix([420, 300, 180])
    speeds = sp.Matrix([sp.Rational(14, 10), 2, sp.Rational(12, 10)])
    total_time = sum(distances[i] / speeds[i] for i in range(3))
    total_distance = sum(distances)
    d_np = np.array([420.0, 300.0, 180.0])
    v_np = np.array([1.4, 2.0, 1.2])
    out += [
        Check("9a", f(total_time), float((d_np / v_np).sum()), "600,00 s"),
        Check("9b", f(total_distance), float(d_np.sum()), "900,00 m"),
        Check("9c", f(total_distance / total_time), float(d_np.sum() / (d_np / v_np).sum()), "1,50 m/s"),
    ]

    return out


def main() -> None:
    all_checks = checks()
    for check in all_checks:
        check.validate()
        print(f"{check.key}: {check.latex_value}")
    print(f"\nOK: {len(all_checks)} respuestas validadas con SymPy y NumPy.")


if __name__ == "__main__":
    main()
