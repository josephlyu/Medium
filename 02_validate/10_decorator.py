def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper

# with @ symbol 
@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# without @ symbol
def greet(name):
    print(f"Hello, {name}!")

my_decorator(greet)("John")

"""
The above decorated greet [line 13] and my_decorator(greet) [line 19] are equivalent.

Both outputs are:
    Before the function call
    Hello, John!
    After the function call
"""