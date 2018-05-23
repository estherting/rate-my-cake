def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        if arr[j] > temp:
            while arr[j] > temp and j >= 0:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp
    return arr

print insertionSort([9, 4, 1, 0, 3, 20, -4, 15, 345, -70, 2, 89])
