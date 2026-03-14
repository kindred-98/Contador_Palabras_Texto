import json
import csv
from datetime import datetime
from text_analyzer.core.analyzer import AnalysisResult


# ===============================
# GENERAR NOMBRE DE ARCHIVO
# ===============================
def generate_filename(prefix: str, extension: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"


# ===============================
# SERIALIZAR RESULTADO
# ===============================
def serialize_analysis(result) -> dict:
    """
    Convierte AnalysisResult o dict a estructura estándar.
    """

    # Caso tests (dict)
    if isinstance(result, dict):

        data = {
            "texto_original": result.get("texto_original", ""),
            "texto_normalizado": result.get("texto_normalizado", ""),
            "num_caracteres": result.get("num_caracteres", 0),
            "num_caracteres_sin_espacios": result.get("num_caracteres_sin_espacios", 0),
            "num_palabras": result.get("num_palabras", 0),
            "num_oraciones": result.get("num_oraciones", 0),
            "num_parrafos": result.get("num_parrafos", 0),
            "top_palabras": result.get("top_palabras", []),
        }

        # asegurar tuplas
        data["top_palabras"] = [tuple(x) for x in data["top_palabras"]]

        return data

    # Caso AnalysisResult real
    return {
        "texto_original": result.raw_text,
        "texto_normalizado": result.normalized_text,
        "num_caracteres": result.num_characters,
        "num_caracteres_sin_espacios": result.num_characters_no_spaces,
        "num_palabras": result.num_words,
        "num_oraciones": result.num_sentences,
        "num_parrafos": result.num_paragraphs,
        "top_palabras": list(result.most_common_words),
    }


# ===============================
# EXPORTAR JSON
# ===============================
def export_json(result) -> str:
    filename = generate_filename("analysis", "json")

    data = serialize_analysis(result)

    # JSON no soporta tuplas → convertir a listas
    if "top_palabras" in data:
        data["top_palabras"] = [list(x) for x in data["top_palabras"]]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return filename


# ===============================
# EXPORTAR CSV
# ===============================
def export_csv(result) -> str:
    filename = generate_filename("analysis", "csv")

    data = serialize_analysis(result)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "texto_original",
            "num_caracteres",
            "num_caracteres_sin_espacios",
            "num_palabras",
            "num_oraciones",
            "num_parrafos",
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow({
            "texto_original": data.get("texto_original", ""),
            "num_caracteres": data.get("num_caracteres", 0),
            "num_caracteres_sin_espacios": data.get("num_caracteres_sin_espacios", 0),
            "num_palabras": data.get("num_palabras", 0),
            "num_oraciones": data.get("num_oraciones", 0),
            "num_parrafos": data.get("num_parrafos", 0),
        })

    return filename

# ===============================
# EXPORTAR TXT
# ===============================
def export_txt(result) -> str:
    filename = generate_filename("analysis", "txt")

    data = serialize_analysis(result)

    # Evitamos caracteres que rompen cp1252 en tests
    header = "ANALISIS DE TEXTO"

    with open(filename, "w", encoding="utf-8") as f:

        f.write(header + "\n\n")

        f.write(f"Texto original:\n{data.get('texto_original','')}\n\n")

        f.write(f"Palabras: {data.get('num_palabras',0)}\n")
        f.write(f"Caracteres: {data.get('num_caracteres',0)}\n")
        f.write(f"Caracteres sin espacios: {data.get('num_caracteres_sin_espacios',0)}\n")
        f.write(f"Oraciones: {data.get('num_oraciones',0)}\n")
        f.write(f"Parrafos: {data.get('num_parrafos',0)}\n\n")

        f.write("PALABRAS MAS FRECUENTES\n")

        for palabra, freq in data["top_palabras"]:
            f.write(f"{palabra}: {freq}\n")

    return filename