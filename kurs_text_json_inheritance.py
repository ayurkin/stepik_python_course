from collections import deque
import json


def get_parent(graph, class_name):
    global result_parent_numbers
    distances = {i: None for i in graph}

    start_vertex = class_name  # начинаем с 0 вершины
    distances[start_vertex] = 0  # расстояние до себя равно 0
    queue = deque([start_vertex])  #

    while queue:  # пока очередь не пуста
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                queue.append(neigh_v)

    for p in distances:
        if not distances[p] is None and distances[p] > 0:
            result_parent_numbers[p] += 1



# json_input = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# data_from_input_json = json.loads(json_input)
data_from_input_json = json.loads(input())

graph4 = dict()
result_parent_numbers = dict()

for d in data_from_input_json:
    graph4[d['name']] = d['parents']
    result_parent_numbers[d['name']] = 1

for point in graph4:
    get_parent(graph4, point)

result_parent_numbers_list = []

for point in result_parent_numbers:
    result_parent_numbers_list.append(str(point) + ' : ' + str(result_parent_numbers[point]))

result_parent_numbers_list.sort()

for str in result_parent_numbers_list:
    print(str)

