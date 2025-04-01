import process_data

if __name__ == "__main__":
    # get processed dataset
    df = process_data.df

    RFMSCORE_THRESHOLD = 8  # min required RFM score to consider a customer as 'high value'

    # Example of finding high-value customers (e.g., RFMScore >= 8)
    high_value_customers = df[df['RFMScore'] >= RFMSCORE_THRESHOLD]
    print('high_value_customers :\n', high_value_customers)
    
