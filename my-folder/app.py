import pandas as pd

# Create a simple table (DataFrame)
data = {
    "Name": ["Pravie", "John", "Asha"],
    "Age": [30, 25, 28]
}

df = pd.DataFrame(data)
print("Here is your data table:")
print(df)