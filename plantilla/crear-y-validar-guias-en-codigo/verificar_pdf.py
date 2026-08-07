"""Comprobaciones estructurales del PDF; la revisión visual sigue siendo obligatoria."""

from pathlib import Path

import pdfplumber
from pypdf import PdfReader


PDF = Path("main.pdf")
if not PDF.exists():
    raise FileNotFoundError("No existe main.pdf. Compile LaTeX antes de ejecutar esta prueba.")

reader = PdfReader(PDF)
if not reader.pages:
    raise AssertionError("El PDF no contiene páginas")

for numero, pagina in enumerate(reader.pages, start=1):
    ancho = float(pagina.mediabox.width)
    alto = float(pagina.mediabox.height)
    if abs(ancho - 612) > 1 or abs(alto - 792) > 1:
        raise AssertionError(f"Página {numero}: no tiene tamaño carta ({ancho} x {alto})")

with pdfplumber.open(PDF) as documento:
    vacias = [i for i, pagina in enumerate(documento.pages, start=1) if not (pagina.extract_text() or "").strip()]
    if vacias:
        raise AssertionError(f"Páginas sin texto extraíble: {vacias}")

texto = "\n".join((pagina.extract_text() or "") for pagina in reader.pages)
for seccion in ("GUÍA", "SOLUCIONARIO"):
    if seccion not in texto:
        raise AssertionError(f"No se encontró la sección requerida: {seccion}")

print(f"OK PDF: {len(reader.pages)} páginas carta con texto extraíble.")
