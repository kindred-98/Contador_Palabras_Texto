# FASE 0

1. Eh agregado el archivo respuestaDeLaIA.md 
para documentar todo lo posible de perplexity.

2. Luego de que la separacion de responsabiliades que me dio se la 
cuestione me ha cambiado la estructura del proyecto.
Eh aceptado la segunda que me ha dado porque la primera no me convencia.

3. Voy a seguir este orden en la creacion de codigo: models → utils → analyzer → file_loader → input_handler → cli → app.  

4. Decidi hacer los test robustos por gusto.

5. Cambios de import manuales para no romper todo. 

6. Revision del codigo y documentancion. 

7. No avanzo en el proyecto hasta acomodar los test.

8. Cada proyecto lo hago distinto por practicar errores y conocer mas
de como funciona python.

9. Problema resulto de los test, sigo avanzado.

10. Ya que tengo la base del proyecto ahora si comienzo con mi planificacion.
Agrego archivo roadmap.md y imagen del mismo.
Ire implementando cada cosa paso a paso y comentandolo todo.

## FASE 1

11. Eliminacion de run.py por main.py. Se evito tener dos arranques distintos.
12. Mejorando la terminal con rich.

## FASE 2

13. Evitar recalcular textos o palabras que ya fueron analizados.
14. Craecion de storage ( history_manager.py / history.json )
15. Modificacion de analizar_texto()
16. Modificacion de analayzer.py se añadieron bloques nuevo: Consulta de historial, Guardado en historial.

17. Lo que se implementó específicamente a petición del usuario

- Menú principal con Rich, iconos y colores (🚀, 📂, 🖥️, 📜, ❌).
- Opción de Historial rápido visible desde el menú principal.
- Función resumen_historial() para compatibilidad CLI/GUI.
- Mantener main.py ejecutable desde VS Code y desde línea de comandos dentro de src/.
- Historial dinámico con últimos 5 análisis, independiente del origen (CLI o GUI).

18. el cache de la key es raw_text porque no hare el proyecto tan grande, si lo fuera ampliar usaria hash(text)

19. Puntos de acuerdo y desacuerdo

✅ Acuerdo:

- Mantener menú con Rich y colores.
- Historial debe ser compartido entre CLI y GUI.
- Historial rápido debe mostrar resumen legible de los últimos análisis.

⚠️ Desacuerdo / ajuste:

Originalmente querías que GUI guardara strings como CLI, pero decidimos guardar AnalysisResult y resumirlo dinámicamente.
