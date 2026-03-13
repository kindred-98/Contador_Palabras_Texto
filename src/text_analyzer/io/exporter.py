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
# SERIALIZAR AnalysisResult
# ===============================
def serialize_analysis(result: AnalysisResult) -> dict:
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
def export_json(result: AnalysisResult) -> str:
    filename = generate_filename("analysis", "json")
    data = serialize_analysis(result)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return filename

# ===============================
# EXPORTAR CSV
# ===============================
def export_csv(result: AnalysisResult) -> str:
    filename = generate_filename("analysis", "csv")
    data = serialize_analysis(result)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Métrica", "Valor"])
        writer.writerow(["Caracteres", data["num_caracteres"]])
        writer.writerow(["Caracteres sin espacios", data["num_caracteres_sin_espacios"]])
        writer.writerow(["Palabras", data["num_palabras"]])
        writer.writerow(["Oraciones", data["num_oraciones"]])
        writer.writerow(["Párrafos", data["num_parrafos"]])
        writer.writerow([])
        writer.writerow(["Palabra", "Frecuencia"])
        for palabra, freq in data["top_palabras"]:
            writer.writerow([palabra, freq])
    return filename

# ===============================
# EXPORTAR TXT
# ===============================
def export_txt(result: AnalysisResult) -> str:
    filename = generate_filename("analysis", "txt")
    data = serialize_analysis(result)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("ANÁLISIS DE TEXTO\n\n")
        f.write(f"Texto original:\n{data['texto_original']}\n\n")
        f.write(f"Palabras: {data['num_palabras']}\n")
        f.write(f"Caracteres: {data['num_caracteres']}\n")
        f.write(f"Caracteres sin espacios: {data['num_caracteres_sin_espacios']}\n")
        f.write(f"Oraciones: {data['num_oraciones']}\n")
        f.write(f"Párrafos: {data['num_parrafos']}\n\n")
        f.write("PALABRAS MÁS FRECUENTES\n")
        for palabra, freq in data["top_palabras"]:
            f.write(f"{palabra}: {freq}\n")
    return filename