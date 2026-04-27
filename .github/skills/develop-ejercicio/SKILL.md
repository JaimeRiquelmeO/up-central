---
name: develop-ejercicio
description: "Desarrollar el paso a paso completo de un ejercicio matemático en PDF LaTeX estilo Usach Premium. Cada paso intermedio debe estar validado con Python antes de incluirlo. Usar cuando: crear solucionario detallado, desarrollo completo con tabla de signos y recta numérica, verificar un ejercicio específico paso a paso."
argument-hint: "Ejercicio a desarrollar, ej: ejercicio 2.3 de c1_inecuaciones — raíz sobre raíz"
---

# Desarrollo Paso a Paso — Usach Premium

## Cuando Usar

- Crear un PDF con el desarrollo completo y detallado de un ejercicio
- Generar solucionario con tabla de signos, recta numérica y justificaciones
- Verificar si una solución es correcta analizando cada transformación

---

## REGLA FUNDAMENTAL — Validación por Paso

> **Cada afirmación matemática intermedia importante debe verificarse con Python**.  
> No basta validar solo el resultado final: verificar que cada equivalencia/transformación conserva el conjunto solución.

Si una transformación falla la validación → hay un error en ese paso → corregir antes de continuar.

---

## Procedimiento

### 1. Analizar el Ejercicio

Antes de escribir código o LaTeX:

- Leer el enunciado completo
- Identificar el tipo: inecuación, ecuación, límite, integral, etc.
- Definir los pasos que se necesitarán (dominio → transformaciones → tabla de signos → intersección)
- Identificar los puntos críticos (raíces, cambios de signo)

---

### 2. Validar CADA Paso con Python

#### Esquema general (inecuaciones)

```python
from sympy import *
import numpy as np, math

x = symbols('x', real=True)

# ── PASO 1: Dominio ──────────────────────────────────────────
# Verificar simbólicamente las condiciones de dominio
dom_cond_1 = solveset(<condición 1>, x, S.Reals)
dom_cond_2 = solveset(<condición 2>, x, S.Reals)
dominio = dom_cond_1 & dom_cond_2
print("Dominio:", dominio)

# ── PASO 2..N: Cada transformación ──────────────────────────
# Antes de declarar A ⟺ B, verificar numericamente:
pts_dom = np.linspace(<a>, <b>, 50_000)
mask_A = <condición A vectorizada>
mask_B = <condición B vectorizada>
print(f"Equivalencia A⟺B: {np.mean(mask_A == mask_B)*100:.4f}%")  # debe ser 100%

# ── RESULTADO FINAL: Doble validación ───────────────────────
# Librería 1 — SymPy (simbólico)
sol_sympy = solveset(<inecuación original>, x, S.Reals)
print("SymPy:", sol_sympy)

# Librería 2 — NumPy (muestreo, 50 000+ puntos con desfase irracional)
rng = np.random.default_rng(0)
pts = np.sort(np.concatenate([
    np.linspace(<min>, <max>, 40_000) + 1e-6 * math.pi,
    rng.uniform(<min>, <max>, 10_000)
]))
# Evaluar inecuación original y conjunto solución
mask_orig = <inecuación original sobre pts, con guardas para dominio>
mask_sol  = <intervalo/unión resultante sobre pts>
acuerdo = np.mean(mask_orig == mask_sol)
print(f"NumPy acuerdo: {100*acuerdo:.4f}%")   # debe ser 100.0000%
```

**Criterio de aceptación**: ambas librerías coinciden al 100 %.  
Si hay discrepancia → hay un error en el paso → recalcular → re-validar.

---

### 3. Estructura del Documento LaTeX

#### Cajas personalizadas requeridas

```latex
% Paso numerado — cabecera azul
\newtcolorbox{paso}[2][]{
    colback=celesteSuave!30, colframe=azulFuerte,
    title={Paso #2}, fonttitle=\bfseries\large,
    coltitle=white, colbacktitle=azulFuerte,
    arc=8pt, boxrule=1.5pt, enhanced, #1}

% Resultado final — fondo azul oscuro
\newtcolorbox{resultado}{
    colback=azulFuerte, colframe=azulFuerte,
    colupper=white, arc=10pt, boxrule=1.5pt,
    enhanced, drop shadow={black!15}}

% Justificación / advertencia — naranja
\newtcolorbox{justif}[1]{
    colback=orange!10, colframe=orange!70!black,
    title={#1}, fonttitle=\bfseries,
    coltitle=black, arc=6pt, boxrule=1pt, enhanced}
```

