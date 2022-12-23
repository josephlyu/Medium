from beartype import beartype

@beartype
def add_two_nums(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

"""Examples (doctest style)

>>> add_two_nums(1, 2)
3
>>> add_two_nums('str', 2)
Traceback (most recent call last):
  ...
beartype.roar.BeartypeCallHintParamViolation: @beartyped __main__.add_two_nums() parameter num1='str' violates type hint <class 'int'>, as str 'str' not instance of int.

"""