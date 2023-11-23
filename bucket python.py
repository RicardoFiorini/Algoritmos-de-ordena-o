def bucket_sort(arr):
    bucket_size = 5
    buckets = [[] for _ in range(bucket_size)]

    # Distribui os elementos nos baldes
    for element in arr:
        index = int(element * bucket_size)
        buckets[index].append(element)

    # Ordena cada balde e concatena
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Exemplo de uso
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
result = bucket_sort(arr)
print(result)
