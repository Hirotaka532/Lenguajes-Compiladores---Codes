import re
import os
import tkinter as tk
from tkinter import filedialog

# Diccionario de traducciones
TRADUCCIONES = {
    "int": "entero",
    "float": "flotante",
    "double": "doble",
    "char": "carácter",
    "void": "vacío",
    "if": "si",
    "else": "sino",
    "for": "para",
    "while": "mientras",
    "do": "hacer",
    "return": "retornar",
    "switch": "selección",
    "case": "caso",
    "break": "romper",
    "continue": "continuar",
    "default": "defecto",
    "struct": "estructura",
    "typedef": "tipo_definido",
    "const": "constante",
    "static": "estático",
    "goto": "ir_a",
    "sizeof": "tamaño_de",
    "unsigned": "sin_signo",
    "signed": "con_signo",
    "short": "corto",
    "long": "largo",
    "enum": "enumeración",
    "extern": "externo",
    "union": "unión",
    "volatile": "volátil",
    "register": "registro",
    "auto": "automático",
    "include": "incluir",
    "define": "definir",
    "main": "principal",
    "printf": "imprimir",
    "scanf": "leer"
}


# Función para traducir el código
def traducir_codigo(contenido):
    # Reemplazar solo palabras completas
    for palabra, traduccion in TRADUCCIONES.items():
        contenido = re.sub(rf'\b{palabra}\b', traduccion, contenido)
    return contenido


# Función para seleccionar archivo y traducir
def traducir_archivo():
    # Ventana para seleccionar archivo .c
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo .c",
        filetypes=(("Archivos C", "*.c"), ("Todos los archivos", "*.*"))
    )
    
    if not archivo:
        print("❕ No se seleccionó ningún archivo.")
        return

    print(f"\n🗸 Archivo seleccionado: {archivo}")
    
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            codigo = f.read()
    except Exception as e:
        print(f"✗ Error al leer el archivo: {e}")
        return

    # Traducir el contenido
    traducido = traducir_codigo(codigo)

    # Guardar en la misma carpeta donde está el .py
    ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "traducido.txt")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(traducido)

    # Mostrar resumen
    print("\n🗸 Traducción completada correctamente.")
    print(f"📁 Archivo generado en: {ruta_salida}")
    print("\nEjemplo del resultado traducido (primeras líneas):\n")
    print("\n".join(traducido.splitlines()[:10]))  # Mostrar solo las primeras 10 líneas

# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=============================")
        print("     TRADUCTOR DE C A ESPAÑOL")
        print("=============================")
        print("1. Seleccionar archivo .c y traducir")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            traducir_archivo()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("❕ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":

    menu()
