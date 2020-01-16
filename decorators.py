def decorator_maker():
    def my_decorator(func):

        def wrapped():
            return func()

        return wrapped

    return my_decorator

new_decorator = decorator_maker()

def decorated_function():
    print("Я - декорируемая функция")


decorated_function = new_decorator(decorated_function)
decorated_function()
