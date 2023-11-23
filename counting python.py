def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    # Conta as ocorrências de cada elemento
    for num in arr:
        count[num] += 1

    # Calcula as posições corretas
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    # Constrói a lista ordenada
    sorted_array = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        sorted_array[count[num]] = num

    return sorted_array

# Exemplo de uso
arr = [4, 2, 4, 1, 0, 2, 1]
result = counting_sort(arr)
print(result)
