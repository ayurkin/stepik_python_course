class Buffer:
    def __init__(self):
        self.current_list = []

    def add(self, *a):
        self.current_list = self.current_list + list(a)
        while len(self.current_list) >= 5:
            print(sum(self.current_list[0:5]))
            del self.current_list[0:5]

    def get_current_part(self):
        return self.current_list


x = Buffer()
x.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(x.get_current_part())
# x.add(1, 2, 3)
# print(x.get_current_part())
