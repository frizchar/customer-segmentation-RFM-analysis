"""
code to segment customers using RFM analysis:
 recency (R) - time since last purchase
 frequency (F) - total number of purcharses
 monetary value (M) - total spent
"""
import get_data
import process_data

if __name__ == "__main__":
    # get data
    dataset = get_data.data

    # get processed dataset
    df = process_data.perform_rfm_analysis(dataset)
    # calculate RFM score per customer
    RFM_score = df.groupby('CustomerID')['RFMScore'].max().reset_index()
    print('RFM score per customer :\n', RFM_score)

    RFM_SCORE_THRESHOLD = 8  # min required RFM score to consider a customer as 'high value'

    # Example of finding high-value customers (e.g., RFM_score >= 8)
    high_value_customers = df[df['RFMScore'] >= RFM_SCORE_THRESHOLD]
    print('high_value_customers :\n', high_value_customers[['CustomerID','RFMScore']])
