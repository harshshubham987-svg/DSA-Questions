'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
'''

# Solution:

prices = [7,1,5,3,6,4]

# Store maximum profit
max_pro = 0

# Assume first day as the best buying price
best_buy = prices[0]

# Traverse all prices
for p in prices:
    
    # Update best buying price if smaller price is found
    best_buy = min(p, best_buy)

    # Calculate current profit
    profit = p - best_buy

    # Update maximum profit
    max_pro = max(max_pro, profit)

# Print final maximum profit
print(max_pro)

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Greedy approach.

2. The idea is simple:
   -> Keep track of the lowest price (best buy)
   -> Calculate profit for every day
   -> Keep the maximum profit

3. "best_buy" stores the minimum price seen so far.

4. At each step:
   profit = current price - best_buy

5. If current profit is bigger than previous max profit,
   update max_pro.

Important Steps:

-> Buying must always happen before selling.
-> So we keep updating best_buy only from left to right.
-> We never check future prices for buying.
-> This makes it a one-pass solution.

Key Intuition:

Lowest buy price + highest possible sell after it = maximum profit.
'''