#PostLab1

"""
Make sure 'pandas' and 'matplotlib' is installed before running the program!
"""
#Import relevant modules.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the folder.
file_path = "breadprice.csv"
data = pd.read_csv(file_path)

# Clean the data present, converting all columns (except 'Year') to a numeric
for month in data.columns[1:]:
    data[month] = pd.to_numeric(data[month], errors='coerce')

# Calculate the average price for each year
data['Average'] = data.iloc[:, 1:].mean(axis=1)

# Plots the average prices from the table.
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Average'], marker='o', linestyle='-')
plt.title('Average Bread Price Per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.tight_layout()

#Shows the diagram.
plt.show()
