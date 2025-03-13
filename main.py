import pandas as pd
import matplotlib.pyplot as plt

# Sample transactional data
data = {
    'CustomerID': [1, 1, 1, 2, 2, 3, 3, 3, 3],
    'InvoiceDate': ['2025-01-01', '2025-01-15', '2025-02-01', '2025-01-05', '2025-02-10', '2025-01-02', '2025-01-20', '2025-02-05', '2025-03-01'],
    'Quantity': [2, 3, 1, 4, 2, 1, 3, 2, 4],
    'UnitPrice': [10.0, 10.0, 10.0, 20.0, 20.0, 15.0, 15.0, 15.0, 15.0]
}

# Load data into DataFrame
df = pd.DataFrame(data)

# Convert InvoiceDate to datetime and calculate total amount per transaction
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Amount'] = df['Quantity'] * df['UnitPrice']

# Calculate RFM metrics
df_max_date = df['InvoiceDate'].max()
df['Recency'] = (df_max_date - df['InvoiceDate']).dt.days
df['Frequency'] = df.groupby('CustomerID')['InvoiceDate'].transform('count')
df['Monetary'] = df.groupby('CustomerID')['Amount'].transform('sum')

# Assign RFM scores
df['RecencyScore'] = pd.qcut(df['Recency'], q=5, labels=False, duplicates='drop')
df['FrequencyScore'] = pd.qcut(df['Frequency'], q=5, labels=False, duplicates='drop')
df['MonetaryScore'] = pd.qcut(df['Monetary'], q=5, labels=False, duplicates='drop')

# Calculate RFM score
df['RFMScore'] = df['RecencyScore'] + df['FrequencyScore'] + df['MonetaryScore']

# Plot RFM distribution
plt.figure(figsize=(10, 6))
plt.scatter(df['Recency'], df['Monetary'])
plt.xlabel('Recency')
plt.ylabel('Monetary')
plt.title('Recency vs Monetary')
plt.show()

# Example of finding high-value customers (e.g., RFMScore >= 8)
high_value_customers = df[df['RFMScore'] >= 8]
print(high_value_customers)
