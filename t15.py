a = ['a', 'b', 'c', 'f', 'i']
b = ['a', 'b', 'c', 'e', 'i']

a_set = set(a)
b_set = set(b)

print(a_set - b_set)

print(a_set.difference(b_set))
