def digital_root(n):
    st = str(n)
    st = list(st)
    print(st)
    for i in range(len(st)):
        st[i] = int(st[i])
    c = sum(st)
    if len(str(c)) > 1:
        digital_root(c)
    else:
        return c

print(digital_root(942))