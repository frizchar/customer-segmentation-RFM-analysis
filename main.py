import process_data

if __name__ == "__main__":
    # get processed dataset
    df = process_data.df
    # calculate RFM score per customer
    RFM_score = df.groupby('CustomerID')['RFMScore'].max().reset_index()
    print('RFM score per customer :\n', RFM_score)

    RFM_SCORE_THRESHOLD = 8  # min required RFM score to consider a customer as 'high value'

    # Example of finding high-value customers (e.g., RFM_score >= 8)
    high_value_customers = df[df['RFMScore'] >= RFM_SCORE_THRESHOLD]
    print('high_value_customers :\n', high_value_customers[['CustomerID','RFMScore']])
