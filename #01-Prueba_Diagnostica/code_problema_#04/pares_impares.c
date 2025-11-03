#include <stdio.h>

int main() {
    int numeros[5];
    int i;

    printf("Ingrese 5 numeros enteros:\n");
    for(i = 0; i < 5; i++) {
        scanf("%d", &numeros[i]);
    }

    printf("\nResultados:\n");
    for(i = 0; i < 5; i++) {
        if(numeros[i] % 2 == 0) {
            printf("%d es par\n", numeros[i]);
        } else {
            printf("%d es impar\n", numeros[i]);
        }
    }

    return 0;
}