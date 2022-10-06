def union(a, b):
    map = {}

    for x in a:
        map[x] = True
    for i in b:
        if i not in map:
            a.append(i)
    return a


a = [1, 2, 3, 4, 10]
b = [2, 3]
print(union(a, b))
