def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f(3)
f(3, [1, 2, 3])
f(3)
# f(3)
# f(3)
