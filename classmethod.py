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


# >>> obj = ToyClass()
# >>> obj.instancemethod()
# ('instance method called', ToyClass instance at 0x10f47e7a0>)
# >>> ToyClass.instancemethod(obj)
# ('instance method called', ToyClass instance at 0x10f47e7a0>)
#
# >>> obj.classmethod()
# ('class method called', <class  ToyClass at 0x10f453a10>)
#
# >>> ToyClass.classmethod()
# ('class method called', <class ToyClass at 0x10f453a10>)
# >>> ToyClass.staticmethod()
# 'static method called'
# >>> ToyClass.instancemethod()
# TypeError: unbound method instancemethod()
# must be called with ToyClass instance as
# first argument (got nothing instead)
