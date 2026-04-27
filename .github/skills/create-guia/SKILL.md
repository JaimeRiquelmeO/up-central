---
name: create-guia
description: "Crear guías de ejercicios matemáticos en LaTeX estilo Usach Premium (Cálculo I, Álgebra). Solucionario con resultado final únicamente, sin paso a paso. OBLIGATORIO: validar CADA resultado con Python (SymPy + NumPy, mínimo 2 librerías) antes de añadir al PDF. Usar cuando: crear guía, añadir ejercicios, completar solucionario, generar PDF de guía de ejercicios."
argument-hint: "Describe la guía: asignatura, tema, número de ejercicios y nivel de dificultad"
---

# Crear Guía LaTeX — Usach Premium

## Cuando Usar

- Crear nueva guía de ejercicios para una asignatura (Cálculo I, Álgebra, etc.)
- Añadir ejercicios a una guía existente
- Completar o corregir un solucionario
- Generar PDF de una guía de práctica o control

---

## REGLA FUNDAMENTAL — Validación Python

> **NUNCA** añadir un resultado al solucionario sin haberlo validado primero con Python usando **al menos 2 librerías independientes**.

Si hay discrepancia entre librerías → recalcular el ejercicio a mano → volver a validar → solo entonces añadir al `.tex`.

---

## Procedimiento

### 1. Recopilar Información

Antes de escribir LaTeX, determinar:

- Asignatura (Cálculo I, Álgebra, Física, etc.)
- Unidad / tema (Inecuaciones con raíz, Valor absoluto, Límites, etc.)
- Número de secciones y escala de dificultad (Básica → Intermedia → Desafío)
- Número de ejercicios por sección
- ¿Existe archivo `.tex` previo que extender?

---

### 2. Calcular y Validar TODOS los Resultados

Para **cada** ejercicio, ejecutar el siguiente esquema antes de tocar el `.tex`:

```python
from sympy import *
import numpy as np

x = symbols('x', real=True)

# ── Librería 1: SymPy (simbólico) ──────────────────────────
sol_sympy = solveset(<inecuación o ecuación>, x, S.Reals)
print("SymPy:", sol_sympy)

# ── Librería 2: NumPy (muestreo numérico denso) ─────────────
pts = np.linspace(-20, 20, 100_000)
# Construir máscara vectorizada que evalúe la inecuación original
mask_orig = <condición sobre pts>
# Construir máscara que evalúe el conjunto solución encontrado
mask_sol  = <condición equivalente al intervalo/unión de intervalos>
acuerdo = np.mean(mask_orig == mask_sol)
print(f"NumPy acuerdo: {100*acuerdo:.4f}%")  # debe ser 100.0000%
```

**Criterio de aceptación**: ambas librerías coinciden al 100 %.  
Si no coinciden → la solución tiene un error → NO añadir al PDF.

---

### 3. Estructura del Archivo LaTeX

Plantilla base del proyecto (ver `template/guia-institucional.tex`):

```latex
\documentclass[11pt,letterpaper]{article}
% Paquetes requeridos:
%   amsmath, amssymb
%   tcolorbox con opciones: skins, breakable
%   tikz — SIEMPRE incluir la librería babel:
\usetikzlibrary{patterns, arrows.meta, decorations.pathmorphing, babel}
%   babel con opción spanish
%   fancyhdr, multicol, enumitem, colortbl, booktabs
%   xcolor, graphicx, eso-pic, hyperref

% Colores institucionales disponibles:
%   azulFuerte, celesteSuave, verdeExito, rojoAlerta, verdePaso

% Cajas tcolorbox disponibles:
%   ejercicios, solbox, desafiobox, \listacontenidos

% Logos — SOLO estas rutas funcionan:
%   ./template/images/logo_up.png
%   ./template/images/logo_usach.png
```

---

### 4. Solucionario — Solo Resultado Final

El solucionario de la guía **únicamente muestra el resultado**, sin desarrollo:

```latex
\begin{solbox}{Sección I — Ejercicio 1.1}
    $x \in (-\infty, 3]$
\end{solbox}
```

**Prohibido** en el solucionario de guía: tablas de signos, pasos algebraicos,
justificaciones, desarrollo, rectas numéricas.  
→ Para eso existe el skill `develop-ejercicio`.

---

### 5. Escala de Dificultad Recomendada

| Sección | Tipo | Descripción |
|---------|------|-------------|
| I | Básica | Aplicación directa, 1–2 condiciones |
| II | Intermedia | Combinación de condiciones, dominio no trivial |
| III | Desafío | Raíz sobre raíz, parámetros, casos por separar |

---

### 6. Compilar y Verificar PDF

```powershell
cd <carpeta-del-archivo>
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | Select-String "^!|Output written"
# Segunda pasada para referencias cruzadas
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | Select-String "Output written"
```

**Criterio de éxito**: ninguna línea comenzando con `!` en la salida.

---

### 7. Bug Conocido — babel + TikZ

`babel[spanish]` activa el carácter `>`. Si aparecen errores `\language@active@arg>`:

- **Fix principal**: añadir `babel` a `\usetikzlibrary{..., babel}` ← siempre hacerlo.
- **Fix secundario** (código dentro de tcolorbox): usar `listings` en lugar de `verbatim`.

---

## Checklist de Entrega

- [ ] Todos los resultados validados con SymPy **Y** NumPy (o dos librerías equivalentes)
- [ ] Ninguna discrepancia entre librerías
- [ ] Solucionario solo con resultado final (sin desarrollo)
- [ ] Compila sin errores `!`
- [ ] PDF abierto y revisado visualmente (portada, ejercicios, solucionario)
- [ ] Logos con rutas `./template/images/logo_up.png` y `logo_usach.png`
- [ ] `babel` incluido en `\usetikzlibrary`
