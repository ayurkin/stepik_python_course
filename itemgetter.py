from operator import itemgetter, attrgetter

x_list = [1, 2, 3]

itemgetter(1)(x)  # 2
f = itemgetter(2)
f(x)  # 3

x_dict = {"123": 5}
itemgetter("123")(x_dict)

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]
x.sort(key=itemgetter(-1))

attrgetter("sort")(x)  # x.sort


