def genPrimes():
    primes = []
    print(primes)  # primes generated so far
    last = 1  # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


# x = genPrimes()
#
# for i in range(30):
#     print(next(x))


def primes():
    x = 1
    while True:
        x += 1
        divisor = 2
        while divisor < x:
            if x % divisor == 0:
                break
            else:
                divisor = divisor + 1
        else:
            yield x

y = primes()


print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

# def is_simple_number(x):
#     divisor = 2
#     while divisor < x:
#         if x%divisor == 0:
#             print(divisor)
#             return print("False")
#         else:
#             divisor = divisor + 1
#     return print("True")
