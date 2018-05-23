# Countdown
def countdown(num):
    arr = []
    i = num;
    while i >= 0:
        arr += [i]
        i-=1
    return arr

# print countdown(13)


# Print and Return
def printReturn(arr):
    print arr[0]
    return arr[1]


# First Plus Length
def firstPlusLen(arr):
    return arr[0] + len(arr)


# Values Greater than Second
def greaterThanSec(arr):
    newArr = []
    count = 0
    for i in arr:
        if i > arr[1]:
            newArr += [i]
            count += 1
    print count
    return newArr

# print greaterThanSec([1, 2, 3, 4, 5])

# This Length, That Value
