'''744. Find Smallest Letter Greater Than Target

Hint:- 
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].'''

# solution :

le = ["c","f","j"]
target = "a"

# Start pointer
s = 0

# End pointer
e = len(le) - 1

# Default answer (for wrap around case)
ans = le[0]

# Apply binary search until start crosses end
while s <= e:
    
    # Find middle index
    mid = (s+e)//2

    # If current letter is greater than target
    if le[mid] > target:
        
        # Store it as possible answer
        ans = le[mid]
        
        # Search left side for smaller valid character
        e = mid - 1
    
    # Otherwise search right side
    else:
        s = mid + 1

# Print final answer
print(ans)

# Time Complexity: O(log n)
# Space Complexity: O(1)