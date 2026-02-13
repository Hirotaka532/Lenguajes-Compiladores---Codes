import re
import tkinter as tk
from tkinter import filedialog

# Definición de tokens
TOKENS = [
    ('TK_FROM',      r'\bFROM\b'),
    ('TK_RUN',       r'\bRUN\b'),
    ('TK_ENV',       r'\bENV\b'),
    ('TK_COPY',      r'\bCOPY\b'),
    ('TK_WORKDIR',   r'\bWORKDIR\b'),
    ('TK_CMD',       r'\bCMD\b'),
    ('TK_EXPOSE',    r'\bEXPOSE\b'),
    ('TK_IMAGE',     r'[a-zA-Z0-9._/-]+:[a-zA-Z0-9._-]+'),
    ('TK_NUMBER',    r'\b\d+\b'),
    ('TK_STRING',    r'"[^"]*"'),
    ('TK_PATH',      r'/(?:[a-zA-Z0-9._/-]+)?'), # Rutas que empiezan con /
    
    # Cosas que no se guardan en la lista de salida
    ('SKIP_SPACE',   r'[ \t\r\f]+'),
    ('SKIP_COMMENT', r'#.*'),
    ('SKIP_SYMBOLS', r'[\[\],\.\-]'), # Corchetes, puntos, comas, guiones
    ('SKIP_ARGS',    r'\b[a-z][a-z0-9._-]*\b'), # Palabras en minúscula como apt-get, update
    ('NEWLINE',      r'\n'),
    
    # Cualquier palabra que empiece con Mayúscula o tenga números y no sea un Keyword
    ('TK_ERROR_CMD', r'\b[A-Z0-9_]+\b'), 
    ('MISMATCH',     r'.'), 
]

def lexer(text):
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS)
    line_num = 1
    line_start = 0
    
    tokens_a_imprimir = [] # Lista temporal para guardar tokens si todo sale bien

    for match in re.finditer(token_regex, text):
        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start

        if kind == 'NEWLINE':
            line_num += 1
            line_start = match.end()
        elif kind.startswith('SKIP'):
            continue # Ignoramos completamente
        elif kind == 'TK_ERROR_CMD' or kind == 'MISMATCH':
            # SI HAY ERROR: Imprimimos y cortamos la ejecución (return)
            print(f"ERROR LÉXICO: Comando o palabra no reconocida '{value}' (línea {line_num}, columna {column})")
            return 
        else:
            # Si es un token válido, lo guardamos para el final
            tokens_a_imprimir.append(f"TOKEN: {kind} -> {value}")

    # Si llegamos aquí, no hubo errores, imprimimos la lista
    for t in tokens_a_imprimir:
        print(t)

def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def seleccionar_dockerfile():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    ruta = filedialog.askopenfilename(
        title="Seleccionar Dockerfile",
        filetypes=[("Dockerfile", "*"), ("Todos los archivos", "*.*")]
    )
    root.destroy()
    return ruta

if __name__ == "__main__":
    print("--- Analizador Léxico para Dockerfiles ---")
    while True:
        archivo = seleccionar_dockerfile()
        if not archivo:
            print("\nNo se seleccionó ningún archivo.")
        else:
            contenido = leer_archivo(archivo)
            if contenido:
                print(f"\nAnalizando: {archivo}\n")
                lexer(contenido)

        respuesta = input("\n¿Desea analizar otro archivo? (s/n): ").lower().strip()
        if respuesta != 's':
            break
