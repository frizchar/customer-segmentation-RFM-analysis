import pandas as pd
import matplotlib.pyplot as plt


def perform_rfm_analysis(data: dict):
    """
        Performs RFM analysis on transactional data.

        Parameters:
            data (list of dict): Transactional data containing 'CustomerID', 'InvoiceDate', 'Quantity', and 'UnitPrice'.

        Returns:
            pd.DataFrame: DataFrame with RFM metrics and scores.
    """

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

    return df
