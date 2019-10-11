#Треугольник Паскаля
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n,0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]
        c = zip(row + y, y + row)

print(1)
pascal_triangle(6)
