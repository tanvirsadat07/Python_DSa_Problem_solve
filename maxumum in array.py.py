# Maximum and minimum of an array


def maximum(arr):

    max = arr[0]
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]

    print("max", max)


def minimum(arr):
    min = arr[0]
    for i in range(len(arr)):
        if (arr[i] < min):
            min = arr[i]

    print("min", min)


A = [10, 11, 12, 55]
maximum(A)
minimum(A)
