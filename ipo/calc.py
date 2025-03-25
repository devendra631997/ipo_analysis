    
import pandas as pd
from basic_function import calculate_pe_ratio, calculate_pb_ratio, calculate_eps, calculate_de_ratio, calculate_roe, calculate_roa, calculate_dividend_yield, calculate_subscription_rate, calculate_market_cap, calculate_post_ipo_valuation, calculate_dilution, calculate_listing_gain_or_loss

def basic_parameter_calculation(df):

    # List to store the results
    results = []

    # Loop through each company (row in the DataFrame)
    for _, row in df.iterrows():
        company_name = row['Company_Name']

        # Retrieve values for the current company
        market_price = row['Market_Price']
        eps = row['EPS']
        book_value_per_share = row['Book_Value_per_Share']
        net_income = row['Net_Income']
        shares_outstanding = row['Shares_Outstanding']
        total_debt = row['Total_Debt']
        shareholder_equity = row['Shareholder_Equity']
        avg_shareholder_equity = row['Avg_Shareholder_Equity']
        total_assets = row['Total_Assets']
        annual_dividend = row['Annual_Dividend']
        shares_applied_for = row['Shares_Applied_for']
        shares_offered = row['Shares_Offered']
        market_price_post_ipo = row['Market_Price_Post_IPO']
        shares_outstanding_post_ipo = row['Shares_Outstanding_Post_IPO']
        new_shares_issued = row['New_Shares_Issued']
        offer_price = row['Offer_Price']
        listing_price = row['Listing_Price']

        # Calculate metrics for the current company
        pe_ratio = calculate_pe_ratio(market_price, eps)
        pb_ratio = calculate_pb_ratio(market_price, book_value_per_share)
        calculated_eps = calculate_eps(net_income, shares_outstanding)
        de_ratio = calculate_de_ratio(total_debt, shareholder_equity)
        roe = calculate_roe(net_income, avg_shareholder_equity)
        roa = calculate_roa(net_income, total_assets)
        dividend_yield = calculate_dividend_yield(annual_dividend, market_price)
        subscription_rate = calculate_subscription_rate(shares_applied_for, shares_offered)
        market_cap = calculate_market_cap(market_price, shares_outstanding)
        post_ipo_valuation = calculate_post_ipo_valuation(offer_price, shares_outstanding_post_ipo)
        dilution = calculate_dilution(new_shares_issued, shares_outstanding_post_ipo)
        listing_gain_loss = calculate_listing_gain_or_loss(offer_price, listing_price)

        # Store the results for the current company
        results.append({
            'Company_Name': company_name,
            'P/E_Ratio': pe_ratio,
            'P/B_Ratio': pb_ratio,
            'EPS': calculated_eps,
            'D/E_Ratio': de_ratio,
            'ROE': roe,
            'ROA': roa,
            'Dividend_Yield': dividend_yield,
            'Subscription_Rate': subscription_rate,
            'Market_Capitalization': market_cap,
            'Post_IPO_Valuation': post_ipo_valuation,
            'Dilution': dilution,
            'Listing_Gain_Loss': listing_gain_loss
        })

    # Convert the results list to a DataFrame and save it to a new Excel file
    results_df = pd.DataFrame(results)
    return results_df