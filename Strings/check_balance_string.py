'''
3340. Check Balanced String

You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

Example 1:

Input: num = "1234"
Output: false

Example 2:

Input: num = "24123"
Output: true
'''

# solution

num = "1234"

# Store sum of odd index digits
odd = 0

# Store sum of even index digits
even = 0

# Traverse through the string
for i in range(len(num)):
    
    # If index is even
    if i % 2 == 0:
        even += int(num[i])
    
    # If index is odd
    else:
        odd += int(num[i])

# Check if both sums are equal
if odd == even:
    print(True)
else:
    print(False)

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses simple Traversal.

2. The idea:
   -> Separate digits based on index.
   -> Add even index digits into "even".
   -> Add odd index digits into "odd".

3. After traversal:
   Compare both sums.

4. If both sums are equal:
   String is balanced.

5. Otherwise:
   String is not balanced.

Important Steps:

-> Index starts from 0.
-> 0, 2, 4... are even indices.
-> 1, 3, 5... are odd indices.
-> Convert string digit into integer using int().

Key Intuition:

Group digits by position
and compare their total sums.
'''