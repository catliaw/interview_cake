### Problem: ###


# Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was
# 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns
# the best profit I could have made from 1 purchase and 1 sale of 1 Apple
# stock yesterday.

# For example:

#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# # returns 6 (buying for $5 and selling for $11)

# No "shorting"-you must buy before you sell. You may not buy and sell in the
# same time step (at least 1 minute must pass).

# In: list of stock prices in chronological order (oldest to newest)
# Out: greatest profit


### Pseudocode: ###


# Note: index --> minutes past 9:30am
# Set buy price to value at first index
# Compare to subsequent prices for (positive) profit
# Set largest profit to max_profit variable
# Set buy price to next value in stock_prices_yesterday list
# Repeat
# update max_profit variable if largest profit of 2nd buy price is larger than
# previous profit at previous buy price


### First attempt: Fail, hahaha ###


# def get_max_profit(stock_prices_yesterday):
#     """Return the best profit from 1 purchase & 1 sale of 1 Apple stock yesterday"""

#     buy_price = None
#     current_profit = None
#     max_profit = None

#     for price in stock_prices_yesterday:
#         while ...
#         for index in range(len(stock_prices_yesterday)):


### Interview Cake Hint 1: Brute Forcing It ###
### Runtime is O(n^2)) because going through 2 nested loops ###


def brute_get_max_profit(stock_prices_yesterday):

    max_profit = 0

    # go through every time
    for outer_time in xrange(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in xrange(len(stock_prices_yesterday)):

            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


def better_get_max_profit(stock_prices_yesterday):
    # for inner_time, changed xrange to range, included outer_range as lower
    # range for the range list, so not going over duplicate time pairs

    max_profit = 0

    # go through every time
    for outer_time in xrange(len(stock_prices_yesterday)):

        # for every time, go through every OTHER time
        for inner_time in range(outer_time, len(stock_prices_yesterday)):

            # for each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # and use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price   = stock_prices_yesterday[later_time]

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


### Interview Cake Hint 2: More concise version of better_get_max_profit ###
### Runtime still O(n^2) becaise 2 nested loops. Just slightly less steps ###


def get_max_profit(stock_prices_yesterday):

    max_profit = 0

    # go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):

        # and go through all the LATER prices
        for later_price in stock_prices_yesterday[earlier_time+1:]:

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


