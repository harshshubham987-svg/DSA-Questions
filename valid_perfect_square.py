'''367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
'''

# solution:

num = 14

# Start pointer
s = 1

# End pointer
e = num

# Store result (default False)
ans = False 

# Apply binary search until start crosses end
while s <= e:
    
    # Find middle number
    mid = (s+e)//2

    # Check if square of mid equals num
    if mid * mid == num:
        ans = True 
        break
    
    # If square is greater, search left side
    elif mid * mid > num:
        e = mid - 1
    
    # If square is smaller, search right side
    else:
        s = mid + 1

# Print final result
print(ans)

# Time Complexity: O(log n)
# Space Complexity: O(1)