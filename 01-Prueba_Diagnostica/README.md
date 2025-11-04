# Prueba Diagnóstica

Esta carpeta contiene los códigos de la **Prueba Diagnóstica**. 
Se resolvieron 4 ejercicios de programación y análisis de cadenas en distintos lenguajes.  
Cada ejercicio está organizado en su propia subcarpeta `code_problema_#01` hasta `code_problema_#04`.

---

## 📋 Requisitos

### Python
Para instalar las dependencias de Python necesarias, ejecuta:

```bash
pip install chess python-tkinter
```

| Librería | Descripción |
|----------|-------------|
| `re` | Expresiones regulares (incluida en Python) |
| `chess` | Notación FEN y ajedrez |
| `tkinter` | Interfaz gráfica (incluida en Python) |
| `time` | Medición de tiempo (incluida en Python) |
| `os` | Operaciones del sistema (incluida en Python) |


### JavaScript / Node.js
Para instalar las dependencias de JavaScript, ejecuta:

```bash
# con npm
npm install prompt-sync

# con yarn
yarn add prompt-sync

# con pnpm
pnpm add prompt-sync
```

| Librería | Descripción |
|----------|-------------|
| `fs` | Sistema de archivos (incluida en Node.js) |
| `path` | Rutas de archivos (incluida en Node.js) |
| `prompt-sync` | Entrada de usuario en consola |

---

## 📁 Contenido de los ejercicios

### 1️⃣ Problema 01 – Validador FEN (`code_problema_#01`)
**Lenguaje:** Python  
**Librerías:** `re`, `chess.pgn`, `tkinter`  

**Descripción:**  
Valida cadenas en **notación FEN** para tableros de ajedrez. Permite cargar archivos `.pgn` y verificar posiciones 
o introducir manualmente cadenas FEN. Incluye menú interactivo y validación paso a paso.

---

### 2️⃣ Problema 02 – Polinomio de Pascal (`code_problema_#02`)
**Lenguajes:** Python y JavaScript  
**Librerías:** Python: `time`, `os`; JavaScript: `fs`, `path`, `prompt-sync`  

**Descripción:**  
Genera los coeficientes del polinomio `(x+1)^n` usando el **Triángulo de Pascal**, muestra el polinomio completo, evalúa `f(x)` paso a paso y mide el tiempo de ejecución. 
Los resultados se guardan en archivos de texto (`resultados_py.txt` o `resultados_js.txt`).

---

### 3️⃣ Problema 03 – Reconocimiento de cadenas (`code_problema_#03`)
**Lenguaje:** Python  
**Librerías:** `re`  

**Descripción:**  
Identifica cadenas que correspondan a **notación científica**, **direcciones IP** o **correos electrónicos**. 
Permite ingreso desde consola y devuelve el tipo de cadena o un aviso de inválida.

---

### 4️⃣ Problema 04 – Traductor de C (`code_problema_#04`)
**Lenguaje:** Python  
**Librerías:** `re`, `os`, `tkinter`  

**Descripción:**  
Lee un programa escrito en C y detecta palabras reservadas para generar una versión traducida al español. 
Permite seleccionar archivos `.c` mediante menú interactivo y guarda la traducción en un archivo `traducido.txt`.

---

> Cada subcarpeta contiene los códigos y archivos de salida correspondientes.

---

## 🔗 Link de la defensa

[Acceder a la defensa](AQUÍ_PON_TU_LINK)
