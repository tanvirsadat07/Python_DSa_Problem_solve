def solution(A, K):
    old = A
    new = [0]*len(A)
    for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy()  # This was the problematic line
    return


A = [10, 11, 12, 13]
solution(A, 4)
print(A)
