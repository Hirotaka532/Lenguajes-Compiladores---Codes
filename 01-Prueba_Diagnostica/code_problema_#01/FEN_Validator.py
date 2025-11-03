# ============================
#  FEN_Validator.py
#  Descripción:
#  Programa que valida cadenas en notación FEN (Forsyth–Edwards Notation).
#  Permite cargar un archivo .pgn y validar las posiciones generadas,
#  o introducir manualmente una cadena FEN para su verificación.
# ============================

import re
import chess.pgn
import tkinter as tk
from tkinter import filedialog

# FUNCIÓN PRINCIPAL DE VALIDACIÓN DE CADENA FEN
def validar_fen(fen):
    partes = fen.strip().split()

    if len(partes) != 6:
        print("✗ FEN inválida: debe tener 6 secciones separadas por espacios.")
        return False

    posiciones, turno, enroque, en_passant, halfmove, fullmove = partes

    # 1. Validar la sección de posiciones
    filas = posiciones.split('/')
    if len(filas) != 8:
        print("✗ FEN inválida: deben existir 8 filas separadas por '/'.")
        return False

    piezas_validas = re.compile(r"^[prnbqkPRNBQK1-8]+$")

    for i, fila in enumerate(filas, start=1):
        if not piezas_validas.match(fila):
            print(f"✗ FEN inválida: caracteres no permitidos en la fila {i}.")
            return False

        # Contar las casillas totales en la fila
        contador = 0
        for c in fila:
            if c.isdigit():
                contador += int(c)
            else:
                contador += 1
        if contador != 8:
            print(f"✗ FEN inválida: la fila {i} no tiene 8 casillas exactas ({contador}).")
            return False

    # 2. Validar turno (solo w o b)
    if turno not in ['w', 'b']:
        print("✗ FEN inválida: el turno debe ser 'w' o 'b'.")
        return False

    # 3. Validar enroque
    if enroque != '-' and not re.fullmatch(r'[KQkq]+', enroque):
        print("✗ FEN inválida: derechos de enroque incorrectos.")
        return False

    # 4. Validar en passant
    if en_passant != '-' and not re.fullmatch(r'[a-h][36]', en_passant):
        print("✗ FEN inválida: casilla en passant incorrecta.")
        return False

    # 5. Validar contadores numéricos
    if not (halfmove.isdigit() and fullmove.isdigit()):
        print("✗ FEN inválida: los contadores deben ser números enteros.")
        return False

    print("🗸 FEN válida.")
    return True

# FUNCIÓN PARA LEER ARCHIVO PGN Y VALIDAR FEN DE UNA PARTIDA ESPECÍFICA
def validar_fen_desde_pgn(ruta_archivo):
    try:
        partidas = []
        with open(ruta_archivo, encoding="utf-8") as pgn:
            partida = chess.pgn.read_game(pgn)
            while partida:
                partidas.append(partida)
                partida = chess.pgn.read_game(pgn)

        if not partidas:
            print("❕ No se encontraron partidas en el archivo PGN.")
            return

        # Mostrar resumen de las partidas
        print("\nPartidas disponibles en el archivo:")
        for idx, p in enumerate(partidas, start=1):
            white = p.headers.get('White', '?')
            black = p.headers.get('Black', '?')
            result = p.headers.get('Result', '?')
            print(f"{idx}. {white} vs {black} ({result})")

        # Pedir al usuario que seleccione una
        while True:
            seleccion = input(f"Seleccione una partida (1-{len(partidas)}): ")
            if seleccion.isdigit() and 1 <= int(seleccion) <= len(partidas):
                partida = partidas[int(seleccion)-1]
                break
            else:
                print("❕ Opción no válida. Intente de nuevo.")

        # Validar FENs de la partida seleccionada
        tablero = partida.board()
        print(f"\n Validando partida: {partida.headers.get('White', '?')} vs {partida.headers.get('Black', '?')}")
        for i, movimiento in enumerate(partida.mainline_moves(), start=1):
            tablero.push(movimiento)
            fen_actual = tablero.fen()
            print(f"\nJugada {i}: {movimiento}")
            print(f"FEN: {fen_actual}")
            validar_fen(fen_actual)

    except FileNotFoundError:
        print("✗ Archivo no encontrado. Asegúrate de colocar el .pgn en la misma carpeta o dar la ruta completa.")
    except Exception as e:
        print(f"✗ Error al procesar el archivo: {e}")

# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=============================")
        print("  VALIDACIÓN DE NOTACIÓN FEN")
        print("=============================")
        print("1. Cargar archivo .pgn y validar FENs")
        print("2. Introducir una cadena FEN manualmente")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Abrir ventana para seleccionar archivo
            root = tk.Tk()
            root.withdraw()  # Oculta la ventana principal
            archivo = filedialog.askopenfilename(
                title="Selecciona un archivo .pgn",
                filetypes=(("Archivos PGN", "*.pgn"), ("Todos los archivos", "*.*"))
            )
            if archivo:
                print(f"🗸 Archivo seleccionado: {archivo}")
                validar_fen_desde_pgn(archivo)
            else:
                print("❕ No se seleccionó ningún archivo.")
        elif opcion == "2":
            cadena = input("Introduzca la cadena FEN: ")
            validar_fen(cadena)
        elif opcion == "3":
            print("Saliendo... ")
            break
        else:
            print("❕ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()