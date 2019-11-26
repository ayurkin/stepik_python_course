s = input()
t = input()
i = 0
count = 0
while not s.find(t, i) == -1:
    i = s.find(t, i) + 1
    count += 1
else:
    print(count)