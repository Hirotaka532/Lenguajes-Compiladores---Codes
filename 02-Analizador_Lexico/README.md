# Analizador Léxico - Dockerfile

Este proyecto consiste en la implementación de un **analizador léxico** desarrollado en **Python**. Su función principal es reconocer y clasificar los componentes (tokens) de un archivo de configuración de Docker.

---

## 🛠️ Tecnologías y Lógica
* **Lenguaje:** Python.
* **Método:** Uso de expresiones regulares (`re`) para identificar patrones específicos en el texto.
* **Objetivo:** Tokenizar instrucciones de Docker, rutas de archivos y flags.

## 📂 Contenido de la Carpeta
* `lexer.py`: El código fuente principal que realiza el escaneo y análisis.
* **Ejemplos de prueba:** Se incluyen 3 archivos de Dockerfile con diferentes formatos para ver la versatilidad del analizador.
