

def kthsmall(array, position):
    array.sort()
    return (array[position-1])


def kthlarge(array, position):
    array.sort()
    x = len(array)
    return (array[x-position])


A = [10, 5, 25, 44, 00]

p = 1
x = kthsmall(A, p)
print("small", x)
y = kthlarge(A, p)
print("large", y)
