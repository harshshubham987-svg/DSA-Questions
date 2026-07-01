# Question:
# Write a program to print the Fibonacci series up to n terms using recursion.
# Fibonacci series: 0, 1, 1, 2, 3, 5, ...
#
# Sample Input:
# 5
#
# Sample Output:
# 0
# 1
# 1
# 2
# 3

def fib(num):
    # Base cases
    if num == 0:
        return 0
    if num == 1:
        return 1

    # Recursive case
    return fib(num - 1) + fib(num - 2)

# Print Fibonacci series for first 5 terms
for i in range(5):
    print(fib(i))

# Time Complexity: O(2^n) - exponential due to repeated subproblem calculations
# Space Complexity: O(n) - recursion stack depth