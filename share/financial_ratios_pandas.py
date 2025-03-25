import pandas as pd

class FinancialRatios:
    def __init__(self, data):
        """
        Initialize with a pandas DataFrame containing necessary financial data.
        The DataFrame should include:
        - Total Assets
        - Total Liabilities
        - Current Assets
        - Current Liabilities
        - Revenue
        - Gross Profit
        - Operating Income
        - Net Income
        - Earnings Per Share (EPS)
        - Shares Outstanding
        - Dividend per Share
        - Capital Expenditures
        - Depreciation
        - Cash and Cash Equivalents
        - Total Debt
        - Retained Earnings
        - EBIT
        - Market Price per Share
        - Operating Cash Flow
        """
        self.data = data

    def pe_ratio(self):
        """Price-to-Earnings (P/E) Ratio"""
        # Formula: P/E = Market Price per Share / Earnings per Share (EPS)
        return self.data['Market Price per Share'] / self.data['EPS']

    def pb_ratio(self):
        """Price-to-Book (P/B) Ratio"""
        # Formula: P/B = Market Price per Share / (Total Assets - Total Liabilities)
        return self.data['Market Price per Share'] / (self.data['Total Assets'] - self.data['Total Liabilities'])

    def ps_ratio(self):
        """Price-to-Sales (P/S) Ratio"""
        # Formula: P/S = Market Price per Share / Revenue
        return self.data['Market Price per Share'] / self.data['Revenue']

    def return_on_assets(self):
        """Return on Assets (ROA)"""
        # Formula: ROA = (Net Income / Total Assets) * 100
        return (self.data['Net Income'] / self.data['Total Assets']) * 100

    def return_on_equity(self):
        """Return on Equity (ROE)"""
        # Formula: ROE = (Net Income / (Total Assets - Total Liabilities)) * 100
        return (self.data['Net Income'] / (self.data['Total Assets'] - self.data['Total Liabilities'])) * 100

    def quick_ratio(self):
        """Quick Ratio"""
        # Formula: Quick Ratio = (Current Assets - Inventory) / Current Liabilities
        return (self.data['Current Assets'] - self.data['Total Liabilities']) / self.data['Current Liabilities']

    def current_ratio(self):
        """Current Ratio"""
        # Formula: Current Ratio = Current Assets / Current Liabilities
        return self.data['Current Assets'] / self.data['Current Liabilities']

    def debt_to_equity(self):
        """Debt-to-Equity (D/E) Ratio"""
        # Formula: Debt-to-Equity = Total Liabilities / (Total Assets - Total Liabilities)
        return self.data['Total Liabilities'] / (self.data['Total Assets'] - self.data['Total Liabilities'])

    def dividend_yield(self):
        """Dividend Yield"""
        # Formula: Dividend Yield = (Dividend per Share / Market Price per Share) * 100
        return (self.data['Dividend per Share'] / self.data['Market Price per Share']) * 100

    def operating_cash_flow_to_capex(self):
        """Operating Cash Flow to Capital Expenditures (OCF/CapEx)"""
        # Formula: OCF to CapEx = Operating Cash Flow / Capital Expenditures
        return self.data['Operating Cash Flow'] / self.data['Capital Expenditures']

    def beta(self):
        """Beta (β) - Stock Volatility"""
        # Formula: Beta = Covariance of Stock with Market / Variance of Market
        return self.data.get('Beta', 'N/A')  # If not available, return 'N/A'


# Example financial data in a pandas DataFrame
data = pd.DataFrame({
    'Total Assets': [500000000],  # Example value
    'Total Liabilities': [200000000],  # Example value
    'Current Assets': [150000000],  # Example value
    'Current Liabilities': [100000000],  # Example value
    'Revenue': [350000000],  # Example value
    'Gross Profit': [120000000],  # Example value
    'Operating Income': [100000000],  # Example value
    'Net Income': [50000000],  # Example value
    'EPS': [5],  # Example value
    'Shares Outstanding': [10000000],  # Example value
    'Dividend per Share': [1],  # Example value
    'Capital Expenditures': [25000000],  # Example value
    'Depreciation': [15000000],  # Example value
    'Cash and Cash Equivalents': [5000000],  # Example value
    'Total Debt': [100000000],  # Example value
    'Retained Earnings': [20000000],  # Example value
    'EBIT': [70000000],  # Example value
    'Market Price per Share': [100],  # Example value
    'Operating Cash Flow': [40000000],  # Example value
    'Beta': [1.2]  # Example value
})

# Create the FinancialRatios object
fin_ratios = FinancialRatios(data)

# Calculate all ratios and add them to the dataframe
data['P/E Ratio'] = fin_ratios.pe_ratio()
data['P/B Ratio'] = fin_ratios.pb_ratio()
data['P/S Ratio'] = fin_ratios.ps_ratio()
data['Return on Assets (ROA)'] = fin_ratios.return_on_assets()
data['Return on Equity (ROE)'] = fin_ratios.return_on_equity()
data['Quick Ratio'] = fin_ratios.quick_ratio()
data['Current Ratio'] = fin_ratios.current_ratio()
data['Debt-to-Equity Ratio'] = fin_ratios.debt_to_equity()
data['Dividend Yield'] = fin_ratios.dividend_yield()
data['Operating Cash Flow to CapEx'] = fin_ratios.operating_cash_flow_to_capex()
data['Beta'] = fin_ratios.beta()

# Print the dataframe with all the calculated ratios
print(data[['P/E Ratio', 'P/B Ratio', 'P/S Ratio', 'Return on Assets (ROA)', 'Return on Equity (ROE)', 
            'Quick Ratio', 'Current Ratio', 'Debt-to-Equity Ratio', 'Dividend Yield', 
            'Operating Cash Flow to CapEx', 'Beta']])