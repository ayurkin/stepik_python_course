s = input()
a = input()
b = input()


if a not in s and a in b:
    print("Impossible")
else:
    i = 0
    while s.count(a) > 0:
        s = s.replace(a, b)
        i += 1
        if i > 1000:
            break
    print(i) if i < 1000 else print("Impossible")
