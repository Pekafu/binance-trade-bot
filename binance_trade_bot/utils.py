def first(iterable, condition=lambda x: True):
    return next((x for x in iterable if condition(x)), None)


def get_market_ticker_price_from_list(all_tickers, ticker_symbol):
    """
    Get ticker price of a specific coin
    """
    ticker = first(all_tickers, condition=lambda x: x["symbol"] == ticker_symbol)
    return float(ticker["price"]) if ticker else None


def un_notate_exp_float(num: float):
    """
    Returns an un-notateted negative exponental
    """
    if num > 1:
        return num

    i = 0
    test_num = num
    while True:
        if test_num % 1 == 0 or i == 8:
            break
        test_num = test_num * (10)
        i = i + 1

    return f"{num:.{i}f}"
