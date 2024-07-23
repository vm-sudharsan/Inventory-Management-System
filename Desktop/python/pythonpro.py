# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Loading
df = pd.read_csv('patients.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Step 2: Data Cleaning and Preprocessing
df.dropna(inplace=True)  # Drop rows with missing values
# Example: Fill missing values in a specific column with mean
# df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Perform data transformations if needed
# Example: Convert a column to integer type
# df['numeric_column'] = df['numeric_column'].astype(int)

# Display basic statistics after cleaning
print(df.describe())

# Step 3: Exploratory Data Analysis (EDA) and Visualization

# Example: Histogram of a numerical column
plt.figure(figsize=(10, 6))
sns.histplot(df['numerical_column'], bins=20, kde=True)
plt.title('Histogram of Numerical Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot of two numerical columns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='column1', y='column2', data=df)
plt.title('Scatter Plot')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.show()

# Step 4: Export Processed Data
df.to_csv('processed_data.csv', index=False)
print("Processed data exported successfully.")
