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

# Solution 1: Correct but not optimal.

import numpy as np

prices = np.array([100, 180, 260, 310, 40, 535, 695])


def calculate_max_profit(prices: np.ndarray):

    max_profit = 0

    for i in range(1, len(prices) - 1):
        buy_price = prices[i:]
        sell_price = prices[:-i]
        pro_loss = prices[i:] - prices[:-i]
        local_max = np.max(pro_loss)
        if local_max > max_profit:
            inx_position = np.where(local_max == pro_loss)
            low_buy_price = float(buy_price[inx_position])
            high_sell_price = float(sell_price[inx_position])
            max_profit = local_max

    buy_day = np.where(prices == low_buy_price)[0][0]
    sell_day = np.where(prices == high_sell_price)[0][0]

    print(
        "Profit:",
        max_profit,
        "(buy at",
        low_buy_price,
        "on day",
        buy_day,
        "and sell at",
        high_sell_price,
        "on day",
        sell_day,
        ")",
    )


calculate_max_profit(prices)


# ===================================================================================================

# Solution 2: Optimised, handles edge cases like invalid input etc.

import numpy as np


def calculate_max_profit(prices: np.ndarray):
    if len(prices) < 2:
        return 0, None, None  # No profit possible

    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i
            buy_day = np.where(prices == min_price)[0][0]

        if prices[i] < min_price:
            min_price = prices[i]

    if max_profit == 0:
        return 0, None, None  # No profit possible

    return max_profit, buy_day, sell_day


# Test the function
prices = np.array([100, 180, 260, 310, 40, 535, 695])
profit, buy_day, sell_day = calculate_max_profit(prices)

if profit > 0:
    print(
        f"Profit: {profit} (buy at {prices[buy_day]} on day {buy_day + 1} "
        f"and sell at {prices[sell_day]} on day {sell_day + 1})"
    )
else:
    print("No profit can be made.")
