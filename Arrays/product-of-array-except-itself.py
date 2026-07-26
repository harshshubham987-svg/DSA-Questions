'''
238. Product of Array Except Self

Given an integer array nums.

Return an array answer
where:

answer[i]

is equal to the product
of every element
except nums[i].

Division is NOT allowed.

Time Complexity
must be O(n).

Example 1:

Input:

nums = [1,2,3,4]

Output:

[24,12,8,6]

Example 2:

Input:

nums = [-1,1,0,-3,3]

Output:

[0,0,9,0,0]
'''

# Solution

# Input array
nums = [-1,1,0,-3,3]

# Store prefix products
left = ["-"] * len(nums)

# Build prefix product array
for i in range(len(nums)):

    # Prefix product
    if i > 0:

        left[i] = left[i - 1] * nums[i - 1]

    else:

        # No element on left side
        left[i] = 1


# Store suffix products
right = ["_"] * len(nums)

# Start from last index
en = len(nums) - 1

# Build suffix product array
while en >= 0:

    # Suffix product
    if en < len(nums) - 1:

        right[en] = right[en + 1] * nums[en + 1]

    else:

        # No element on right side
        right[en] = 1

    en -= 1


# Store final answer
ans = []

# Multiply prefix and suffix products
for i in range(len(nums)):

    ans.append(left[i] * right[i])

# Print answer
print(ans)

# Time Complexity: O(n)
# Space Complexity: O(n)


'''
Theory Explanation:

1. Division is not allowed.

Therefore,

we cannot simply compute

Total Product / nums[i].

2. Observe that

Product Except Self

can be divided into

Left Product

×

Right Product

Example:

nums =

[1,2,3,4]

For index 2

Answer should be

1 × 2 × 4

Instead think as

(Product on Left)

×

(Product on Right)

(1 × 2)

×

(4)

3. Build the Prefix Product array.

left[i]

stores

product of every element
before index i.

Example:

nums

[1,2,3,4]

left

Index 0

No elements before it

1

Index 1

1

Index 2

1×2 = 2

Index 3

1×2×3 = 6

Result:

left

[1,1,2,6]

4. Build the Suffix Product array.

right[i]

stores

product of every element
after index i.

Example:

nums

[1,2,3,4]

right

Index 3

No elements after it

1

Index 2

4

Index 1

3×4 = 12

Index 0

2×3×4 = 24

Result:

right

[24,12,4,1]

5. Final Answer

Multiply

left[i]

×

right[i]

Example:

left

[1,1,2,6]

right

[24,12,4,1]

Answer

24

12

8

6

6. This automatically handles zeros.

Example:

nums

[-1,1,0,-3,3]

left

[1,-1,-1,0,0]

right

[0,0,-9,3,1]

Answer

0

0

9

0

0

No special handling
for zero is needed.

Important Steps:

-> Build prefix product array.
-> Build suffix product array.
-> Prefix stores product before current index.
-> Suffix stores product after current index.
-> Multiply prefix and suffix for every index.
-> No division is used.

Key Intuition:

Every answer can be split into

(Product of Left Side)

×

(Product of Right Side)

Instead of removing one element,

precompute both products
independently.

Then combine them
to get the product
except self.

Pattern:

Prefix Product
+
Suffix Product
+
Array Traversal
=
Product of Array Except Self
'''