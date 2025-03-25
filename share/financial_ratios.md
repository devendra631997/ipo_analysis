# Financial Ratios Calculator (Using Pandas)

This Python script calculates a variety of important financial ratios using `pandas` for easier data management and computation. The ratios are computed from the financial data stored in a `pandas.DataFrame`.

### Key Ratios and Their Formulas:

1. **P/E Ratio (Price-to-Earnings Ratio)**:
   - Formula:  
     \[
     \text{P/E} = \frac{\text{Market Price per Share}}{\text{Earnings per Share (EPS)}}
     \]
   - The P/E ratio measures how much investors are willing to pay for a dollar of earnings.

2. **P/B Ratio (Price-to-Book Ratio)**:
   - Formula:  
     \[
     \text{P/B} = \frac{\text{Market Price per Share}}{\text{Total Assets} - \text{Total Liabilities}}
     \]
   - The P/B ratio compares the market price of a company’s shares to its book value.

3. **P/S Ratio (Price-to-Sales Ratio)**:
   - Formula:  
     \[
     \text{P/S} = \frac{\text{Market Price per Share}}{\text{Revenue}}
     \]
   - The P/S ratio compares the market price of a company’s stock to its revenue.

4. **ROA (Return on Assets)**:
   - Formula:  
     \[
     \text{ROA} = \frac{\text{Net Income}}{\text{Total Assets}} \times 100
     \]
   - The ROA ratio measures a company’s ability to generate profit from its assets.

5. **ROE (Return on Equity)**:
   - Formula:  
     \[
     \text{ROE} = \frac{\text{Net Income}}{\text{Equity}} \times 100
     \]
   - The ROE ratio measures how effectively a company is using its equity base to generate profits.

6. **Quick Ratio**:
   - Formula:  
     \[
     \text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}}
     \]
   - The quick ratio evaluates a company's ability to meet its short-term liabilities using its most liquid assets.

7. **Current Ratio**:
   - Formula:  
     \[
     \text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}
     \]
   - The current ratio measures a company’s ability to cover its short-term obligations with short-term assets.

8. **Debt-to-Equity Ratio**:
   - Formula:  
     \[
     \text{Debt-to-Equity} = \frac{\text{Total Liabilities}}{\text{Equity}}
     \]
   - The D/E ratio measures the financial leverage of a company by comparing its total liabilities to shareholders' equity.

9. **Dividend Yield**:
   - Formula:  
     \[
     \text{Dividend Yield} = \frac{\text{Dividend per Share}}{\text{Market Price per Share}} \times 100
     \]
   - The dividend yield indicates the return on investment based on the dividends paid out by the company.

10. **Operating Cash Flow to Capital Expenditures (OCF/CapEx)**:
    - Formula:  
      \[
      \text{OCF to CapEx} = \frac{\text{Operating Cash Flow}}{\text{Capital Expenditures}}
      \]
    - This ratio measures how well a company can cover its capital expenditures through its operating cash flow.

11. **Beta (β)**:
    - Formula:  
      \[
      \beta = \frac{\text{Covariance of Stock with Market}}{\text{Variance of Market}}
      \]
    - Beta measures the stock’s volatility in relation to the overall market. A beta greater than 1 indicates that the stock is more volatile than the market.

### How to Use:
1. Ensure you have Python installed on your computer.
2. Install `pandas` if not already installed:  
   `pip install pandas`
3. Replace the example data in the script with the financial data of the company you're analyzing.
4. Run the script by typing `python financial_ratios_pandas.py` in your terminal.

---

This script will print a DataFrame that includes all the key financial ratios and their corresponding values based on the input data.
