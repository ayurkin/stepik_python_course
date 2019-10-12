# n = int(input())
# y = 0
# for x in range(n):
#     y += int(input())
# print(y)

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)

objects = [1, 2, 1, 2, 3]
ans = 0
id_lists = []
for obj in objects:
    id_lists.append(id(obj))

ans = len(set(id_lists))
print(ans)

a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)