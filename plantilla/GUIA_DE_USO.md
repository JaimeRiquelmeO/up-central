# Guía de uso

## Información que debe solicitarse antes de comenzar

- ramo y nivel;
- nombre o número de la guía;
- semestre;
- contenidos y subtemas;
- cantidad de ejercicios total y por tema;
- dificultad esperada: básica, media, avanzada o progresiva;
- tipo de ejercicios: cálculo, demostración, aplicación, selección, desarrollo u otros;
- si debe incluir resumen teórico, formulario, pistas o desarrollos completos;
- formato del solucionario: respuestas breves o soluciones desarrolladas;
- nombre de quien prepara la guía;
- fuentes o evaluaciones de referencia;
- fecha de entrega y cualquier restricción especial.

Si faltan datos no críticos, se puede proponer una configuración razonable y pedir confirmación antes de redactar todos los ejercicios.

## Flujo obligatorio

1. Completar el formulario de contexto.
2. Diseñar una tabla maestra con identificador, tema, dificultad, enunciado y resultado esperado para cada ejercicio.
3. Revisar que los enunciados sean suficientes, consistentes y no ambiguos.
4. Escribir la guía y el solucionario en LaTeX.
5. Implementar una prueba Python por cada ejercicio o subítem evaluado.
6. Usar como mínimo dos enfoques de validación cuando sea posible:
   - SymPy para cálculo simbólico o exacto;
   - NumPy o SciPy para comprobación numérica independiente;
   - `fractions`, `decimal`, `math`, simulación, sustitución directa o enumeración como tercera verificación.
7. Ejecutar el validador. Debe terminar con código 0 y reportar que todas las pruebas pasan.
8. Compilar LaTeX dos veces.
9. Renderizar todas las páginas del PDF como PNG y revisarlas visualmente.
10. Verificar el PDF con `pypdf` y `pdfplumber`: cantidad de páginas, tamaño carta, texto extraíble y presencia de secciones/resultados.

## Criterios de validación

- No comparar solamente con el mismo procedimiento usado para crear la respuesta.
- Preferir aritmética exacta antes que decimales.
- En resultados aproximados, declarar tolerancia y unidades.
- Probar dominios, restricciones, casos degenerados y soluciones espurias.
- En demostraciones, validar los pasos algebraicos y hacer pruebas numéricas de apoyo; estas pruebas no reemplazan la demostración.
- Si un enunciado es inconsistente, corregirlo antes de validar y documentar el cambio fuera del PDF.
- No entregar resultados parcialmente comprobados como si estuvieran validados.

## Contenido visible

La validación es interna. Nunca escribir en el PDF frases como “validado con Python”, “hecho con IA” o similares.
