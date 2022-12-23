def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper

# with @ symbol 
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")

# without @ symbol
def say_hello(name):
    print(f"Hello, {name}!")

my_decorator(say_hello)("John")

"""
The above decorated say_hello and my_decorator(say_hello) are equivalent.

Both outputs are:
    Before the function call
    Hello, John!
    After the function call
"""