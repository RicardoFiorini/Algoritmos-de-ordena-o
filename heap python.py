def heap_sort(arr):
    build_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def build_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Exemplo de uso
arr = [4, 10, 3, 5, 1]
result = heap_sort(arr)
print(result)
