class TextAnalyzerError(Exception):
    """Error base del sistema"""
    pass


class EmptyTextError(TextAnalyzerError):
    """Se lanza cuando el texto está vacío"""
    pass


class ExportError(TextAnalyzerError):
    """Error al exportar archivos"""
    pass


class WordAnalysisError(TextAnalyzerError):
    """Error durante análisis de palabra"""
    pass