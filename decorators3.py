import time

def timer_decorator(func):
    def wrapper():
        init_time = time.time()
        func()
        print(time.time()-init_time)
    return wrapper

# def test():
#     print('lol')
#
# test = timer_decorator(test())

@timer_decorator
def test():
    print('lol')

test()

