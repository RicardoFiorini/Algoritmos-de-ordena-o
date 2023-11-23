#include <stdio.h>
#include <stdlib.h>

void countingSort(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    int *count = (int *)malloc((max + 1) * sizeof(int));

    // Inicializa o array de contagem
    for (int i = 0; i <= max; i++) {
        count[i] = 0;
    }

    // Conta as ocorrências de cada elemento
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Calcula as posições corretas
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Constrói a lista ordenada
    int *sortedArray = (int *)malloc(n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        count[arr[i]]--;
        sortedArray[count[arr[i]]] = arr[i];
    }

    // Exibe o resultado ordenado
    for (int i = 0; i < n; i++) {
        printf("%d ", sortedArray[i]);
    }

    free(count);
    free(sortedArray);
}

int main() {
    int arr[] = {4, 2, 4, 1, 0, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    countingSort(arr, n);

    return 0;
}
