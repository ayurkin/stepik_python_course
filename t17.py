def sum_digits(n):
    digits = [int(f) for f in str(n)]
    return sum(digits)


print(sum_digits(123))
