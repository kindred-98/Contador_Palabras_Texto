<!-- markdownlint-disable MD032 -->

# 🗺 Roadmap Profesional – Text Analyzer

## Fase 0 – Base (ya implementada)
✅ Objetivo: Tener un proyecto funcional y testeado.

- Arquitectura modular (core, io, interfaces)
- CLI básico funcional
- Funciones de análisis de texto: palabras, caracteres, oraciones, párrafos
- Tests unitarios con pytest
- Normalización de texto confiable (normalize_text)

Resultado esperado: todos los tests pasan, CLI mínimo funcional, código limpio.

## Fase 1 – Mejoras en CLI y experiencia usuario
🎯 Objetivo: Hacer la app más legible y profesional en la terminal.

1. Crear un menú interactivo para seleccionar modo:
´´´
1) Analizar texto
2) Analizar palabra
3) Ver historial
4) Exportar resultados
5) Salir
´´´
2. guiada para analizar palabras individuales.
3. Usar librería de terminal para mejorar presentación:
- Rich (Python library) – tablas, colores
- Indicadores visuales de progreso o separación de secciones
4. Mejorar la salida de análisis de texto:
- 📝 Número de palabras, caracteres, oraciones, párrafos
- 🏆 Top N palabras con frecuencia
- Distinción visual entre datos principales y secundarios

Resultado esperado: CLI limpio, comprensible, atractivo visualmente.

## Fase 2 – Historial y persistencia
🎯 Objetivo: Evitar recalcular palabras o textos ya analizados.

1. Implementar módulo history_manager.py en storage/.
2. Guardar resultados de palabras y textos en JSON o SQLite.
3. Flujo de análisis:
- Si palabra/texto existe → leer del historial
- Si no existe → generar análisis y guardar
- Permitir consultar historial desde el CLI.

Resultado esperado: app recuerda todos los análisis previos, mejora velocidad y experiencia.


## Fase 3 – Análisis lingüístico de palabras
🎯 Objetivo: Analizar cada palabra más a fondo.

1. Dividir palabras en sílabas.
2. Determinar tipo de palabra (aguda, grave, esdrújula, sobresdrújula).
3. Detectar acento escrito (tilde) y número de sílabas.
4. Guardar análisis lingüístico en historial.

Resultado esperado: palabras analizadas con información completa, usable desde historial.


## Fase 4 – Exportación de resultados
🎯 Objetivo: Permitir guardar y compartir análisis.

1. Exportar análisis a:
- CSV
- TXT
- JSON
2. Permitir exportar solo historial, solo resultado actual o ambos.
3. Añadir timestamp a los archivos exportados.

Resultado esperado: usuario puede guardar, revisar y compartir resultados fácilmente.


## Fase 5 – GUI básica (opcional pero profesional)
🎯 Objetivo: Proveer una interfaz visual para usuarios menos técnicos.

1. Usar librería simple: Tkinter o CustomTkinter
2. Mostrar análisis de texto en tablas y paneles.
3. Permitir selección de archivo, entrada de texto y palabra individual.
4. Guardar historial y exportar desde GUI.

Resultado esperado: GUI funcional y coherente con la CLI, reutilizando lógica del backend.


## Fase 6 – Optimización y escalabilidad

🎯 Objetivo: Proyectos grandes requieren código eficiente y mantenible.

1. Añadir logging profesional (logging module)
2. Manejar errores y excepciones con mensajes claros
3. Mejorar tests:
- Cobertura de tests ≥ 95% (pytest-cov)
- Tests de CLI y GUI
- Casos de borde: texto vacío, espacios, caracteres especiales
4. Refactorizar módulos para mantener principio de responsabilidad única
5. Documentación profesional:
- README con instalación, ejemplos, screenshots
- sistencia_ia/ actualizado con decisiones y prompts

Resultado esperado: proyecto estable, testeable, profesional y listo para portfolio.

## Fase 7 – Extras opcionales (destacan en GitHub)

1. Añadir análisis avanzado:
- Longitud media de palabras
- Densidad de palabras clave
- Nube de palabras (ASCII o GUI)
2. Integración con API externa (opcional):
- Por ejemplo, para corrección ortográfica o análisis de sentimiento.
3. Versionado de historial con timestamps y hashes, para asegurar integridad.


## 💡 Tip senior

- Cada fase debe ser autocontenida y testeable.
- No mezclar CLI, GUI y lógica antes de tener tests robustos.
- Mantener código limpio y modular: core no debe depender de GUI/CLI.
- Cada feature nueva → test unitario + test de integración.
- Documentar cada decisión y mantener historial de cambios.


## ROADMAP VISUAL
![alt text](<ChatGPT Image 8 mar 2026, 22_30_40.png>)

## ESTRUCTURA BASICA INICIAL ANTES DE COMENZAR CON EL ROADMAP
![alt text](image.png)

## PRUEBA DE QUE TODO PASA, ANTES DE COMENZAR A APLICAR CAMBIOS.
![alt text](<Captura de pantalla 2026-03-08 235759.png>)

## INTERFAZ DE INICIO ACTUALIZADA
![alt text](<Captura de pantalla 2026-03-12 105619.png>)
![alt text](<Captura de pantalla 2026-03-12 105642.png>)
![alt text](<Captura de pantalla 2026-03-12 105825.png>)
![alt text](<Captura de pantalla 2026-03-12 105852.png>)
![alt text](<Captura de pantalla 2026-03-12 110446.png>)
![alt text](image.png)
![alt text](<Captura de pantalla 2026-03-15 002031.png>)