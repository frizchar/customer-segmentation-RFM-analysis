import process_data

if __name__ == "__main__":
    # get processed dataset
    df = process_data.df

    # Example of finding high-value customers (e.g., RFMScore >= 8)
    high_value_customers = df[df['RFMScore'] >= 8]
    print('high_value_customers :\n', high_value_customers)
