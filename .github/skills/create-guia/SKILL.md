---
name: create-guia
description: "Crear guías de ejercicios en LaTeX estilo Usach Premium para cualquier ramo (Cálculo, Álgebra, Física, Estadística, Programación, etc.). Solucionario con resultado final únicamente, sin paso a paso. OBLIGATORIO: validar CADA resultado del solucionario con Python (mínimo 2 librerías) antes de añadir al PDF."
argument-hint: "Describe la guía: asignatura, tema, número de ejercicios, nivel de dificultad y si existe un .tex base"
---

# Crear Guía LaTeX — Usach Premium

## Cuando Usar

- Crear nueva guía de ejercicios para **cualquier asignatura**
- Añadir ejercicios a una guía existente
- Completar o corregir un solucionario
- Generar PDF de guía de práctica o control

---

## REGLA FUNDAMENTAL — Validación Python

> **NUNCA** añadir un resultado al solucionario sin haberlo validado con Python usando **al menos 2 librerías independientes**.

- Si hay discrepancia entre librerías → recalcular → volver a validar → solo entonces añadir al `.tex`.
- Guardar el script de validación **junto al `.tex`** (mismo directorio) para referencia futura.
- El script debe imprimir `PASS/FAIL` por ejercicio y un resumen final `N/N PASS`.

---

## Procedimiento

### 1. Recopilar Información

Antes de escribir LaTeX, determinar:

- **Asignatura** — ¿de qué ramo es la guía?
- **Tema** — ¿qué subtema específico cubre?
- **Nivel del curso** — ¿primer año? ¿segundo? Esto define la profundidad esperada.
- **Número de ejercicios** — ~15 en total es ideal para una guía completa
- **Fuentes** — leer archivos en `Pruebas_Pasadas/` del repositorio para extraer patrones reales de PEP y controles del ramo
- **¿Existe `.tex` previo?** — si existe, extenderlo en lugar de crear uno nuevo

> **Importante**: Leer las pruebas anteriores antes de diseñar ejercicios. Esto garantiza que la guía sea representativa de lo que realmente se evalúa en ese ramo.

---

### 2. Diseñar los Ejercicios

Elegir ejercicios con **soluciones exactas y limpias**. Antes de comprometerse con un enunciado, verificar que la solución sea computacionalmente manejable.

#### Distribución recomendada para ~15 ejercicios

| Sección | # Ej | Nivel | Descripción |
|---------|-------|-------|-------------|
| I | 5 | 🟢 Básico | Concepto directo, aplicación inmediata |
| II | 5 | 🟡 Intermedio | Combinación de conceptos |
| III | 3 | 🔵 Avanzado | Demostración, parámetros, casos |
| IV | 2 | 🔴 PEP | Formato y dificultad de prueba real |

#### Regla de terminología en enunciados

**Usar lenguaje que describa lo que se busca**, no el nombre del concepto que el estudiante aún no domina:

| ❌ Evitar | ✅ Usar |
|-----------|---------|
| *Estudie la monotonía de f* | *Determina los intervalos donde f crece y donde decrece* |
| *Determine la biyectividad* | *¿La función es a la vez inyectiva y sobreyectiva? Justifique* |
| *Calcule el determinante por cofactores* | *Usando expansión por cofactores, calcule el determinante* |
| *Aplique el teorema de Bayes* | *Use probabilidad condicional para encontrar P(A\|B)* |
| *Demuestre la convergencia* | *¿La serie converge o diverge? Justifique con el criterio que corresponda* |

---

### 3. Elegir las Librerías de Validación según el Ramo

Seleccionar las 2 librerías más apropiadas al tipo de ejercicio:

| Tipo de ejercicio | Librería 1 (simbólica/exacta) | Librería 2 (numérica/verificación) |
|---|---|---|
| Álgebra, inecuaciones, funciones | `sympy` (`solveset`, `solve`, `diff`) | `numpy` (muestreo denso, máscaras) |
| Álgebra Lineal | `sympy` (`Matrix`, `det`, `eigenvects`) | `numpy.linalg` (`det`, `eig`, `solve`) |
| Estadística y Probabilidad | `scipy.stats` | `numpy` (simulación Monte Carlo) |
| Física / Ingeniería | `sympy` (`integrate`, `diff`) | `scipy.integrate` (`quad`, `odeint`) |
| Aritmética / Discreta | `sympy` (`factorint`, `isprime`) | `math` + verificación directa |
| Programación / Algoritmos | Implementación directa | Comparación con librería estándar |

---

### 4. Escribir el Script de Validación

Crear un archivo Python en la misma carpeta que el `.tex`. Estructura universal:

