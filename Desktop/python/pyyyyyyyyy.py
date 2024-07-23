import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Specify the file path
file_path = 'patients.csv'

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(r"C:/Users/Sudharsan/Desktop/python/patients.csv")


# Display first few rows of the DataFram
print(df.head())

# Check column names
print(df.columns)

# Check data types
print(df.dtypes)

# Handle missing values (if any)
df = df.dropna()  # Example: drop rows with missing values
