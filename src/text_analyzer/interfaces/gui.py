import customtkinter as ctk
from tkinter import filedialog
import sys
from text_analyzer.core.analyzer import analyze_text, analyze_single_word
from text_analyzer.interfaces.gui_formatter import format_analysis
from text_analyzer.login.logger import setup_logger

logger = setup_logger()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TextAnalyzerGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        logger.info("GUI iniciada")

        self.title("📊 Text Analyzer Pro")
        self.geometry("900x700")

        self.resultado_actual = None

        # cerrar correctamente al pulsar la X
        self.exit_handler = lambda: sys.exit()
        self.protocol("WM_DELETE_WINDOW", self.exit_handler)

        self.create_layout()

    def create_layout(self):

        # =========================
        # TITULO
        # =========================
        title = ctk.CTkLabel(
            self,
            text="📊 ANALIZADOR DE TEXTO PROFESIONAL",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=15)

        # =========================
        # PANEL TEXTO
        # =========================
        frame_texto = ctk.CTkFrame(self)
        frame_texto.pack(fill="both", padx=20, pady=10)

        label_texto = ctk.CTkLabel(frame_texto, text="Texto o palabra a analizar")
        label_texto.pack(anchor="w", padx=10, pady=5)

        self.text_input = ctk.CTkTextbox(frame_texto, height=150)
        self.text_input.pack(fill="both", padx=10, pady=10)

        # =========================
        # BOTONES
        # =========================
        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(pady=10)

        btn_cargar = ctk.CTkButton(
            frame_botones,
            text="📂 Cargar archivo",
            command=self.cargar_archivo
        )
        btn_cargar.grid(row=0, column=0, padx=10)

        btn_analizar = ctk.CTkButton(
            frame_botones,
            text="🔎 Analizar texto",
            command=self.analizar_texto
        )
        btn_analizar.grid(row=0, column=1, padx=10)

        btn_palabra = ctk.CTkButton(
            frame_botones,
            text="🧠 Analizar palabra",
            command=self.analizar_palabra
        )
        btn_palabra.grid(row=0, column=2, padx=10)

        btn_exportar = ctk.CTkButton(
            frame_botones,
            text="💾 Exportar",
            command=self.exportar
        )
        btn_exportar.grid(row=0, column=3, padx=10)

        btn_salir = ctk.CTkButton(
            frame_botones,
            text="❌ Salir",
            fg_color="red",
            hover_color="#8B0000",
            command=self.salir
        )
        btn_salir.grid(row=0, column=4, padx=10)

        # =========================
        # RESULTADOS
        # =========================
        frame_resultados = ctk.CTkFrame(self)
        frame_resultados.pack(fill="both", expand=True, padx=20, pady=10)

        label_result = ctk.CTkLabel(
            frame_resultados,
            text="📈 Resultados del análisis",
            font=("Arial", 16, "bold")
        )
        label_result.pack(anchor="w", padx=10, pady=5)

        self.result_box = ctk.CTkTextbox(frame_resultados)
        self.result_box.pack(fill="both", expand=True, padx=10, pady=10)

    # =========================
    # CARGAR ARCHIVO
    # =========================
    def cargar_archivo(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )
        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            contenido = f.read()

        self.text_input.delete("1.0", "end")
        self.text_input.insert("1.0", contenido)
        logger.info(f"Archivo cargado: {path}")

    # =========================
    # ANALIZAR TEXTO
    # =========================
    def analizar_texto(self):
        self.result_box.delete("1.0", "end")  # limpia resultados previos

        texto = self.text_input.get("1.0", "end").strip()
        if not texto:
            logger.warning("Intento de análisis de texto vacío")
            return

        resultado = analyze_text(texto)
        self.resultado_actual = resultado
        salida = format_analysis(resultado)
        self.result_box.insert("1.0", salida)

    # =========================
    # ANALIZAR PALABRA
    # =========================
    def analizar_palabra(self):
        self.result_box.delete("1.0", "end")  # limpia resultados previos

        palabra = self.text_input.get("1.0", "end").strip()
        if not palabra:
            logger.warning("Intento de análisis de palabra vacío")
            return

        data = analyze_single_word(palabra)
        lines = [
            "🧠 ANÁLISIS LINGÜÍSTICO\n",
            f"Palabra: {data['word']}",
            f"Sílabas: {'-'.join(data['syllables'])}",
            f"Número de sílabas: {data['syllable_count']}",
            f"Tiene tilde: {'Sí' if data['has_tilde'] else 'No'}",
            f"Tipo de palabra: {data['stress_type']}"
        ]
        salida = "\n".join(lines)
        self.result_box.insert("1.0", salida)

    # =========================
    # EXPORTAR
    # =========================
    def exportar(self):
        contenido = self.result_box.get("1.0", "end").rstrip()  # elimina salto final
        if not contenido:
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text file", "*.txt")]
        )
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write(contenido)

        logger.info(f"Resultados exportados a: {path}")

    # =========================
    # SALIR
    # =========================
    def salir(self):
        sys.exit()


def run_gui():
    logger.info("Aplicación iniciada")
    app = TextAnalyzerGUI()
    app.mainloop()