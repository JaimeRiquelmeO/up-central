# Crear y validar una guía dentro del repositorio

## Inicio rápido

1. Copie esta carpeta dentro del ramo correspondiente, por ejemplo:
   `1-2026/nivel-1/calculo-1/guías/nueva-guia/`.
2. Complete `CONTEXTO_GUIA.md`.
3. Abra la carpeta en Visual Studio Code o inicie una tarea de Codex y pida crear la guía usando ese contexto.
4. Reemplace el contenido pendiente de `main.tex`.
5. Implemente todas las pruebas de `validar_resultados.py`.
6. Instale dependencias con `python -m pip install -r requirements.txt`.
7. Ejecute `./construir_y_revisar.ps1`.
8. Revise manualmente cada PNG de `tmp_render/`.
9. Copie el PDF aprobado a `output/pdf/`.

`AGENTS.md` contiene reglas que Codex debe seguir automáticamente al trabajar dentro de esta carpeta.
