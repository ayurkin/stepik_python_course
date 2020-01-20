class ToyClass:
    name1 = "wqe"

    def __init__(self):
        self.name = "ha"

    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print(cls.name1)
        print("dsad")
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

