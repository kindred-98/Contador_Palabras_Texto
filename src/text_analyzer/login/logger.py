import logging
import os

from logging.handlers import RotatingFileHandler


def setup_logger():

    logger = logging.getLogger("text_analyzer")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # ==============================
    # Crear carpeta logs
    # ==============================

    os.makedirs("logs", exist_ok=True)

    # ==============================
    # Formato profesional
    # ==============================

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # ==============================
    # Log principal (rotating)
    # ==============================

    file_handler = RotatingFileHandler(
        "logs/text_analyzer.log",
        maxBytes=1_000_000,  # 1MB
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.INFO)

    file_handler.setFormatter(formatter)

    # ==============================
    # Log de errores
    # ==============================

    error_handler = RotatingFileHandler(
        "logs/errors.log",
        maxBytes=500_000,
        backupCount=3,
        encoding="utf-8"
    )

    error_handler.setLevel(logging.ERROR)

    error_handler.setFormatter(formatter)

    # ==============================
    # Consola
    # ==============================

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    # ==============================
    # Añadir handlers
    # ==============================

    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger