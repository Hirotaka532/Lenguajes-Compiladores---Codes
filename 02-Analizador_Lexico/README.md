# Analizador Léxico - Dockerfile

Este proyecto consiste en la implementación de un **analizador léxico** desarrollado en **Python**. Su función principal es reconocer y clasificar los componentes (tokens) de un archivo de configuración de Docker.

---

## 🛠️ Tecnologías y Lógica
* **Lenguaje:** Python.
* **Método:** Uso de expresiones regulares (`re`) para identificar patrones específicos en el texto.
* **Objetivo:** Tokenizar instrucciones de Docker, rutas de archivos y flags.

## 📂 Contenido de la Carpeta
* `lexer.py`: El código fuente principal que realiza el escaneo y análisis.
* **Ejemplos de prueba:** Se incluyen 3 archivos de Dockerfile con diferentes niveles de complejidad para validar el funcionamiento:
    1. **Ejemplo Básico**: Uso de instrucciones estándar como `FROM` y `RUN`.
    2. **Ejemplo Intermedio**: Configuración de variables de entorno y copiado de archivos.
    3. **Ejemplo Avanzado**: Multi-stage builds o comandos complejos para probar la robustez del lexer.

## 🚀 Cómo ejecutarlo
Para probar el analizador con uno de los ejemplos, ejecuta el siguiente comando en tu terminal:

```bash
python lexer.py nombre_del_archivo_ejemplo
