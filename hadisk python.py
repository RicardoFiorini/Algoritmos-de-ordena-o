def radix_sort(arr):
    max_digit = len(str(max(arr)))

    for i in range(max_digit):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // (10**i)) % 10
            buckets[digit].append(num)

        arr = [item for bucket in buckets for item in bucket]

    return arr

# Exemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
result = radix_sort(arr)
print(result)
