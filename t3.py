# Отсортировать словарь по значению в порядке возрастания и убывания
import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

res1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
res2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print(res1)
print(res2)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
res3 = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

print(res3)  # {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
