from pydantic import validate_arguments

@validate_arguments
def add_two_nums(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

"""Examples (doctest style)

>>> add_two_nums(1, 2)
3
>>> add_two_nums('str', 2)
Traceback (most recent call last):
  ...
pydantic.error_wrappers.ValidationError: 1 validation error for AddTwoNums
num1
  value is not a valid integer (type=type_error.integer)
  
"""