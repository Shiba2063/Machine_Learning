# Pandas is an open-source Python library that provides data structures and functions for efficient data manipulation, analysis, and handling of structured data.
#It leverages the power and speed of numpy to make data analysis and preprocessing.
#It provides rich and highly robust data operations.

#Example :-
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari"],
    "Age": [20, 21, 19],
    "Marks": [80, 75, 90]
}

df = pd.DataFrame(data)

print(df)

