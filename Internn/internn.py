import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('Internn.csv')

# Write the DataFrame to an Excel file
df.to_excel('Internn.xlsx', index=False)
