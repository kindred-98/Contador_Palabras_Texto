# 🗺️ Roadmap Profesional — Text Analyzer

---

## Fase 0 — Base del proyecto
**✅ Completada**

Objetivo: tener un proyecto funcional y testeado antes de agregar funcionalidades.

- Arquitectura modular: `core`, `io`, `interfaces`
- CLI básico funcional
- Funciones de análisis: palabras, caracteres, oraciones, párrafos
- Tests unitarios con pytest
- Normalización de texto confiable (`normalize_text`)

**Resultado:** todos los tests pasan, CLI mínimo funcional, código limpio.

---

## Fase 1 — Mejoras en CLI y experiencia de usuario
**✅ Completada**

Objetivo: hacer la app más legible y profesional en la terminal.

- Menú interactivo con 5 opciones: Analizar texto, Analizar palabra, Ver historial, Exportar resultados, Salir
- Entrada guiada para analizar palabras individuales
- Integración de Rich: tablas, colores, separadores visuales
- Salida mejorada: top N palabras con frecuencia, distinción visual entre datos principales y secundarios

**Resultado:** CLI limpio, comprensible y atractivo visualmente.

---

## Fase 2 — Historial y persistencia
**✅ Completada**

Objetivo: evitar recalcular palabras o textos ya analizados.

- Módulo `history_manager.py` en `storage/`
- Guardado de resultados en JSON
- Flujo de análisis: si existe en historial → leer; si no → analizar y guardar
- Consulta de historial desde la CLI

**Resultado:** la app recuerda todos los análisis previos, mejora velocidad y experiencia.

---

## Fase 3 — Análisis lingüístico de palabras
**✅ Completada**

Objetivo: analizar cada palabra más a fondo.

- División en sílabas
- Tipo de palabra: aguda, grave, esdrújula, sobresdrújula
- Detección de tilde y número de sílabas
- Guardado del análisis lingüístico en historial

**Resultado:** palabras analizadas con información completa, accesible desde el historial.

---

## Fase 4 — Exportación de resultados
**✅ Completada**

Objetivo: permitir guardar y compartir análisis.

- Exportación a CSV, TXT y JSON
- Opción de exportar historial, resultado actual o ambos
- Timestamp automático en los nombres de archivo generados

**Resultado:** el usuario puede guardar, revisar y compartir resultados fácilmente.

---

## Fase 5 — GUI básica
**✅ Completada**

Objetivo: interfaz visual para usuarios menos técnicos.

- Librería: CustomTkinter
- Tablas y paneles para mostrar resultados
- Selección de archivo, entrada de texto y análisis de palabra individual
- Historial y exportación disponibles desde la GUI
- Lógica de backend reutilizada sin duplicar código

**Resultado:** GUI funcional y coherente con la CLI.

---

## Fase 6 — Optimización y estabilidad
**✅ Completada**

Objetivo: código eficiente, mantenible y listo para portafolio.

- Logging profesional con el módulo `logging`
- Manejo de errores con mensajes claros al usuario
- Tests mejorados: cobertura ~88%, tests de CLI y GUI, casos de borde
- Refactorización para mantener responsabilidad única por módulo
- Documentación: README completo, `asistencia_ia/` actualizado

**Resultado:** proyecto estable, testeable y profesional.

---

## Fase 7 — Documentación de tests
**✅ Completada**

Objetivo: documentar exhaustivamente el proceso de pruebas.

- Decisiones del desarrollador y acuerdos con la IA
- Incidencias detectadas y soluciones implementadas
- Flujo de testeo paso a paso
- Resolución del error `_tkinter.TclError` mediante mocking

**Resultado:** proceso de testing documentado para referencia futura.

---

## 💡 Principios aplicados durante el desarrollo

- Cada fase autocontenida y testeable antes de pasar a la siguiente
- `core` sin dependencias de GUI ni CLI
- Cada feature nueva acompañada de test unitario
- Decisiones documentadas en `asistencia_ia/`

---

## Extras opcionales (Fase 8 — Futura)

Ideas para continuar el proyecto:

- Longitud media de palabras y densidad de palabras clave
- Nube de palabras en ASCII o GUI
- Integración con API externa (corrección ortográfica, análisis de sentimiento)
- Versionado de historial con timestamps y hashes

---

## 📸 Capturas del proyecto

**Roadmap visual**
![Roadmap](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/Roadmap.png)

**Estructura inicial antes del roadmap**
![Arquitectura inicial](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/Arquictectura_inicial.png)

**Tests pasando antes de comenzar cambios**
![Tests pasando](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/PruebasDe_QueTodoPasa.png)

**Interfaz de inicio actualizada**

![Interfaz de inicio](image.png)

![Usar CLI](https://github.com/kindred-98/Contador_Palabras_Texto/blob/73d01104824439745dab0d5f5bb38be38c4a3237/asistencia_IA/IMG/1-Usar_CLI.png)
![GUI actualizada](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0ee6a3defc958166d8b49bc397b37093f4f3f018/asistencia_IA/IMG/GUI_Actualizado.png)
![Ver historial](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/3-Ver_historial_rapido.png)
![Salir](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/4-Salir.png)