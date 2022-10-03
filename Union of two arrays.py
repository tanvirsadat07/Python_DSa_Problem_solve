def union(A, B):

    for x in range(len(B)):
        for i in range(len(A)):
            if A[i] == B[x]:
                continue

            else:

                print(A[i], end=" ")


A = [1, 2, 3, 4, 5]
B = [4, 5]
union(A, B)
