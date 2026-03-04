# Analizadores Sintácticos (LL y LR)

Esta carpeta contiene el desarrollo práctico sobre gramáticas formales y técnicas de análisis sintáctico aplicadas a expresiones aritméticas. Se presentan dos aproximaciones clásicas: el análisis **Top-Down (Descendente)** y el análisis **Bottom-Up (Ascendente)**.

---

## 📄 Descripción de los Archivos

### 1. Analizador LL(1) (`parser_ll.py`)
Este analizador implementa la técnica de **Descenso Recursivo** de forma manual. 

*   **Gramática:** Se utilizó una gramática transformada para eliminar la **recursión izquierda**, requisito indispensable para los analizadores LL(1).
*   **Funcionamiento:** Procesa la entrada de arriba hacia abajo (Top-Down), expandiendo las reglas de producción basándose en el token actual (*lookahead* de 1).
*   **Lexer:** Incluye un tokenizador interno basado en la librería `re` de Python.

### 2. Analizador LR / LALR (`parser_lr.py`)
Este analizador utiliza la biblioteca **PLY (Python Lex-Yacc)** para implementar un algoritmo LALR(1).

*   **Gramática:** Permite el uso de gramáticas con **recursión izquierda**, lo que resulta en una definición más natural y compacta de las expresiones.
*   **Funcionamiento:** Procesa la entrada de abajo hacia arriba (Bottom-Up), realizando operaciones de "Desplazamiento" (*Shift*) y "Reducción" (*Reduce*) hasta llegar al símbolo inicial.
*   **Precedencia:** Define explícitamente la jerarquía de operadores (multiplicación/división sobre suma/resta).

---

## 🛠️ Requisitos e Instalación

Para ejecutar estos scripts, necesitas tener instalado **Python 3.x** en tu sistema.

### Instalación de Dependencias
El analizador LL no requiere librerías externas. Sin embargo, el analizador LR requiere la instalación de la librería **PLY**:

```bash
pip install ply
```

Nota: Al ejecutar parser_lr.py, la librería PLY generará automáticamente dos archivos: parsetab.py y parser.out. Estos contienen las tablas de estados del autómata y son necesarios para el funcionamiento del analizador.
