#include <stdio.h>

float calcularPromedio(float notas[], int cantidad) {
    float suma = 0;
    for(int i = 0; i < cantidad; i++) {
        suma += notas[i];
    }
    return suma / cantidad;
}

int main() {
    int n;
    printf("Ingrese el numero de estudiantes: ");
    scanf("%d", &n);

    float notas[n];
    for(int i = 0; i < n; i++) {
        printf("Nota %d: ", i + 1);
        scanf("%f", &notas[i]);
    }

    float promedio = calcularPromedio(notas, n);
    printf("El promedio del grupo es: %.2f\n", promedio);

    return 0;
}