numbers = [5, 1, 10, 15, 30, 45, 60, 55, 16]

b = list(filter(lambda x: not x%15, numbers))

print(b)
