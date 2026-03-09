import json
from pathlib import Path

# Ruta del archivo JSON
BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "history.json"


def load_history():
    """Carga historial desde JSON"""
    if not HISTORY_FILE.exists():
        return {"texts": {}, "words": {}}

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history):
    """Guarda historial en JSON"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)


def get_text_analysis(text):
    history = load_history()
    return history["texts"].get(text)


def save_text_analysis(text, result):
    history = load_history()
    history["texts"][text] = result
    save_history(history)


def get_word_analysis(word):
    history = load_history()
    return history["words"].get(word)


def save_word_analysis(word, result):
    history = load_history()
    history["words"][word] = result
    save_history(history)