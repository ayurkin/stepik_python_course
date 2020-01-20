import time

def timer(func):
    def wrapper():
        init_time = time.time()
        func()
        print(time.time()-init_time)
    return wrapper()

@timer
def test():
    print('lol')



