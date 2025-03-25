import pandas as pd
data = [
    {
        'Company_Name': 'Grand Continent Hotels Limited',
        'Market_Price': 113.0,
        'EPS': 3.74,
        'Book_Value_per_Share': 22.36,
        'Net_Income': 68000000.0,
        'Shares_Outstanding': 18659003,
        'Total_Debt': 347200000.0,
        'Shareholder_Equity': 401800000.0,
        'Avg_Shareholder_Equity': 260000000.0,
        'Total_Assets': 979000000.0,
        'Annual_Dividend': 0,
        'Shares_Applied_for': 0,
        'Shares_Offered': 6589200,
        'Market_Price_Post_IPO': 113.0,
        'Shares_Outstanding_Post_IPO': 24919403,
        'New_Shares_Issued': 6260400,
        'Offer_Price': 107.0,
        'Listing_Price': 113.0
    }
]

def con():
    df = pd.DataFrame(data)
    df.to_csv('input_data/company_details.csv', index=False)
    return df