```python
"""
VALIDACIÓN — Guía de [TEMA] — [ASIGNATURA]
Librerías usadas: [Librería 1] + [Librería 2]
"""

# ── Importaciones según el ramo ───────────────────────────────
# Álgebra / Cálculo:
from sympy import *
import numpy as np, math

# Álgebra Lineal:
# from sympy import Matrix, det, eigenvects
# import numpy.linalg as la

# Estadística:
# from scipy import stats
# import numpy as np

# ─────────────────────────────────────────────────────────────
PASS = "✔ PASS"
FAIL = "✗ FAIL"
results = {}

def val(tag, ok_lib1, ok_lib2, solucion, detalle=""):
    """Registra y muestra el resultado de un test."""
    ok = ok_lib1 and ok_lib2
    results[tag] = ok
    print(f"  {'PASS' if ok else 'FAIL'}  [{tag}]  → {solucion}")
    if detalle:
        print(f"        ↳ {detalle}")

# ── Ejercicio 1 ────────────────────────────────────────────────
print("\n[Ej.1] Descripción breve del ejercicio")

# Librería 1
resultado_lib1 = ...   # resultado con librería simbólica/exacta
ok_lib1 = (resultado_lib1 == <valor esperado>)

# Librería 2
resultado_lib2 = ...   # resultado con librería numérica/alternativa
ok_lib2 = ...          # comparación (np.allclose, ==, etc.)

val("1", ok_lib1, ok_lib2, "<resultado final>",
    f"Lib1={resultado_lib1}, Lib2={resultado_lib2:.6f}")

# ... (repetir para cada ejercicio)

# ── Resumen final ──────────────────────────────────────────────
total  = len(results)
passed = sum(results.values())
print(f"\n{'═'*50}")
print(f"  RESULTADO: {passed}/{total} PASS")
failed = [k for k, v in results.items() if not v]
if failed:
    print(f"  ✗ FALLIDOS: {failed}")
else:
    print(f"  ✔ TODOS VALIDADOS — listos para el .tex")
print(f"{'═'*50}")
```

#### Criterio de aceptación

- **Exacto** (`==`): para resultados enteros, racionales o simbólicos
- **Numérico** (`np.allclose(..., atol=1e-5)`): para resultados reales aproximados
- **Muestreo 100%** (`np.mean(mask_orig == mask_sol) == 1.0`): para dominios e intervalos

Si algún test falla → **no añadir ese resultado al `.tex`** → corregir el ejercicio → volver a correr el script.

---

### 5. Estructura del Archivo LaTeX

#### Preámbulo universal

```latex
\documentclass[letterpaper, 12pt]{article}

\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{eso-pic}
\usepackage{transparent}
\usepackage{tikz}
\usetikzlibrary{patterns, arrows.meta, babel}   % ← babel SIEMPRE
\tcbuselibrary{skins, breakable}

% ── Logos ────────────────────────────────────────────────────
% IMPORTANTE: copiar los logos a ./images/ dentro de la carpeta de la guía
% Ver sección "Logos" más abajo
\newcommand{\logoup}{./images/logo_up.png}
\newcommand{\logousach}{./images/logo_usach.png}
\newcommand{\logofondo}{./images/logo_up.png}

% ── Colores institucionales ──────────────────────────────────
\definecolor{celesteSuave}{HTML}{F0F7FF}
\definecolor{azulFuerte}{HTML}{1A5276}
\definecolor{verdePaso}{HTML}{1E8449}
\definecolor{naranjaNivel}{HTML}{D35400}
\definecolor{rojoAlerta}{HTML}{C0392B}

% ── Macros de nivel ──────────────────────────────────────────
\newcommand{\nivelbasico}{\textcolor{verdePaso}{\textbf{[Básico]}}}
\newcommand{\nivelintermedio}{\textcolor{naranjaNivel}{\textbf{[Intermedio]}}}
\newcommand{\niveladvanzado}{\textcolor{azulFuerte}{\textbf{[Avanzado]}}}
\newcommand{\nivelpep}{\textcolor{rojoAlerta}{\textbf{[PEP]}}}
```

#### Cajas tcolorbox disponibles

```latex
% Caja de ejercicio con sombra
\newtcolorbox{desafiobox}[1]{
    colback=white, colframe=azulFuerte, fonttitle=\bfseries,
    coltitle=white, title=#1, arc=8pt, boxrule=1.2pt, enhanced,
    drop shadow={black!5}}

% Caja de solución (fondo celeste)
\newenvironment{solbox}[1]{
    \begin{tcolorbox}[colback=celesteSuave, colframe=azulFuerte,
        title=\textbf{#1}, fonttitle=\bfseries]
}{\end{tcolorbox}}

% Aviso / Alerta (para secciones PEP)
% \begin{tcolorbox}[colback=rojoAlerta!8, colframe=rojoAlerta, ...]

% Entorno del solucionario completo (nueva página, título grande)
\newenvironment{soluciones}{%
    \newpage
    \begin{center}
        \begin{tcolorbox}[colback=azulFuerte, colframe=azulFuerte,
            colupper=white, width=0.8\textwidth, center, arc=10pt]
            \centering\Large\textbf{SOLUCIONARIO}
        \end{tcolorbox}
    \end{center}
    \MarcaAgua\small
}{}
```

