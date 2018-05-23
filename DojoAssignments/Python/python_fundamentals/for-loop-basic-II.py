def biggieSize(arr):
    for i in arr:
        if i > 0:
            arr[arr.index(i)] = "big"
    return arr

# print biggieSize([1, -1, 2, 0])


def countPos(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

# print countPos([-1, 1, 1, 1])

def sumTotal(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def average(arr):
    return sumTotal(arr)/len(arr)

# print average([1, 2, 3, 4, 5])

def length(arr):
    return len(arr)

def min(arr):
    if len(arr) == 0:
        return False
    else:
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
        return min

# print min([])

def max(arr):
    if len(arr) == 0:
        return False
    else:
        max = arr[0]
        for i in arr:
            if i > min:
                max = i
        return max

def ultimateAnalyze(arr):
    dict = {}
    sum = 0
    min = arr[0]
    max = arr[0]
    for i in arr:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    dict['sumTotal'] = sum
    dict['average'] = sum/len(arr)
    dict['min'] = min
    dict['max'] = max
    dict['arrLen'] = len(arr)
    return dict

# print ultimateAnalyze([0, 1, 2, 3, 4])


def reverseList(arr):
    i = 0
    while i < len(arr)/2:
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
        i += 1
    return arr

print reverseList([1, 2, 3, 4, 5])
