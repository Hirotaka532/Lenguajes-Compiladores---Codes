# ============================
#  Poli_Pascal.py
#  Descripción:
#  Genera los coeficientes del polinomio (x+1)^n usando el Triángulo de Pascal.
#  Evalúa f(x) = (x+1)^n paso a paso y mide el tiempo de ejecución.
#  Guarda los resultados en resultados.txt
# ============================

import time
import os

# Función para Generar los coeficientes del Triángulo de Pascal
def generar_coeficientes(n):
    pascal = [[1] * (i + 1) for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal[n]

# Función para Mostrar el polinomio generado
def mostrar_polinomio(coef):
    n = len(coef) - 1
    partes = []
    for i, c in enumerate(coef):
        exp = n - i
        if exp > 1:
            partes.append(f"{c}x^{exp}" if c != 1 else f"x^{exp}")
        elif exp == 1:
            partes.append(f"{c}x" if c != 1 else "x")
        else:
            partes.append(str(c))
    return " + ".join(partes)

# Función para Evaluar el polinomio paso a paso
def evaluar_polinomio(coef, x):
    n = len(coef) - 1
    pasos = []
    total = 0
    for i, c in enumerate(coef):
        exp = n - i
        valor = c * (x ** exp)
        pasos.append(f"{c}*(x^{exp}) = {valor}")
        total += valor
    return pasos, total

# PROGRAMA PRINCIPAL
def main():
    print("===============================")
    print("  POLINOMIO DE PASCAL (x+1)^n ")
    print("===============================")

    try:
        n = int(input("Ingrese el valor de n: "))
        x = float(input("Ingrese el valor de x: "))
    except ValueError:
        print("✗ Entrada inválida. Use números enteros o decimales.")
        return

    inicio = time.time()

    coeficientes = generar_coeficientes(n)
    polinomio = mostrar_polinomio(coeficientes)
    pasos, resultado = evaluar_polinomio(coeficientes, x)

    fin = time.time()
    duracion = fin - inicio

    # Mostrar resultados en consola
    print(f"\nCoeficientes del polinomio: {coeficientes}")
    print(f"(x+1)^{n} = {polinomio}")

    print("\nCálculo paso a paso:")
    for p in pasos:
        print(" ", p)
    print(f"\nResultado final: f({x}) = {resultado}")
    print(f"\n🕔 Tiempo de ejecución: {duracion:.6f} segundos")

    # Guardar resultados en archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), "resultados_py.txt")
    with open(ruta_archivo, "a", encoding="utf-8") as f:
        f.write(f"\n--- Resultados para n={n}, x={x} ---\n")
        f.write(f"Coeficientes: {coeficientes}\n")
        f.write(f"Polinomio: (x+1)^{n} = {polinomio}\n")
        f.write("Cálculo paso a paso:\n")
        for p in pasos:
            f.write(f"  {p}\n")
        f.write(f"Resultado final: f({x}) = {resultado}\n")
        f.write(f"Tiempo de ejecución: {duracion:.6f} segundos\n")
        f.write("-" * 40 + "\n")

    print("\n🗸 Resultados guardados en 'resultados_py.txt'")

if __name__ == "__main__":
    main()