#### Estructura de secciones

```latex
\subsection*{I.\; [Nombre descriptivo del tema] \nivelbasico}

\begin{enumerate}[label=\color{azulFuerte}\bfseries\arabic*.,
                  leftmargin=*, itemsep=1.2em]
    \item Enunciado del ejercicio 1...
    \item Enunciado del ejercicio 2...
\end{enumerate}
```

---

### 6. Solucionario — Solo Resultado Final

El solucionario **únicamente muestra el resultado**, sin desarrollo:

```latex
\begin{soluciones}

\begin{solbox}{I. Soluciones — [Nombre de sección]}
\begin{enumerate}[label=\color{azulFuerte}\bfseries\arabic*.,
                  leftmargin=*, itemsep=0.6em]
    \item Resultado final del ejercicio 1
    \item Resultado final del ejercicio 2
\end{enumerate}
\end{solbox}

\vspace{0.4cm}

\begin{solbox}{II. Soluciones — [Siguiente sección]}
...
\end{solbox}

\end{soluciones}
```

**Prohibido** en el solucionario: tablas, pasos intermedios, justificaciones, desarrollos.  
→ Para eso existe el skill `develop-ejercicio`.

---

### 7. Logos — Regla Fija

Los logos **deben estar en `./images/`** dentro de la misma carpeta del `.tex`.  
Nunca usar rutas relativas hacia arriba (`../../`) ni rutas con espacios.

```bash
# Copiar logos desde el template del repositorio
mkdir -p ./images
cp <raíz-del-repo>/template/images/logo_up.png    ./images/
cp <raíz-del-repo>/template/images/logo_usach.png ./images/
```

Los logos también se encuentran en otras guías del repo en caso de que el template no esté disponible:
```
1-2026/nivel-1/calculo-1/guías/guia1/images/
1-2026/nivel-1/algebra-1/guías/guia2/images/
```

---

### 8. Compilar y Verificar PDF

```bash
# En Linux/macOS (bash)
cd <carpeta-del-archivo>
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | grep -E "^!|Output written"
# Segunda pasada (referencias cruzadas)
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | grep "Output written"
```

**Criterio de éxito**: `Output written on <archivo>.pdf (N pages, ...)` sin ninguna línea `!` lógica.

> Los errores `pdftex.def Error: File './images/logo_up.png' not found` indican que los logos no fueron copiados. Ejecutar el comando de copia antes de recompilar.

---

### 9. Bugs Conocidos

| Bug | Causa | Fix |
|-----|-------|-----|
| `\language@active@arg>` en TikZ | `babel[spanish]` activa `>` como carácter especial | Añadir `babel` a `\usetikzlibrary{..., babel}` — **siempre** |
| `Lonely \item` | `\item` escrito fuera de `enumerate` o `itemize` | Envolver todos los ítems dentro del entorno correcto |
| `Missing \begin{document}` | `\includegraphics{}` vacío u otro comando en el preámbulo | Eliminar la línea; los comandos de contenido van solo en el cuerpo |
| Logos no encontrados | Rutas relativas largas o con espacios | Copiar logos a `./images/` y usar `./images/logo_up.png` |
| `MarcaAgua` usa ruta hardcodeada | El comando `\MarcaAgua` tiene ruta literal en lugar de `\logofondo` | Reemplazar `{ruta/logo.png}` por `{\logofondo}` en la definición |

---

## Checklist de Entrega

### Validación Python
- [ ] Script de validación guardado junto al `.tex`
- [ ] Todos los resultados del solucionario validados con **2 librerías distintas**
- [ ] El script imprime `N/N PASS` sin ningún `FAIL`

### LaTeX
- [ ] Logos copiados a `./images/` dentro de la carpeta de la guía
- [ ] `\logoup`, `\logousach`, `\logofondo` apuntan a `./images/`
- [ ] `\MarcaAgua` usa `{\logofondo}` (no ruta hardcodeada)
- [ ] `babel` incluido en `\usetikzlibrary`
- [ ] Sin `\item` sueltos fuera de listas
- [ ] Sin `\includegraphics{}` vacíos en el preámbulo
- [ ] Indicadores de nivel (`\nivelbasico`, etc.) en los títulos de sección
- [ ] Solucionario solo con resultado final

### PDF
- [ ] Dos pasadas de `pdflatex` ejecutadas
- [ ] Sin errores `!` lógicos en la salida
- [ ] PDF revisado visualmente: portada, ejercicios, solucionario
