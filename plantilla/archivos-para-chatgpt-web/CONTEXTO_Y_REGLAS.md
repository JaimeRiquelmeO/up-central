# Contexto institucional y reglas de calidad

La entrega debe parecer una guía del repositorio Usach Premium: formato carta, portada institucional, colores azul y celeste, logos proporcionados, encabezado, pie de página, secciones claras y solucionario separado.

## Reglas académicas

- Diseñar primero un inventario de ejercicios y resultados.
- Evitar datos insuficientes, contradicciones, ambigüedades y soluciones no deseadas.
- Mantener correspondencia exacta entre numeración, enunciados, respuestas y pruebas.
- Especificar dominios, unidades, tolerancias y redondeos.
- Si una referencia contiene un error, corregirlo y reportarlo fuera del PDF.
- En una solicitud de validación, no modificar la guía salvo que el usuario pida expresamente una versión corregida.
- Diferenciar claramente errores del enunciado, errores de cálculo, errores del solucionario y elementos que no puedan verificarse con los datos disponibles.

## Validación obligatoria

- Crear y ejecutar un archivo Python que cubra cada ejercicio o subítem con resultado.
- Usar dos métodos independientes cuando sea viable y tres en resultados sensibles.
- Herramientas recomendadas: SymPy, NumPy, SciPy, `fractions`, `decimal`, `math`, enumeración, sustitución directa o simulación.
- Preferir resultados exactos y usar tolerancias explícitas para aproximaciones.
- Probar restricciones de dominio, casos degenerados y soluciones espurias.
- El validador debe fallar si falta una prueba o si existe un marcador pendiente.
- No declarar la guía validada hasta ejecutar el script con todas las pruebas aprobadas.

## Verificación del PDF

- Compilar LaTeX dos veces.
- Renderizar todas las páginas y revisarlas visualmente.
- Comprobar que no existan cortes, superposiciones, caracteres dañados o páginas accidentales.
- Abrir el PDF con `pypdf` y `pdfplumber` y comprobar texto extraíble, tamaño carta y secciones requeridas.

## Regla editorial

El PDF entregable no debe mencionar Python, librerías, inteligencia artificial, scripts ni el proceso interno de validación.
