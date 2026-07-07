'''7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

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

def main():
    x = 123
    a = abs(x)
    r_x = 0

    while a > 0:
        r = a%10
        
        if (r_x*10) + r < (2**31)-1:
            r_x = (r_x*10) + r
            
        else:
            return 0
        a =a//10
    
    if x < 0:
        return (-1)*r_x
    else:
        return r_x

print(main())