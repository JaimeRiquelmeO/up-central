from __future__ import annotations

from fractions import Fraction


def close(actual: float, expected: float, tolerance: float = 0.005) -> bool:
    return abs(actual - expected) <= tolerance


def assert_value(key: str, actual: Fraction | float, expected: float, unit: str) -> None:
    actual_float = float(actual)
    if not close(actual_float, expected):
        raise AssertionError(f"{key}: esperado {expected} {unit}, obtenido {actual_float:.8f} {unit}")
    print(f"{key}: {actual_float:.2f} {unit}")


def main() -> None:
    # Ejercicio 1
    v1 = Fraction(54_000, 3_600)
    assert_value("1a", Fraction(1_200, 1) / v1, 80.00, "s")
    assert_value("1b", v1 * 35, 525.00, "m")

    # Ejercicio 2: 1.6t = 480 - 1.2(t - 60)
    t2 = Fraction(480, 1) + Fraction(12, 10) * 60
    t2 /= Fraction(16, 10) + Fraction(12, 10)
    assert_value("2a", t2, 197.14, "s")
    assert_value("2b", Fraction(16, 10) * t2, 315.43, "m")

    # Ejercicio 3: x(t)=120+2.5t
    assert_value("3a", Fraction(120, 1), 120.00, "m")
    assert_value("3b", Fraction(25, 10), 2.50, "m/s")
    assert_value("3c", Fraction(620 - 120, 1) / Fraction(25, 10), 200.00, "s")
    assert_value("3d", Fraction(120, 1) + Fraction(25, 10) * 90, 345.00, "m")

    # Ejercicio 4
    same_direction = Fraction(8, 10) + Fraction(14, 10)
    opposite_direction = Fraction(14, 10) - Fraction(8, 10)
    assert_value("4a", same_direction, 2.20, "m/s")
    assert_value("4b", opposite_direction, 0.60, "m/s")
    assert_value("4c", Fraction(132, 1) / same_direction, 60.00, "s")
    assert_value("4d", Fraction(132, 1) / opposite_direction, 220.00, "s")

    # Ejercicio 5
    v5 = Fraction(72_000, 3_600)
    assert_value("5a", v5 * 6, 120.00, "m")
    assert_value("5b", Fraction(14_500 - 14_400, 1) / v5, 5.00, "s")
    # En 6 s llega a 14520 m, por lo que cruza el portico en t=5 s.
    assert_value("5c_posicion_final", Fraction(14_400, 1) + v5 * 6, 14_520.00, "m")

    # Ejercicio 6: 0.18t = 0.30(t - 45)
    t6 = Fraction(30, 100) * 45 / (Fraction(30, 100) - Fraction(18, 100))
    x6 = Fraction(18, 100) * t6
    assert_value("6a", t6, 112.50, "s")
    assert_value("6b", x6, 20.25, "m")
    assert_value("6c", Fraction(36, 1) - x6, 15.75, "m")

    # Ejercicio 7: 1.5t = 1800 - 5t
    t7 = Fraction(1_800, 1) / (Fraction(15, 10) + 5)
    assert_value("7a", t7, 276.92, "s")
    assert_value("7b", Fraction(15, 10) * t7, 415.38, "m")

    # Ejercicio 8
    v8_a = Fraction(90 - 30, 20 - 0)
    v8_b = Fraction(180 - 90, 50 - 20)
    if v8_a != v8_b:
        raise AssertionError("8a: las pendientes no coinciden, no seria MRU")
    print("8a: compatible con MRU")
    assert_value("8b", v8_a, 3.00, "m/s")
    assert_value("8c", Fraction(30, 1) + v8_a * 75, 255.00, "m")
    assert_value("8d", Fraction(300 - 30, 1) / v8_a, 90.00, "s")

    # Ejercicio 9
    t9 = Fraction(420, 1) / Fraction(14, 10)
    t9 += Fraction(300, 1) / 2
    t9 += Fraction(180, 1) / Fraction(12, 10)
    d9 = Fraction(420 + 300 + 180, 1)
    assert_value("9a", t9, 600.00, "s")
    assert_value("9b", d9, 900.00, "m")
    assert_value("9c", d9 / t9, 1.50, "m/s")

    print("\nOK: segunda validacion independiente completada.")


if __name__ == "__main__":
    main()
