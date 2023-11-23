import time
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n^2)"

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n^2)"

def selection_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n^2)"

def merge_sort(arr):
    start_time = time.time()

    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort_helper(left_half)
            merge_sort_helper(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    merge_sort_helper(arr)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n log n)"

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    start_time = time.time()

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, low, high)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n^2) - O(n log n)"

def radix_sort(arr):
    start_time = time.time()

    # Encontrar o máximo para saber o número de dígitos
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(nk)"

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def heap_sort(arr):
    start_time = time.time()

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, "O(n log n)"

# Função para gerar gráfico de desempenho
def plot_performance(algorithm_names, execution_times):
    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, execution_times, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
    plt.title("Desempenho dos Algoritmos de Ordenação")
    plt.xlabel("Algoritmo")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.show()

# Função para realizar estudo comparativo
def estudo_comparativo(data):
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Radix Sort': radix_sort,
        'Counting Sort': counting_sort,
        'Heap Sort': heap_sort
    }

    execution_times = []

    print("\nEstudo Comparativo:")
    print("{:<20} {:<20}".format("Algoritmo", "Tempo de Execução (s)"))
    print("-" * 40)

    for algorithm_name, algorithm in algorithms.items():
        start_time = time.time()
        algorithm(data.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        print("{:<20} {:<20.8f}".format(algorithm_name, execution_time))

    # Gráfico de desempenho
    plot_performance(list(algorithms.keys()), execution_times)

# Função principal
def main():
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Radix Sort': radix_sort,
        'Counting Sort': counting_sort,
        'Heap Sort': heap_sort
    }

    print("Escolha um algoritmo de ordenação:")
    for i, algorithm_name in enumerate(algorithms.keys(), start=1):
        print(f"{i}. {algorithm_name}")

    choice = int(input("Digite o número do algoritmo desejado: "))

    algorithm_names = list(algorithms.keys())
    algorithm_name = algorithm_names[choice - 1]

    data = input("Digite os dados separados por espaços: ")
    data = list(map(int, data.split()))

    start_time = time.time()
    algorithms[algorithm_name](data)
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\nDados ordenados pelo {algorithm_name}:")
    print(data)
    print(f"Tempo de execução: {execution_time:.8f} segundos")
    print(f"Complexidade: {algorithms[algorithm_name](data)[1]}")

    # Adiciona o tempo de execução ao gráfico
    plot_performance([algorithm_name], [execution_time])

    # Executa a função estudo_comparativo
    estudo_comparativo(data)

if __name__ == "__main__":
    main()