'''
11. Container With Most Water

You are given an integer array height.

Each element represents height of a vertical line.

Find two lines that form the container
which stores maximum water.

Formula:
Area = width × min(left_height, right_height)
'''

# Solution:

height = [1,8,6,2,5,4,8,3,7]

# Left pointer
lef = 0

# Right pointer
rig = len(height) - 1

# Store maximum water
most_water = 0

# Apply two-pointer approach
while lef < rig:

    # Store current left height
    lef_v = height[lef]

    # Store current right height
    rig_v = height[rig]

    # Calculate width
    width = rig - lef

    # Current area = width × minimum height
    curr = width * min(lef_v, rig_v)

    # Update maximum water
    most_water = max(most_water, curr)

    # Move smaller height pointer
    if rig_v > lef_v:
        lef += 1

    elif rig_v == lef_v:
        rig -= 1
        lef += 1

    else:
        rig -= 1

    # Print current details
    print(f"left value : {lef_v} , Right value : {rig_v}, current : {curr}")

# Print final answer
print(most_water)

# Time Complexity: O(n)
# Space Complexity: O(1)

'''
Theory Explanation:

1. This problem uses Two Pointer.

2. Water stored depends on:
   -> Width between pointers
   -> Smaller height

Formula:
Area = (right - left) × min(height[left], height[right])

3. Start with:
   left = 0
   right = n-1

4. Calculate area.

5. Move the smaller height pointer.

Why?

Because:
Moving bigger height cannot increase area,
since smaller height limits water.

Important Steps:

-> Always calculate area first.
-> Use min(left, right).
-> Move smaller pointer only.
-> Update maximum every time.

Key Intuition:

Wider container at start,
then shrink smartly
by removing smaller walls.
'''