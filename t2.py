# Вернуть список, который состоит из элементов, общих для этих списков
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res1 = []
res2 = []
for i in a:
    for j in b:
        if (i == j):
            res1.append(i)

print(res1)

for i in a:
    if i in b:
        res2.append(i)

print(res2)

res3 = list(filter(lambda i: i in b, a))

print(res3)

res4 = list(set(a) & set(b))

print(res4)
