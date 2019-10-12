from collections import deque


def is_parent(class_parent: str, class_child: str, graph):
    distances = {i: None for i in graph}
    if class_child not in graph or class_parent not in graph:
        print("No")
        return None

    start_vertex = class_child  # начинаем с 0 вершины
    distances[start_vertex] = 0  # расстояние до себя равно 0
    queue = deque([start_vertex])  #

    while queue:  # пока очередь не пуста
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                queue.append(neigh_v)

    if not distances[class_parent] is None:
        # print("Yes")
        return 1
    else:
        # print("No")
        return 0

N = int(input())
graph3 = dict()

for i in range(N):
    buf = input().split()
    graph3[buf[0]] = set()
    if(len(buf) > 1):
        graph3[buf[0]].update(buf[2:])
M = int(input())
buf = [None]*M
for i in reversed(range(M)):
    buf[i] = input()

out = []
for i in range(M - 1):
    s = 0
    for j in range(i + 1, M):
        s += is_parent(buf[j], buf[i], graph3)
    if s > 0:
        out.append(buf[i])
for i in reversed(out):
    print(i)

# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError

# 14
# a
# b : a
# c : a
# f : a
# d : c b
# g : d f
# i : g
# m : i
# n : i
# z : i
# e : m n
# y : z
# x : z
# w : e y x
# 9
# y
# m
# n
# m
# d
# e
# g
# a
# f
