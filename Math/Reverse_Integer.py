'''
7. Reverse Integer

Given a signed 32-bit integer x,
return the integer with its digits reversed.

If the reversed integer overflows
the 32-bit signed integer range,
return 0.

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
'''

# Solution

def main():

    # Input number
    x = 123

    # Store absolute value
    a = abs(x)

    # Store reversed number
    r_x = 0

    # Reverse digits
    while a > 0:

        # Extract last digit
        r = a % 10

        # Check 32-bit integer overflow
        if (r_x * 10) + r < (2 ** 31) - 1 :

            # Build reversed number
            r_x = (r_x * 10) + r

        else:
            return 0

        # Remove last digit
        a = a // 10

    # Restore original sign
    if x < 0:
        return (-1) * r_x

    else:
        return r_x


# Print final answer
print(main())

# Time Complexity: O(log₁₀ n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Math.

2. First:
   Store absolute value of number.

3. Extract digits one by one using:

   digit = number % 10

4. Build reversed number:

   reverse = reverse * 10 + digit

5. Remove last digit:

   number = number // 10

6. Before updating reverse,
   check whether it exceeds
   32-bit signed integer range.

7. Finally:
   Restore the original sign.

Important Steps:

-> Use abs() to handle negative numbers.
-> Extract digits using modulus.
-> Remove digits using integer division.
-> Check overflow before updating.
-> Restore sign at the end.

Key Intuition:

Take digits from right to left
and rebuild the number
from left to right.
'''