"""Base obligatoria para validar todos los resultados de una guía.

Este archivo es interno y su contenido no debe mencionarse en el PDF.
Reemplace las pruebas de ejemplo por una prueba para cada identificador E1, E2...
"""

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable
import math
import re

import numpy as np
import sympy as sp


@dataclass
class Resultado:
    ejercicio: str
    metodo_exacto: bool
    metodo_independiente: bool
    detalle: str

    @property
    def aprobado(self) -> bool:
        return self.metodo_exacto and self.metodo_independiente


resultados: list[Resultado] = []


def registrar(ejercicio: str, exacto: bool, independiente: bool, detalle: str) -> None:
    """Registra dos comprobaciones distintas para un resultado visible."""
    resultados.append(Resultado(ejercicio, bool(exacto), bool(independiente), detalle))


def casi_igual(a, b, tolerancia=1e-10) -> bool:
    return bool(np.isclose(float(a), float(b), rtol=tolerancia, atol=tolerancia))


def validar_que_no_haya_marcadores() -> None:
    fuente = Path("main.tex").read_text(encoding="utf-8")
    prohibidos = ["PENDIENTE", "pendiente", "Resultado pendiente", "Enunciado pendiente"]
    encontrados = [texto for texto in prohibidos if texto in fuente]
    if encontrados:
        raise AssertionError(f"Quedan marcadores sin completar en main.tex: {encontrados}")


def ids_visibles() -> set[str]:
    fuente = Path("main.tex").read_text(encoding="utf-8")
    return set(re.findall(r"\[E\d+(?:[a-z])?\]", fuente))


# ---------------------------------------------------------------------------
# EJEMPLO DE IMPLEMENTACION - ELIMINAR AL CREAR LA GUIA REAL
# ---------------------------------------------------------------------------
def pruebas_de_la_guia() -> None:
    # Ejemplo: si E1 pide sumar 1/3 + 1/6 y la respuesta visible es 1/2.
    # Método 1: aritmética racional exacta.
    exacto = Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)
    # Método 2: comprobación numérica independiente con NumPy.
    independiente = casi_igual(np.float64(1/3) + np.float64(1/6), 0.5)
    # registrar("E1", exacto, independiente, "1/3 + 1/6 = 1/2")

    # Agregue registrar(...) para TODOS los ejercicios y subítems.
    # Para cálculo simbólico use SymPy; para ecuaciones sustituya cada raíz;
    # para estadística compare fórmula y simulación; para geometría verifique
    # relaciones exactas y coordenadas numéricas; para demostraciones compruebe
    # identidades simbólicas y una muestra amplia dentro del dominio.


def finalizar() -> None:
    validar_que_no_haya_marcadores()
    pruebas_de_la_guia()

    visibles = ids_visibles()
    probados = {f"[{r.ejercicio}]" for r in resultados}
    faltantes = visibles - probados
    extras = probados - visibles
    duplicados = sorted({r.ejercicio for r in resultados if sum(x.ejercicio == r.ejercicio for x in resultados) > 1})

    if faltantes:
        raise AssertionError(f"Resultados visibles sin prueba: {sorted(faltantes)}")
    if extras:
        raise AssertionError(f"Pruebas sin ejercicio visible: {sorted(extras)}")
    if duplicados:
        raise AssertionError(f"Identificadores duplicados: {duplicados}")
    if not resultados:
        raise AssertionError("No se registró ninguna validación")

    fallidos = [r for r in resultados if not r.aprobado]
    for r in resultados:
        estado = "PASS" if r.aprobado else "FAIL"
        print(f"{estado:4} {r.ejercicio}: {r.detalle}")
    if fallidos:
        raise AssertionError(f"Fallaron {len(fallidos)} validaciones")

    print(f"OK: {len(resultados)} resultados validados con dos métodos independientes.")


if __name__ == "__main__":
    finalizar()
