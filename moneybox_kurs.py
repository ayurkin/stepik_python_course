class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.money_counter = 0

    def can_add(self, v):
        if self.money_counter + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.money_counter += v


x = Moneybox(10)
print(x.money_counter)
x.add(5)
print(x.money_counter)
x.add(20)
print(x.money_counter)