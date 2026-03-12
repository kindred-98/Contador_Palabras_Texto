import json
import csv
from datetime import datetime


def generate_filename(prefix: str, extension: str):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefix}_{timestamp}.{extension}"


# ===============================
# EXPORTAR RESULTADO COMPLETO
# ===============================

def serialize_analysis(result):

    """
    Convierte AnalysisResult a diccionario exportable
    """

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

def export_json(result):

    filename = generate_filename("analysis", "json")

    data = serialize_analysis(result)

    with open(filename, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4, ensure_ascii=False)

    return filename


# ===============================
# EXPORTAR CSV
# ===============================

def export_csv(result):

    filename = generate_filename("analysis", "csv")

    data = serialize_analysis(result)

    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["metric", "value"])

        writer.writerow(["num_caracteres", data["num_caracteres"]])
        writer.writerow(["num_palabras", data["num_palabras"]])
        writer.writerow(["num_oraciones", data["num_oraciones"]])
        writer.writerow(["num_parrafos", data["num_parrafos"]])

        writer.writerow([])
        writer.writerow(["top_palabras", "frecuencia"])

        for word, freq in data["top_palabras"]:

            writer.writerow([word, freq])

    return filename


# ===============================
# EXPORTAR TXT
# ===============================

def export_txt(result):

    filename = generate_filename("analysis", "txt")

    data = serialize_analysis(result)

    with open(filename, "w", encoding="utf-8") as f:

        f.write("ANALISIS DE TEXTO\n\n")

        f.write(f"Palabras: {data['num_palabras']}\n")
        f.write(f"Caracteres: {data['num_caracteres']}\n")
        f.write(f"Oraciones: {data['num_oraciones']}\n")
        f.write(f"Parrafos: {data['num_parrafos']}\n\n")

        f.write("PALABRAS MAS FRECUENTES\n")

        for word, freq in data["top_palabras"]:

            f.write(f"{word}: {freq}\n")

    return filename