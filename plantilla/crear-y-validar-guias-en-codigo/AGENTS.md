# Reglas para crear guías en esta carpeta

## Antes de editar

1. Leer completamente `CONTEXTO_GUIA.md`, `CHECKLIST.md` y esta instrucción.
2. Si `CONTEXTO_GUIA.md` tiene campos esenciales pendientes, preguntar al usuario por ramo, contenidos, cantidad de ejercicios, dificultad y tipo de solucionario.
3. Revisar al menos dos guías comparables del repositorio para respetar el estilo académico y visual.

## Archivos de salida

- Fuente principal: `main.tex`.
- Validación: `validar_resultados.py`.
- PDF de trabajo: `main.pdf`.
- PDF final: copiar a `output/pdf/` con un nombre descriptivo.
- Imágenes: `images/`.

## Validación obligatoria

- Crear una prueba identificable para cada ejercicio y subítem con respuesta.
- Usar Python y al menos dos métodos o librerías independientes cuando el tipo de ejercicio lo permita.
- Base recomendada: SymPy + NumPy/SciPy; usar también `fractions`, `decimal`, `math`, sustitución directa, enumeración o simulación según corresponda.
- La cantidad de pruebas registradas debe coincidir con el inventario de resultados de la guía.
- El script debe fallar si queda un marcador `PENDIENTE`, una prueba no implementada o un resultado incorrecto.
- No afirmar que la guía está validada si el script no termina con código 0.
- Revisar dominios, unidades, redondeos, soluciones espurias y casos especiales.

## PDF

- Compilar dos veces.
- Renderizar todas las páginas y revisarlas visualmente.
- No aceptar contenido cortado, cajas desbordadas, encabezados ausentes, páginas involuntariamente vacías ni caracteres dañados.
- Comprobar estructura y texto extraíble con `pypdf` y `pdfplumber`.

## Prohibición editorial

La guía y el PDF nunca deben mencionar Python, SymPy, NumPy, inteligencia artificial, scripts o el proceso interno de validación.
