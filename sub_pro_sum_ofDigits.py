"""1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15"""

# solution code:

n = 234
sm = 0  #storing the sum of number
pro = 1 # storing the product of number

while n != 0:
    r = n%10        # taking the once place number as a reminder
    sm += r         # adding the reminder to sm variable
    pro *= r        # multiplying the number to product variable
    n //= 10        # dividing the number with 10 so that r will not be taken again

print(pro-sm)