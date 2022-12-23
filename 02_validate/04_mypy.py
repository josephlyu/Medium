def add_two_nums(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

if __name__ == "__main__":
    result = add_two_nums("str", 2)

"""Examples (in terminal)

$ mypy 04_mypy.py
04_mypy.py:6: error: Argument 1 to "add_two_nums" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

"""