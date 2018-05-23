def selectionSort(arr):
    i = 0
    while i < len(arr)-1:
        j = i
        min = arr[i]
        while j < len(arr)-1:
            if arr[j] < min:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr

print selectionSort([1, 3, 0, 5, 4, 9])
