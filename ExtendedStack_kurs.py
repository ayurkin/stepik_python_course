class ExtendedStack(list):
    def sum(self):
        return self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop()-self.pop())

    def mul(self):
        return self.append(self.pop()*self.pop())

    def div(self):
        return self.append(self.pop()//self.pop())


x = ExtendedStack([ 10])
# print(x.sum())
x.div()
print(x)