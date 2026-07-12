'''
739. Daily Temperatures

Given an array of integers temperatures,
return an array answer where answer[i]
represents the number of days
you have to wait to get a warmer temperature.

If no warmer day exists,
answer[i] remains 0.

Example 1:

Input:
temperatures = [73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]

Example 2:

Input:
temperatures = [30,40,50,60]

Output:
[1,1,1,0]

Example 3:

Input:
temperatures = [30,60,90]

Output:
[1,1,0]
'''

# solution


"""=============================== BruteFouce Approach ======================="""

temp = [73,74,75,71,69,72,76,73]

# Store final answer
ans = []

# Traverse every temperature
for i in range(len(temp)):

    # Store current day's temperature
    old_tem = temp[i]

    # Track whether a warmer day is found
    found = False

    # Search for warmer temperature in future days
    for j in range(i + 1, len(temp)):

        # Check if future temperature is warmer
        if old_tem < temp[j]:

            # Mark warmer day as found
            found = True

            # Store number of days waited
            ans.append(j - i)

            # Stop after finding first warmer day
            break

    # If no warmer day exists
    if not found:

        # Store 0 for current day
        ans.append(0)

# Print final answer
print(ans)

# Time Complexity: O(n²)
# Space Complexity: O(n)


'''
Theory Explanation (Brute Force):

1. Traverse every temperature.

2. For each day:
   Search all future days.

3. Find the first future day
   whose temperature is greater.

4. Calculate waiting days:

   future_index - current_index

5. If no warmer day exists:
   Store 0.

Important Steps:

-> Search only future days.
-> Stop at first warmer temperature.
-> j - i gives waiting days.
-> Use found to handle no warmer day.

Key Intuition:

For every day,
look ahead until the first warmer day is found.
'''


"""====================================Optimal Approach=============================="""


def main():

    # Input temperatures
    temp = [30,60,90]

    # Create answer array with default 0
    ans = [0] * len(temp)

    # Stack stores indices of unresolved temperatures
    stack = []

    # Traverse every temperature
    for i in range(len(temp)):

        # Resolve all previous smaller temperatures
        while stack and temp[i] > temp[stack[-1]]:

            # Calculate waiting days
            days = i - stack[-1]

            # Store answer for stack top index
            ans[stack[-1]] = days

            # Remove resolved index from stack
            stack.pop()

        # Store current index in stack
        stack.append(i)

    # Print final answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n)
# Space Complexity: O(n)


'''
Theory Explanation (Optimal Approach):

1. This problem uses Monotonic Stack.

2. Stack stores indices,
   not temperature values.

Why indices?

Because we need to calculate:

current_index - previous_index

3. Stack contains days
   whose next warmer temperature
   has not been found yet.

4. For every current temperature:

   Compare it with the temperature
   at the top index of stack.

5. If:

   temp[i] > temp[stack[-1]]

   Current day is warmer.

6. Calculate waiting days:

   i - stack[-1]

7. Store the answer
   for that previous day.

8. Pop the resolved index.

9. Use while loop because
   one current temperature can resolve
   multiple previous days.

Example:

temp = [73,74,75]

i = 0:
stack = [0]

i = 1:
74 > 73

answer[0] = 1 - 0 = 1

stack = [1]

i = 2:
75 > 74

answer[1] = 2 - 1 = 1

stack = [2]

Important Steps:

-> Stack stores indices.
-> Keep unresolved days in stack.
-> Current warmer day resolves stack top.
-> Use while for multiple resolutions.
-> Remaining stack indices keep answer 0.

Key Intuition:

The stack is waiting
for a warmer temperature.

Whenever a warmer day arrives,
resolve all smaller temperatures
waiting at the top of the stack.

Pattern:

Next Greater Element
+
Index Difference
=
Daily Temperatures
'''