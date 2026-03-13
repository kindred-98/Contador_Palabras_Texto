def format_analysis(result):
    """
    Convierte AnalysisResult en texto legible para GUI.
    """

    lines = []

    lines.append("📊 ESTADÍSTICAS DEL TEXTO\n")

    lines.append(f"Caracteres: {result.num_characters}")
    lines.append(f"Caracteres sin espacios: {result.num_characters_no_spaces}")
    lines.append(f"Palabras: {result.num_words}")
    lines.append(f"Oraciones: {result.num_sentences}")
    lines.append(f"Párrafos: {result.num_paragraphs}")

    lines.append("\n📈 PALABRAS MÁS FRECUENTES\n")

    for word, freq in result.most_common_words:
        lines.append(f"{word} → {freq}")

    if result.errors:
        lines.append("\n⚠️ ERRORES")
        for e in result.errors:
            lines.append(e)

    return "\n".join(lines)