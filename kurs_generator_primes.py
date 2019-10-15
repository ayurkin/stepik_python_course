import itertools
def primes():


    divisor = 2
    while True:

        while divisor < x:
            if x%divisor == 0:
                print(divisor)
                break
            else:
                divisor = divisor + 1
        yield x




print(list(itertools.takewhile(lambda x: x <= 31, primes())))
