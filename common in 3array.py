def common(A, B, C, x, y, z):
    i = 0
    j = 0
    k = 0
    while (x > i and y > j and z > k):
        if (A[i] == B[j] and A[i] == C[k]):
            print(A[i])
            i += 1
            j += 1
            k += 1
        elif B[j] > A[i]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1


A = [10, 0, 70]
B = [10, 0, 70]
C = [0, 10, 70]
A.sort()
B.sort()
C.sort()
a = len(A)
b = len(B)
c = len(C)
common(A, B, C, a, b, c)
