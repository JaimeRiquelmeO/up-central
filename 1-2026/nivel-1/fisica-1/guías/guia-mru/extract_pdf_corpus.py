from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from PyPDF2 import PdfReader


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name("analisis_pdfs.md")
KEYWORDS = (
    "rapidez",
    "velocidad",
    "constante",
    "distancia",
    "tiempo",
    "desplazamiento",
    "aceleracion",
    "aceleración",
    "mru",
    "cinematica",
    "cinemática",
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u00ad", "")).strip()


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return clean("\n".join(page.extract_text() or "" for page in reader.pages))


def main() -> None:
    lines = [
        "# Analisis del corpus PDF - Fisica 1",
        "",
        "Extraccion reproducible realizada con PyPDF2. Algunos PDFs codifican texto sin espacios; el analisis se usa como apoyo cualitativo.",
        "",
        "## Hallazgos de estilo",
        "",
        "- Evaluaciones de 80 minutos, usualmente con 3 problemas.",
        "- Enunciados extensos, contextualizados, con figuras e incisos puntuados.",
        "- Respuestas en Sistema Internacional, recuadradas y redondeadas a 2 decimales.",
        "- Las pautas incluyen resultados numericos y rubricas progresivas.",
        "",
    ]
    total = Counter()
    relevant: list[tuple[str, str]] = []

    for pdf in sorted(ROOT.glob("*.pdf")):
        reader = PdfReader(str(pdf))
        text = pdf_text(pdf)
        lower = text.lower()
        hits = Counter({word: lower.count(word) for word in KEYWORDS if lower.count(word)})
        total.update(hits)
        lines += [
            f"## {pdf.name}",
            "",
            f"- Paginas: {len(reader.pages)}",
            f"- Caracteres extraidos: {len(text)}",
            f"- Palabras clave: {dict(hits)}",
            "",
        ]
        for block in re.split(r"(?=Problema\s*\d+\s*:?)", text):
            if block.startswith("Problema") and any(word in block.lower() for word in KEYWORDS):
                relevant.append((pdf.name, block[:900]))

    lines += ["## Frecuencia global", "", f"`{dict(total)}`", "", "## Fragmentos relevantes", ""]
    for name, snippet in relevant:
        lines += [f"### {name}", "", snippet, ""]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Analisis escrito en {OUT}")


if __name__ == "__main__":
    main()
