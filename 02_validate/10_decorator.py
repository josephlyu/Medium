# with @ symbol
@decorator
foo(x, y):
    pass

foo(1, 2)

# without @ symbol
foo(x, y):
    pass

decorator(foo)(1, 2)