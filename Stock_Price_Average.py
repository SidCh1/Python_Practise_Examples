# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================

# Problem:

# Imagine you're designing an application that involves analyzing stock market data. You have daily stock prices for a month as a NumPy array.
# Write a function calculate_moving_average(prices, window_size) to compute the moving average of the stock prices over a specified window size.

# Example input:

# prices = np.array([100, 102, 104, 108, 110, 115, 120, 125])
# window_size = 3

# Example output:

# array([102. , 104.66666667, 107.33333333, 111. , 115. , 120. ])


# ===================================================================================================

# Solution 1: (not optimal)

import numpy as np

prices = np.array([100, 102, 104, 108, 110, 115, 120, 125])
window_size = 3


def calculate_moving_average(prices, window_size):

    result = []
    if window_size > len(prices) or window_size <= 0:
        print("impossible value given for window_size")

        return

    if len(prices) == 0:
        print("prices array empty, please check")

        return

    for i in range(len(prices) - window_size + 1):
        window_prices = prices[i : window_size + i]
        print(window_prices)
        if len(window_prices) == window_size:
            result.append(float(np.average(window_prices)))
        else:
            print("something went wrong with window sizes")
    return result


moving_avg_prices = calculate_moving_average(prices, window_size)

print(moving_avg_prices)


# ===================================================================================================

# Solution 2: (optimal)

import numpy as np


def calculate_moving_average(prices, window_size):

    # Handle edge cases

    if len(prices) == 0:
        raise ValueError("Prices array is empty.")
    if window_size > len(prices) or window_size <= 0:
        raise ValueError(
            "Invalid window_size: should be between 1 and the length of prices."
        )

    # Use NumPy's convolve function to compute the moving average
    weights = np.ones(window_size) / window_size
    moving_avg = np.convolve(prices, weights, mode="valid")
    return moving_avg


# Example usage
prices = np.array([100, 102, 104, 108, 110, 115, 120, 125])
window_size = 3
moving_avg_prices = calculate_moving_average(prices, window_size)

print(moving_avg_prices)
