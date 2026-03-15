# 🗒️ Devlog 

Registro del proceso de desarrollo, decisiones tomadas y aprendizajes del proyecto.

---

## 🟦 Fase 0 — Base del proyecto

- Agregado `respuestaDeLaIA.md` para documentar el proceso con Perplexity.
- Se cuestionó la primera propuesta de separación de responsabilidades y se aceptó la segunda por ser más convincente.
- Orden de creación definido: `models → utils → analyzer → file_loader → input_handler → cli → app`.
- Decisión de hacer tests robustos por gusto y aprendizaje.
- Cambios de imports manuales para no romper el proyecto durante la migración.
- Revisión de código y documentación antes de continuar.
- No se avanzó hasta tener los tests en orden.
- Cada proyecto se hace distinto a propósito, para practicar errores distintos y entender mejor cómo funciona Python.
- Problema de tests resuelto. Se continúa.
- Con la base lista, se inicia la planificación real. Se agrega `roadmap.md` e imagen del mismo.

---

## 🟨 Fase 1 — Mejora de la terminal

- `run.py` eliminado y reemplazado por `main.py` para evitar dos puntos de arranque distintos.
- Mejora visual de la terminal con **Rich**.

---

## 🟩 Fase 2 — Historial y caché

- Implementación de caché para evitar recalcular textos o palabras ya analizadas.
- Creación del módulo `storage`: `history_manager.py` + `history.json`.
- Modificación de `analizar_texto()` y `analyzer.py` con dos nuevos bloques: consulta de historial y guardado en historial.

**Implementado a petición del usuario:**

- Menú principal con Rich, iconos y colores (`🚀 📂 🖥️ 📜 ❌`).
- Opción de historial rápido visible desde el menú principal.
- Función `resumen_historial()` para compatibilidad entre CLI y GUI.
- `main.py` ejecutable tanto desde VS Code como desde línea de comandos dentro de `src/`.
- Historial dinámico con los últimos 5 análisis, independiente del origen.

**Nota técnica:** La clave del caché es `raw_text` porque el proyecto no requiere escalar a gran volumen. Si se ampliara, se usaría `hash(text)`.

**Acuerdos y desacuerdos durante el desarrollo:**

| | Punto |
|:---:|---|
| ✅ | Mantener menú con Rich y colores |
| ✅ | Historial compartido entre CLI y GUI |
| ✅ | Historial rápido con resumen legible de los últimos análisis |
| ⚠️ | Originalmente se quería que GUI guardara strings como CLI, pero se decidió guardar `AnalysisResult` y resumirlo dinámicamente |

---

## 🟪 Fase 3 — Módulo lingüístico

- Creación de `linguistic.py` para separar el análisis lingüístico de `analyzer.py` y mantener cada módulo con una única responsabilidad.
- La propuesta de la IA fue convincente y se aceptó.

---

## 🏁 Fase Final — Cierre y reflexión

Quedó pendiente refactorizar y terminar el roadmap, pero el proyecto llegó hasta la **Fase 6 de los tests** con la app funcional.

El reto personal fue hacerlo lo más complejo posible a propósito, para entender cómo funciona cada bloque de código. De este proyecto se extrajo más aprendizaje que de los anteriores.

> *"Hare un readme algo sencillo y sin complicaciones."*  
> — MDL, al cerrar el proyecto
