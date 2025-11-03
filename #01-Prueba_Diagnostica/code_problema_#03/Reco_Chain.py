# ============================
#  Reco_chain.py
#  Descripción:
#  Programa para reconocer tipos de cadenas:
#    - Notación científica (ej: 2.5e-10)
#    - Dirección IP (ej: 192.168.0.1)
#    - Correo electrónico (ej: nombre@dominio.com)
#  Permite ingresar cadenas desde consola y muestra a qué tipo pertenece.
# ============================

import re

# Expresiones regulares
regex_cientifica = r'^\d+(\.\d+)?[eE][+-]?\d+$'
regex_ip = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def verificar_cadena(cadena):
    if re.match(regex_cientifica, cadena):
        return "Notación científica"
    elif re.match(regex_ip, cadena):
        return "Dirección IP"
    elif re.match(regex_email, cadena):
        return "Correo electrónico"
    else:
        return "Cadena inválida: no coincide con los formatos requeridos"

def menu():
    print("===============================")
    print("  RECONOCIMIENTO DE CADENAS    ")
    print("===============================")

    while True:
        print("\nOpciones:")
        print("1. Ingresar una cadena")
        print("2. Salir")
        opcion = input("Selecciona una opción (1-2): ").strip()

        if opcion == '2':
            print("Saliendo del programa...")
            break
        elif opcion == '1':
            cadena = input("Ingresa la cadena a verificar: ").strip()
            resultado = verificar_cadena(cadena)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida, ingresa 1 o 2.")

if __name__ == "__main__":
    menu()