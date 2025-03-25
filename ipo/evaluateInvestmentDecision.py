import csv

def evaluate_investment(data):
    # Extracting values from the data
    PE_ratio = data["P/E_Ratio"]
    PB_ratio = data["P/B_Ratio"]
    EPS = data["EPS"]
    DE_ratio = data["D/E_Ratio"]
    ROE = data["ROE"]
    Dividend_Yield = data["Dividend_Yield"]
    Listing_Gain_Loss = data["Listing_Gain_Loss"]

    # Criteria thresholds for a good investment
    PE_threshold = 25  # P/E ratio below 25 is generally considered better
    PB_threshold = 3   # P/B ratio below 3 is considered good
    ROE_threshold = 15 # ROE above 15% is considered good
    DE_threshold = 1   # D/E ratio below 1 is considered safe
    Dividend_Yield_threshold = 2  # A dividend yield above 2% is preferred
    Listing_Gain_threshold = 0    # Listing gain should be positive or 0

    # Evaluating each metric
    PE_good = PE_ratio < PE_threshold
    PB_good = PB_ratio < PB_threshold
    ROE_good = ROE > ROE_threshold
    DE_good = DE_ratio < DE_threshold
    EPS_good = EPS > 0  # We want a positive EPS
    Dividend_good = Dividend_Yield > Dividend_Yield_threshold
    Listing_good = Listing_Gain_Loss > Listing_Gain_threshold

    # Final investment decision
    decision = "Buy" if all([PE_good, PB_good, ROE_good, DE_good, EPS_good, Listing_good]) else "<span style=color:red> Hold/Don't Buy"

    # Print the evaluation and decision
    print(f"### Evaluation of {data['Company_Name']}:")
    print(f"- P/E Ratio: {PE_ratio} {'<span style=color:Green>Good' if PE_good else '<span style=color:red>Bad'}")
    print(f"- P/B Ratio: {PB_ratio} {'<span style=color:Green>Good' if PB_good else '<span style=color:red>Bad'}")
    print(f"- EPS: {EPS} {'<span style=color:Green>Good' if EPS_good else '<span style=color:red>Bad'}")
    print(f"- D/E Ratio: {DE_ratio} {'<span style=color:Green>Good' if DE_good else '<span style=color:red>Bad'}")
    print(f"- ROE: {ROE}% {'<span style=color:Green>Good' if ROE_good else '<span style=color:red>Bad'}")
    print(f"- Dividend Yield: {Dividend_Yield}% {'<span style=color:Green>Good' if Dividend_good else '<span style=color:red>Bad'}")
    print(f"- Listing Gain/Loss: {Listing_Gain_Loss}% {'<span style=color:Green>Good' if Listing_good else '<span style=color:red>Bad'}")
    print(f"- Investment Decision: {decision}\n")

def read_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert string values to appropriate types
            row["P/E_Ratio"] = float(row["P/E_Ratio"])
            row["P/B_Ratio"] = float(row["P/B_Ratio"])
            row["EPS"] = float(row["EPS"])
            row["D/E_Ratio"] = float(row["D/E_Ratio"])
            row["ROE"] = float(row["ROE"])
            row["Dividend_Yield"] = float(row["Dividend_Yield"])
            row["Listing_Gain_Loss"] = float(row["Listing_Gain_Loss"])
            evaluate_investment(row)

# Run the program with the CSV file path
# file_path = 'result.csv'  # Path to your CSV file
# read_data_from_csv(file_path)
