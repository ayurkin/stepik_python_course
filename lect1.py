def is_simple_number(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            print(divisor)
            return print("False")
        else:
            divisor = divisor + 1
    return print("True")


is_simple_number(7)


def factorize_number(x):
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            x //= divisor
            print(divisor)
        else:
            divisor += 1


factorize_number(10)
