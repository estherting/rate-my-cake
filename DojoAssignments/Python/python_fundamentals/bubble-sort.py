def bubbleSort(arr):
    for i in range(1, len(arr)):
        j = 0
        while j < len(arr)-i:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

print bubbleSort([3, 4, 2, -1, 0])
