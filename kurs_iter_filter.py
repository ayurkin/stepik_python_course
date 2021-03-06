def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


class multifilter:
    def judge_half(self, pos, neg):  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(self, pos, neg):  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos > 0

    def judge_all(self, pos, neg):  # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.i = 0
        self.pos = 0
        self.neg = 0
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

    def calc(self, x):
        res = [f(x) for f in self.funcs]
        return res.count(True), res.count(False)

    def __next__(self):
        while self.i < len(self.iterable):
            self.i += 1

            self.pos, self.neg = self.calc(self.iterable[self.i - 1])
            if self.judge(self, self.pos, self.neg):
                return self.iterable[self.i - 1]
        else:
            raise StopIteration


x = multifilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], mul2, mul3, judge=multifilter.judge_all)
print(list(x))
