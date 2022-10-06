def ok(x):
    count = 0
    for i in x:
        if i % 2 == 0:
            count = count+1
    return count


print(ok([0, 4, 6, 7]))
