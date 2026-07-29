"""
Leetcode # 121 Best Time To Buy And Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.


Time Complexity: O(n)
Space Complexity: O(1)
"""


def maxProfit(prices):
    lowest = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < lowest:
            lowest = price
        else:
            profit = price - lowest
            if profit > max_profit:
                max_profit = profit
    return max_profit



    


print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0