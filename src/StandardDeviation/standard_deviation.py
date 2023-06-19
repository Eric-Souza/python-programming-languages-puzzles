import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('Stores.csv')

# Rename columns
new_column_names = {
    'Daily_Customer_Count': 'Visitors',
    'Items_Available': 'Available Items',
    'Store_Sales': 'Store Sales'
}
df = df.rename(columns=new_column_names)

# Calculate statistics
statistics = df[['Available Items', 'Visitors', 'Store Sales']].describe()

# Print min, max, mean and standard deviation values
print('Stats:')
print(statistics)

# Generate graphs
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Available Items graph
axes[0].scatter(df.index, df['Available Items'], color='red', label='Available Items')
axes[0].set_xlabel('Index')
axes[0].set_ylabel('Available Items')
axes[0].legend()

# Visitors graph
axes[1].scatter(df.index, df['Visitors'], color='blue', label='Visitors')
axes[1].set_xlabel('Index')
axes[1].set_ylabel('Visitors')
axes[1].legend()

# Store Sales graph
axes[2].scatter(df.index, df['Store Sales'], color='green', label='Store Sales')
axes[2].set_xlabel('Index')
axes[2].set_ylabel('Store Sales')
axes[2].legend()

# Display graphs
plt.tight_layout()
plt.show()
