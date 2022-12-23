from inspect import signature

def foo(x: int, y: str, z: float = 0.0) -> bool:
    pass

print(signature(foo).parameters)
# OrderedDict([('x', <Parameter "x: int">), ('y', <Parameter "y: str">), ('z', <Parameter "z: float = 0.0">)])

print('The parameter names and types are:')
print([k for k in signature(foo).parameters.keys()])
print([v.annotation for v in signature(foo).parameters.values()])
# The parameter names and types are:
# ['x', 'y', 'z']
# [<class 'int'>, <class 'str'>, <class 'float'>]