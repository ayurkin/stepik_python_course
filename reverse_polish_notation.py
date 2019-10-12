import A_stack
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}
def calc_reverse_polish_notation(list):
    """
    Вычисляет выражегие записанное
    в обратной польской нотации
    >>> calc_reverse_polish_notation([2, 4, '+'])
    6
    >>> calc_reverse_polish_notation([2, 7, 5, '*', '+'])
    37
    >>> calc_reverse_polish_notation([2, 7, '-'])
    -5
    """

    for token in list:
        if type(token) == int:
            A_stack.push(token)
        else:
            y = A_stack.pop()
            x = A_stack.pop()
            z = operations[token](x, y)
            A_stack.push(z)

    return A_stack.pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# print(calc_reverse_polish_notation([2, 7, '-']))
# print(calc_reverse_polish_notation([2, 7, 5, '*', '+']))