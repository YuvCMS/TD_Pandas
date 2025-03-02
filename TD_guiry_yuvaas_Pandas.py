import pandas as pd
import numpy as np

# Exercise 1: Creating and Modifying Series
data_series = pd.Series({'a': 100, 'b': 200, 'c': 300})
print("Exercise 1: Series")
print(data_series, "\n")

# Exercise 2: Creating DataFrames
df2 = pd.DataFrame({
    'A': [1, 4, 7],
    'B': [2, 5, 8],
    'C': [3, 6, 9]
})

# Add a new column D
df2['D'] = [10, 11, 12]

# Drop column B and display result
df2 = df2.drop(columns=['B'])
print("Exercise 2: Modified DataFrame")
print(df2, "\n")

# Exercise 3: DataFrame Indexing and Selection
df3 = pd.DataFrame({
    'A': [1, 4, 7],
    'B': [2, 5, 8],
    'C': [3, 6, 9]
})

# Select column B
column_B = df3['B']
print("Exercise 3: Column B")
print(column_B, "\n")

# Select columns A and C
columns_A_C = df3[['A', 'C']]
print("Exercise 3: Columns A and C")
print(columns_A_C, "\n")

# Select row with index 1 using .loc
row_1 = df3.loc[1]
print("Exercise 3: Row at index 1")
print(row_1, "\n")

# Exercise 4: Adding and Removing DataFrame Elements
df4 = df3.copy()

# Add a new column Sum
df4['Sum'] = df4['A'] + df4['B'] + df4['C']
print("Exercise 4: DataFrame with Sum Column")
print(df4, "\n")

# Remove the column Sum
df4 = df4.drop(columns=['Sum'])

# Add a column Random with random numbers
df4['Random'] = np.random.rand(len(df4))
print("Exercise 4: DataFrame with Random Column")
print(df4, "\n")

# Exercise 5: Merging DataFrames
left_df = pd.DataFrame({
    'key': ['A1', 'A2', 'A3'],
    'A': [1, 2, 3],
    'B': ['B1', 'B2', 'B3']
})

right_df = pd.DataFrame({
    'key': ['C1', 'C2', 'C3'],
    'C': [1, 2, 3],
    'D': ['D1', 'D2', 'D3']
})

# Add column E to right DataFrame
right_df['E'] = ['E1', 'E2', 'E3']

# Perform an outer join
merged_df = pd.merge(left_df, right_df, on='key', how='outer')
print("Exercise 5: Merged DataFrame with Outer Join")
print(merged_df, "\n")



# Exercise 6: Data Cleaning
df6 = pd.DataFrame({
    'A': [1.0, np.nan, 7.0],
    'B': [np.nan, 5.0, 8.0],
    'C': [3.0, 6.0, np.nan]
})

# Replace NaN values with 0
df6_filled_zero = df6.fillna(0)
print("Exercise 6: DataFrame with NaN replaced by 0")
print(df6_filled_zero, "\n")

# Replace NaN values with the mean of the column
df6_filled_mean = df6.fillna(df6.mean())
print("Exercise 6: DataFrame with NaN replaced by column mean")
print(df6_filled_mean, "\n")

# Drop rows where any value is NaN
df6_dropped = df6.dropna()
print("Exercise 6: DataFrame with rows containing NaN dropped")
print(df6_dropped, "\n")


# Exercise 7: Grouping and Aggregation
df7 = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'A', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Group by Category and calculate mean
mean_group = df7.groupby('Category')['Value'].mean()
print("Exercise 7: Mean of Value grouped by Category")
print(mean_group, "\n")

# Modify to calculate sum instead of mean
sum_group = df7.groupby('Category')['Value'].sum()
print("Exercise 7: Sum of Value grouped by Category")
print(sum_group, "\n")

# Count number of entries in each group
count_group = df7.groupby('Category')['Value'].count()
print("Exercise 7: Count of entries in each group")
print(count_group, "\n")



# Exercise 8: Pivot Tables
df8 = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Type': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Create pivot table showing mean value for each Category and Type
pivot_mean = df8.pivot_table(values='Value', index='Category', columns='Type', aggfunc='mean')
print("Exercise 8: Pivot Table showing mean Value")
print(pivot_mean, "\n")

# Modify to show sum instead of mean
pivot_sum = df8.pivot_table(values='Value', index='Category', columns='Type', aggfunc='sum')
print("Exercise 8: Pivot Table showing sum of Value")
print(pivot_sum, "\n")

# Add margins to show total sum
pivot_margins = df8.pivot_table(values='Value', index='Category', columns='Type', aggfunc='sum', margins=True)
print("Exercise 8: Pivot Table with Total Sum")
print(pivot_margins, "\n")



# Exercise 9: Time Series Data
date_range = pd.date_range(start='2023-01-01', periods=6, freq='D')
df9 = pd.DataFrame({'Date': date_range, 'Value': np.random.randint(1, 100, size=6)})

# Set the date column as the index
df9.set_index('Date', inplace=True)

# Resample the data to calculate the sum for each 2-day period
df9_resampled = df9.resample('2D').sum()

print("Exercise 9: Time Series Data with 2-Day Sum")
print(df9_resampled, "\n")

# Exercise 10: Handling Missing Data
df10 = pd.DataFrame({
    'A': [1.0, 2.0, np.nan],
    'B': [np.nan, 5.0, 8.0],
    'C': [3.0, np.nan, 9.0]
})

# Interpolate missing values
df10_interpolated = df10.interpolate()
print("Exercise 10: Interpolated Missing Data")
print(df10_interpolated, "\n")

# Drop rows with any NaN values
df10_dropped = df10.dropna()
print("Exercise 10: DataFrame with rows containing NaN dropped")
print(df10_dropped, "\n")

# Exercise 11: DataFrame Operations
df11 = pd.DataFrame({
    'A': [1, 4, 7],
    'B': [2, 5, 8],
    'C': [3, 6, 9]
})

# Calculate the cumulative sum
df11_cumsum = df11.cumsum()
print("Exercise 11: Cumulative Sum")
print(df11_cumsum, "\n")

# Calculate the cumulative product
df11_cumprod = df11.cumprod()
print("Exercise 11: Cumulative Product")
print(df11_cumprod, "\n")

# Apply a function to subtract 1 from all elements
df11_subtract1 = df11.applymap(lambda x: x - 1)
print("Exercise 11: Subtract 1 from All Elements")
print(df11_subtract1, "\n")
