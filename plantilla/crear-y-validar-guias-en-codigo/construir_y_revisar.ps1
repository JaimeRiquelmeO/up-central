$ErrorActionPreference = "Stop"

python .\validar_resultados.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex

$renderDir = Join-Path $PSScriptRoot "tmp_render"
New-Item -ItemType Directory -Force -Path $renderDir | Out-Null
pdftoppm -png -r 120 main.pdf (Join-Path $renderDir "pagina")

python .\verificar_pdf.py

Write-Host "Proceso automático completado. Revise visualmente todos los PNG de tmp_render antes de entregar."
