def foo(x: int, y: str, z: float = 0.0) -> bool:
    pass

print(foo.__annotations__) 
# {'x': <class 'int'>, 'y': <class 'str'>, 'z': <class 'float'>, 'return': <class 'bool'>}