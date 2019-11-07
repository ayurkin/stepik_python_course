import itertools
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

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
