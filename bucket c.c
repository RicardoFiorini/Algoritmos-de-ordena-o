#include <stdio.h>
#include <stdlib.h>

void bucketSort(double arr[], int n) {
    const int bucketSize = 5;
    double *buckets[bucketSize];

    // Inicializa os baldes
    for (int i = 0; i < bucketSize; i++) {
        buckets[i] = (double *)malloc(n * sizeof(double));
    }

    // Distribui os elementos nos baldes
    for (int i = 0; i < n; i++) {
        int index = arr[i] * bucketSize;
        buckets[index][i] = arr[i];
    }

    // Ordena cada balde e concatena
    int sortedIndex = 0;
    for (int i = 0; i < bucketSize; i++) {
        qsort(buckets[i], n, sizeof(double), compare);
        for (int j = 0; j < n; j++) {
            if (buckets[i][j] != 0) {
                arr[sortedIndex++] = buckets[i][j];
            }
        }
        free(buckets[i]);
    }
}

int compare(const void *a, const void *b) {
    return (*(double *)a - *(double *)b);
}

int main() {
    double arr[] = {0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51};
    int n = sizeof(arr) / sizeof(arr[0]);

    bucketSort(arr, n);

    // Exibe o resultado ordenado
    for (int i = 0; i < n; i++) {
        printf("%f ", arr[i]);
    }

    return 0;
}
