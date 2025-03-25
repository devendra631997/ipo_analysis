def calculate_pe_ratio(market_price, eps):
    return market_price / eps if eps != 0 else None


def calculate_pb_ratio(market_price, book_value_per_share):
    return market_price / book_value_per_share if book_value_per_share != 0 else None


def calculate_eps(net_income, shares_outstanding):
    return net_income / shares_outstanding if shares_outstanding != 0 else None


def calculate_de_ratio(total_debt, shareholder_equity):
    return total_debt / shareholder_equity if shareholder_equity != 0 else None


def calculate_roe(net_income, avg_shareholder_equity):
    return (net_income / avg_shareholder_equity) * 100 if avg_shareholder_equity != 0 else None


def calculate_roa(net_income, total_assets):
    return (net_income / total_assets) * 100 if total_assets != 0 else None


def calculate_dividend_yield(annual_dividend, market_price):
    return (annual_dividend / market_price) * 100 if market_price != 0 else None


def calculate_subscription_rate(shares_applied_for, shares_offered):
    return shares_applied_for / shares_offered if shares_offered != 0 else None


def calculate_market_cap(market_price, shares_outstanding):
    return market_price * shares_outstanding if shares_outstanding != 0 else None


def calculate_post_ipo_valuation(offer_price, shares_outstanding_post_ipo):
    return offer_price * shares_outstanding_post_ipo if shares_outstanding_post_ipo != 0 else None


def calculate_dilution(new_shares_issued, total_shares_after_ipo):
    return (new_shares_issued / total_shares_after_ipo) * 100 if total_shares_after_ipo != 0 else None


def calculate_listing_gain_or_loss(offer_price, listing_price):
    return ((listing_price - offer_price) / offer_price) * 100 if offer_price != 0 else None