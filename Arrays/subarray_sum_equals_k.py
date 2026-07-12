'''560. Subarray Sum Equals K

Given an array of integers nums and an integer k,
return the total number of subarrays
whose sum equals to k.

A subarray is a contiguous non-empty
sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

# Solution

nums = [1,1,1]
k = 2

# Store prefix sum and its frequency
mapp = {}

# Empty prefix sum occurs once
mapp[0] = 1

# Store total valid subarrays
cu = 0

# Store current prefix sum
curr = 0

# Traverse the array
for i in range(len(nums)):

    # Calculate current prefix sum
    curr += nums[i]

    # Find required previous prefix sum
    need = curr - k

    # If required prefix sum exists
    if need in mapp:

        # Add its frequency to total count
        cu += mapp[need]

    # Store current prefix sum frequency
    mapp[curr] = mapp.get(curr, 0) + 1

# Print total valid subarrays
print(cu)

# Print prefix sum frequency map
print(mapp)

# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Prefix Sum + HashMap.

2. curr stores the prefix sum
   from index 0 to current index.

3. We need a subarray whose sum is k.

Suppose:

current_prefix - previous_prefix = k

Rearrange:

previous_prefix = current_prefix - k

Therefore:

need = curr - k

4. For every current prefix sum,
   we search whether "need"
   already exists in the HashMap.

5. If need exists:

   It means removing that previous prefix
   from current prefix gives sum k.

Example:

nums = [1,1,1]
k = 2

Prefix sums:

Index 0:
curr = 1

need = 1 - 2 = -1

Not found.

Store:
1 -> 1


Index 1:
curr = 2

need = 2 - 2 = 0

0 exists once.

Count = 1

Subarray:
[1,1]


Index 2:
curr = 3

need = 3 - 2 = 1

1 exists once.

Count = 2

Subarray:
[1,1]

6. HashMap stores:

prefix_sum -> frequency

Example:

{
    0: 1,
    1: 1,
    2: 1,
    3: 1
}

7. Frequency is important.

If the same prefix sum appears
multiple times,
each occurrence can create
a different valid subarray.

Important Steps:

-> mapp[0] = 1 handles subarrays
   starting from index 0.

-> Calculate curr first.

-> Find:
   need = curr - k

-> Add mapp[need] to count.

-> Store current prefix sum
   after checking need.

Key Intuition:

We want:

Subarray Sum = K

Using prefix sum:

Current Prefix - Old Prefix = K

So:

Old Prefix = Current Prefix - K

Find how many times
that old prefix appeared.

Each occurrence represents
one valid subarray.
'''