import functools
from inspect import signature
import pandas as pd

def validate_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the parameter names and annotations for the original function
        original_params = signature(func).parameters

        # Get parameter names and values from the user input
        input_params = signature(func).bind(*args, **kwargs)
        # Use default values if applicable
        input_params.apply_defaults()
        # Keep all parameter names and values in a dictionary
        input_params = input_params.arguments

        # Iterate over the parameters and check the types of the arguments
        for name, param in original_params.items():
            # Check the type of the argument against the annotation
            if not isinstance(input_params.get(name), param.annotation):
                raise ValueError(
                    f"Invalid argument type for {name}: expected {param.annotation}, got {type(input_params.get(name))}"
                )

        # If all arguments are valid, call the original function
        return func(*args, **kwargs)
    return wrapper

@validate_arguments
def get_dataframe_head(
    data: pd.DataFrame,
    n: int = 5,
) -> pd.DataFrame:
    """Function to get the first n rows of a dataframe."""
    return data.head(n)

"""Examples (doctest style)

>>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> get_dataframe_head(df)
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey

>>> get_dataframe_head('str')
Traceback (most recent call last):
  ...
ValueError: Invalid argument type for data: expected <class 'pandas.core.frame.DataFrame'>, got <class 'str'>
  
>>> get_dataframe_head(df, 'str')
Traceback (most recent call last):
  ...
ValueError: Invalid argument type for n: expected <class 'int'>, got <class 'str'>

"""

print(get_dataframe_head.__doc__)
# Function to get the first n rows of a dataframe.
print(get_dataframe_head.__annotations__)
# {'data': <class 'pandas.core.frame.DataFrame'>, 'n': <class 'int'>, 'return': <class 'pandas.core.frame.DataFrame'>}