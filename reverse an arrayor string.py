def rev(A, start, end):
    if (start > end):
        return
    A[start], A[end] = A[end], A[start]
    start = start + 1
    end = end-1
    rev(A, start, end)


A = [10, 11, 12, 13]

rev(A, 0, 3)
print(A, "ok")
