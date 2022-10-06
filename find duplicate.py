A = [1, 2, 3, 4, 5, 6, 4]
B = [4, 5]


for i in range(0, len(A)):
    for j in range(0, len(B)):
        if A[i] == B[j]:
            continue
        elif A[i] != B[j]:
            print(A[i], end=" ")
