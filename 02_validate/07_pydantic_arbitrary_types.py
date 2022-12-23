from pydantic import validate_arguments
import pandas as pd

@validate_arguments(config=dict(arbitrary_types_allowed=True))
def get_dataframe_head(
    data: pd.DataFrame,
    n: int = 5,
) -> pd.DataFrame:
    return data.head(n)

"""Examples (doctest style)

>>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> get_dataframe_head(df, 1)
      animal
0  alligator

>>> get_dataframe_head('str')
Traceback (most recent call last):
  ...
pydantic.error_wrappers.ValidationError: 1 validation error for GetDataframeHead
data
  instance of DataFrame expected (type=type_error.arbitrary_type; expected_arbitrary_type=DataFrame)
  
"""