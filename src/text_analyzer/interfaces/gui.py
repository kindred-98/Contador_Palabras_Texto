# src/text_analyzer/interfaces/gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from text_analyzer.core.analyzer import analyze_text
from text_analyzer.core.models import AnalysisConfig
from text_analyzer.io.file_loader import read_text_file, write_text_file
from text_analyzer.interfaces.cli import guardar_historial, format_analysis_report

class TextAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Analizador de Texto Profesional")
        self.root.geometry("900x700")
        self.config = AnalysisConfig()
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W,tk.E,tk.N,tk.S))

        ttk.Label(frame,text="📝 Texto a analizar:", font=("Arial",12,"bold")).grid(row=0,column=0,sticky=tk.W,pady=5)
        self.text_input = scrolledtext.ScrolledText(frame,height=10,width=80)
        self.text_input.grid(row=1,column=0,columnspan=3,sticky=(tk.W,tk.E),pady=5)

        ttk.Button(frame,text="📁 Cargar archivo",command=self.load_file).grid(row=2,column=0,padx=5,pady=5)
        ttk.Button(frame,text="🔍 ANALIZAR",command=self.analyze_text,style="Accent.TButton").grid(row=2,column=1,padx=5,pady=5)
        ttk.Button(frame,text="💾 Guardar informe",command=self.save_report).grid(row=2,column=2,padx=5,pady=5)

        ttk.Label(frame,text="📊 RESULTADOS:", font=("Arial",12,"bold")).grid(row=3,column=0,sticky=tk.W,pady=(20,5))
        self.results_text = scrolledtext.ScrolledText(frame,height=15,width=80,state=tk.DISABLED)
        self.results_text.grid(row=4,column=0,columnspan=3,sticky=(tk.W,tk.E,tk.N,tk.S),pady=5)

        ttk.Label(frame,text="Top palabras:").grid(row=5,column=0,sticky=tk.W)
        self.top_n_var = tk.StringVar(value="10")
        ttk.Entry(frame,textvariable=self.top_n_var,width=5).grid(row=5,column=1,sticky=tk.W)

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo .txt",
                                               filetypes=[("Archivos TXT","*.txt"),("Todos","*.*")])
        if file_path:
            try:
                content = read_text_file(file_path)
                self.text_input.delete(1.0,tk.END)
                self.text_input.insert(1.0,content)
            except Exception as e:
                messagebox.showerror("Error",f"No se pudo cargar el archivo:\n{str(e)}")

    def analyze_text(self):
        text = self.text_input.get(1.0,tk.END).strip()
        if not text:
            messagebox.showwarning("Advertencia","Por favor, ingrese texto o cargue un archivo.")
            return
        try:
            top_n = int(self.top_n_var.get() or 10)
            config = AnalysisConfig(top_n=top_n)
            result = analyze_text(text,config)
            report = format_analysis_report(result)

            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0,tk.END)
            self.results_text.insert(1.0,report)
            self.results_text.config(state=tk.DISABLED)

            guardar_historial(report)
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def save_report(self):
        content = self.results_text.get(1.0,tk.END).strip()
        if not content:
            messagebox.showwarning("Advertencia","No hay resultados para guardar.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos TXT","*.txt"),("Todos","*.*")])
        if file_path:
            try:
                write_text_file(file_path,content)
                messagebox.showinfo("Éxito",f"Informe guardado en:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error",f"No se pudo guardar:\n{str(e)}")

def run_gui():
    root = tk.Tk()
    app = TextAnalyzerGUI(root)
    root.mainloop()