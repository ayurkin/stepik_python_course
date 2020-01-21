from functools import wraps


def decorator_dash(func):
    def wrapper():
        print("--decorator_start--")
        func()
        print("--decorator_end--")

    return wrapper


# def print_hello():
#     print("hello")

@decorator_dash
def print_hello():
    print("hello")


# print_hello = decorator_dash(print_hello)
print_hello()


# def print_world(arg1, arg2):
#     print(f"world for {arg1}, {arg2}")


def decorator_plus(func):
    def wrapper(arg1, arg2):
        print("++decorator_start++")
        # print(f"arg1: {arg1}, arg2: {arg2}")
        func(arg1, arg2)
        print("++decorator_end++")

    return wrapper


# print_world = decorator_plus(print_world)

@decorator_plus
def print_world(arg1, arg2):
    print(f"world for {arg1}, {arg2}")


print_world("Bobb", "Arto")


# def decorator_maker(arg1, arg2):
#     def decorator_with_args(func):
#         print(f"zaprintim decorator args - {arg1} and {arg2}")
#
#         def wrapper(func_arg1, func_arg2):
#             print("decorator_with_args_start")
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return decorator_with_args


def decorator_with_args(arg1, arg2):
    def decorator_internal(func):
        print(f"zaprintim decorator args - {arg1} and {arg2}")

        @wraps(func)
        def wrapper(func_arg1, func_arg2):
            print("decorator_with_args_start")
            print(f"one more time zausaem - {arg1} and {arg2}")
            func(func_arg1, func_arg2)
            print("decorator_with_args_end")

        return wrapper

    return decorator_internal


# def printer_hey(func_arg1, func_arg2):
#     print(f"hey, {func_arg1}, {func_arg2}")


# new_decorator = decorator_with_args("argument odnako", "ne argument")
# printer_hey = new_decorator(printer_hey)

@decorator_with_args("argument odnako", "ne argument")
def printer_hey(func_arg1, func_arg2):
    print(f"hey, {func_arg1}, {func_arg2}")

printer_hey("Arto", "Jimmy")
print(printer_hey.__name__)