#### Estructura de páginas del PDF

1. **Portada** — enunciado del ejercicio destacado en caja
2. **Paso 1** — Determinación del dominio (siempre primero en inecuaciones)
3. **Paso 2…N** — Transformaciones algebraicas con `\begin{justif}` cuando se cambia la dirección de la desigualdad
4. **Tabla de signos** — `tabular` dentro de tcolorbox + `tikzpicture` con recta numérica
5. **Intersección con el dominio**
6. **Resultado final** en `\begin{resultado}` (o tcolorbox azul)

**NO incluir** sección de verificación Python en el PDF final.

---

### 4. Recta Numérica con TikZ

```latex
% IMPORTANTE: siempre incluir babel en usetikzlibrary para evitar
% el error \language@active@arg> con babel[spanish]
\usetikzlibrary{patterns, arrows.meta, decorations.pathmorphing, babel}

\begin{tikzpicture}[scale=1.1]
    \draw[->] (-2.5,0) -- (4,0) node[right] {$x$};
    % Raíces / puntos críticos
    \fill[azulFuerte] (<r1>,0) circle (2.5pt)
        node[below=4pt] {\small$r_1 \approx <valor>$};
    \fill[azulFuerte] (<r2>,0) circle (2.5pt)
        node[below=4pt] {\small$r_2 \approx <valor>$};
    % Signos en cada región
    \node at (<pos_izq>, 0.35) {\color{rojoAlerta}$f > 0$};
    \node at (<pos_med>, 0.35) {\color{verdePaso}$f < 0$};
    \node at (<pos_der>, 0.35) {\color{rojoAlerta}$f > 0$};
    % Segmento solución
    \draw[verdePaso, very thick] (<r1>,0) -- (<r2>,0);
    % Dominio (líneas punteadas)
    \draw[azulFuerte!60, dashed, thick] (<a>,-0.55) -- (<a>,0.55);
    \draw[azulFuerte!60, dashed, thick] (<b>,-0.55) -- (<b>,0.55);
    \node[azulFuerte] at (<medio_dom>,-0.9) {\small Dominio};
\end{tikzpicture}
```

---

### 5. Tabla de Signos

```latex
\begin{center}
\renewcommand{\arraystretch}{1.7}
\begin{tabular}{c|ccccc}
    & \small$x < r_1$ & \small$x = r_1$ & \small$r_1 < x < r_2$
      & \small$x = r_2$ & \small$x > r_2$ \\
\hline
$(x - r_1)$ & $-$ & $0$ & $+$ & $+$ & $+$ \\
$(x - r_2)$ & $-$ & $-$ & $-$ & $0$ & $+$ \\
\hline
\rowcolor{celesteSuave}
$f(x)$ & $+$ & $0$ & $\mathbf{-}$ & $0$ & $+$ \\
\end{tabular}
\end{center}
```

---

### 6. Compilar y Verificar PDF

```powershell
cd <carpeta-del-archivo>
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | Select-String "^!|Output written"
# Segunda pasada
pdflatex -interaction=nonstopmode <archivo>.tex 2>&1 | Select-String "Output written"
```

**Criterio de éxito**: ninguna línea comenzando con `!` en la salida.

---

## Checklist de Entrega

- [ ] Cada paso intermedio clave verificado con Python
- [ ] Resultado final validado con SymPy **Y** NumPy (o dos librerías equivalentes)
- [ ] Ninguna discrepancia entre librerías
- [ ] Tabla de signos presente y matemáticamente correcta
- [ ] Recta numérica TikZ con `babel` en `\usetikzlibrary` (sin errores `>`)
- [ ] **NO** hay sección de verificación Python en el PDF final
- [ ] PDF compila limpio (sin líneas `!`)
- [ ] PDF revisado visualmente: pasos, tabla, recta numérica, resultado
- [ ] Logos con rutas `./template/images/logo_up.png` y `logo_usach.png`
