# Выполнить слияние нескольких словарей

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}

res1 = {}

for i in (a, b, c):
    res1.update(i)

print(res1)

res2 = {**a, **b, **c}

print(res2)
