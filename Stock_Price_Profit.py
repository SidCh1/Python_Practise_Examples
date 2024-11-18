# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

# You are given a NumPy array prices representing the daily closing prices of a stock for N days.
# Write a function that calculates the maximum profit that could be achieved by buying on one day and selling on a later day.
# If no profit can be made, return 0 as the profit and None for the buy and sell days.
# Handle edge cases gracefully (e.g., empty array, single-day array).

# Example input:

# prices = [100, 180, 260, 310, 40, 535, 695], the output should be:

# Output:
# Profit: 655 (buy at 40 on day 5 and sell at 695 on day 7).

# ===================================================================================================

# Solution:

import numpy as np

prices = [100, 180, 260, 310, 40, 535, 695]


def calculate_max_profit(prices: list):

    min_price = np.min(prices)
    max_price = np.max(prices)
    min_price_day = np.where(prices == min_price)[0][0] + 1
    max_price_day = np.where(prices == max_price)[0][0] + 1
    max_profit = np.max(prices) - np.min(prices)

    print(
        "Profit:",
        max_profit,
        "(buy at",
        min_price,
        "on day",
        min_price_day,
        "and sell at",
        max_price,
        "on day",
        max_price_day,
        ")",
    )


calculate_max_profit(prices)
