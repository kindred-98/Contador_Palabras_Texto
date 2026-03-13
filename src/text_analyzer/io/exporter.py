# src/text_analyzer/io/exporter.py

import json
import csv
from datetime import datetime
from typing import Any

from ..core.models import AnalysisResult


def generate_filename(prefix: str, extension: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"


# ===============================
# SERIALIZAR RESULTADO
# ===============================

def serialize_analysis(result: AnalysisResult | dict) -> dict:
    """
    Convierte AnalysisResult o dict exportable a diccionario.
    """

    if isinstance(result, dict):
        # si ya es un dict (por ejemplo tests), lo devolvemos tal cual
        return result

    return {
        "texto_original": result.raw_text,
        "texto_normalizado": result.normalized_text,
        "num_caracteres": result.num_characters,
        "num_caracteres_sin_espacios": result.num_characters_no_spaces,
        "num_palabras": result.num_words,
        "num_oraciones": result.num_sentences,
        "num_parrafos": result.num_paragraphs,
        "top_palabras": result.most_common_words
    }


# ===============================
# EXPORTAR JSON
# ===============================

def export_json(result: AnalysisResult | dict) -> str:
    filename = generate_filename("analysis", "json")
    data = serialize_analysis(result)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return filename


# ===============================
# EXPORTAR CSV
# ===============================

def export_csv(result: AnalysisResult | dict) -> str:
    filename = generate_filename("analysis", "csv")
    data = serialize_analysis(result)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        writer.writerow(["num_caracteres", data.get("num_caracteres", 0)])
        writer.writerow(["num_palabras", data.get("num_palabras", 0)])
        writer.writerow(["num_oraciones", data.get("num_oraciones", 0)])
        writer.writerow(["num_parrafos", data.get("num_parrafos", 0)])
        writer.writerow([])
        writer.writerow(["top_palabras", "frecuencia"])

        for word, freq in data.get("top_palabras", []):
            writer.writerow([word, freq])

    return filename


# ===============================
# EXPORTAR TXT
# ===============================

def export_txt(result: AnalysisResult | dict) -> str:
    filename = generate_filename("analysis", "txt")
    data = serialize_analysis(result)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("ANALISIS DE TEXTO\n\n")
        f.write(f"Palabras: {data.get('num_palabras', 0)}\n")
        f.write(f"Caracteres: {data.get('num_caracteres', 0)}\n")
        f.write(f"Oraciones: {data.get('num_oraciones', 0)}\n")
        f.write(f"Parrafos: {data.get('num_parrafos', 0)}\n\n")
        f.write("PALABRAS MAS FRECUENTES\n")
        for word, freq in data.get("top_palabras", []):
            f.write(f"{word}: {freq}\n")

    return filename