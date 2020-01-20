def simple_generator():
    print('generate')
    yield 1
    yield 2

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def generator_function(j):
    for i in range(j):
        yield i

for x in fibon(5):
    print(x)

for x in generator_function(5):
    print(x)
