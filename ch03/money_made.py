def money_made(num_shares, purchase_share_price, current_share_price):
    """
    num_shares is the number of shares of a stock that we purchased.
    purchase_share_price is the price of each of those shares.
    current_share_price is the current share price.

    Return the amount of money we have earned on the stock
    """
    # return num_shares * (current_share_price - purchase_share_price)

    price_difference = current_share_price - purchase_share_price
    return num_shares * price_difference
