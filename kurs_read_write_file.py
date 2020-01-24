with open("dataset_24476_4.txt", 'r') as i, open("dataset_reversed.txt", 'w') as j:
    # file_list = list(i)
    line = i.readline()
    file_list2 = i.readlines()
    j.writelines(reversed(list(i)))



def file_lines_gen(file):
    with open(file) as f:
        for line in f:
            yield line.rstrip()


g = (file_lines_gen("dataset_24476_4.txt"))

print(next(g))
print(next(g))
print(next(g))

