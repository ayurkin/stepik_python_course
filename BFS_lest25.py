from collections import deque

# N, M = map(int, input().split())

graph2 = {'A': {'B', 'C'}, 'B': {'D', 'F'}, 'C': set(), 'D': set(), 'F': set(), 'H': {'F'}}
graph = {'G': 'F',
         'A': set(),
         'B': {'A'},
         'C': {'A'},
         'D': {'B', 'C'},
         'E': {'D'},
         'F': {'D'},
         'X': set(),
         'Y': {'X', 'A'},
         'Z': {'X'},
         'V': {'Z', 'Y'},
         'W': {'V'}}


def is_parent(class_parent: str, class_child: str, graph):
    distances = {i: None for i in graph}
    if class_child not in graph or class_parent not in graph:
        print(False)
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
        print(True)
        return None
    else:
        print(False)
        return None


N = int(input())
graph3 = dict()

for i in range(N):
    buf = input().split()
    graph3[buf[0]] = set()
    if(len(buf) > 1):
        graph3[buf[0]].update(buf[2:])

M = int(input())
for i in range(M):
    buf = input().split()
    is_parent(buf[0], buf[1], graph3)

