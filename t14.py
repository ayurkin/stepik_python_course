a = [44, 12, 34, 5, 6, 2, 65, 0, 1, 3, 237, 5, 66, 32]

def print_my(list):
    for x in list:
        if x %2 == 0:
            print(x)
        if x == 237:
            break

print_my(a)