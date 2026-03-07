# Contador_Palabras_Texto
Uso practico de la IA en programacion con PYTHON

´´´ 
text_analyzer/
├── .gitignore
├── README.md
├── src/
│   └── text_analyzer/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── analyzer.py
│       │   └── utils.py
│       ├── io/
│       │   ├── __init__.py
│       │   ├── file_loader.py
│       │   └── input_handler.py
│       ├── interfaces/        
│       │   ├── __init__.py
│       │   ├── cli.py
│       │   └── gui.py
│       └── app.py
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   ├── test_file_loader.py
│   └── test_cli.py
└── asistencia_ia/
    ├── prompts.md
    ├── decisiones.md
    └── incidencias.md
    └── respuestaDeLaIA.md

´´´
Comandos para probar TODO:

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Tests del core
pytest test/test_analyzer.py -v

# 3. Probar CLI
python -m src.text_analyzer.app

# 4. Probar GUI  
python -m src.text_analyzer.app --gui

# 5. ejecucion
python run.py
