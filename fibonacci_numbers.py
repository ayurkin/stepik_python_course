def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

for k in range(15):
    print(fib(k))

print(fib(4))