'''
128. Longest Consecutive Sequence

Given an unsorted array of integers.

Return the length of the
longest consecutive sequence.

The algorithm must run
in O(n) time.

Example 1:

Input:

nums = [100,4,200,1,3,2]

Output:

4

Sequence:

1,2,3,4

Example 2:

Input:

nums = [0,3,7,2,5,8,4,6,0,1]

Output:

9

Sequence:

0,1,2,3,4,5,6,7,8

Example 3:

Input:

nums = [1,0,1,2]

Output:

3

Sequence:

0,1,2
'''

# Solution


def main():

    # Input array
    nums = [0,3,7,2,5,8,4,6,0,1]

    # Store unique numbers
    mapp = {}

    # Insert every unique number
    for i in nums:

        if i not in mapp:
            mapp[i] = 1

    # Store maximum sequence length
    count = 0

    # Traverse every unique number
    for num in mapp:

        # Current sequence length
        c = 0

        # Offset for consecutive numbers
        i = 0

        # Start only if current number
        # is the beginning of a sequence
        if num - 1 not in mapp:

            # Count consecutive numbers
            while num + i in mapp:

                c += 1

                i += 1

            # Update maximum sequence length
            count = max(count, c)

    # Print longest sequence length
    print(count)


# Main function execution
if __name__ == "__main__":
    main()


# Time Complexity: O(n)
# Space Complexity: O(n)


'''
Theory Explanation:

1. The main challenge is

finding the longest
consecutive sequence

without sorting.

Sorting would take

O(n log n),

which violates
the required complexity.

2. Store every unique number
inside a HashMap (or Set).

This allows

O(1)

average lookup.

Example:

nums

[100,4,200,1,3,2]

Hash Set

{100,4,200,1,3,2}

3. Do NOT start counting
from every number.

Instead,

start only from
the beginning
of a sequence.

How do we know?

If

num - 1

does not exist,

then

num is the first element
of a consecutive sequence.

Example:

Set:

{1,2,3,4}

For

1

0 does not exist.

Therefore,

1 is the starting point.

For

2

1 exists.

So

2 cannot be
the beginning.

Skip it.

For

3

2 exists.

Skip.

For

4

3 exists.

Skip.

4. Once a starting number
is found,

keep checking

num + 1

num + 2

num + 3

...

until the sequence ends.

Example:

Start:

1

Check:

2 ✔

3 ✔

4 ✔

5 ✘

Sequence Length = 4

5. Update the maximum length.

Continue with the remaining numbers.

6. Duplicate values

do not affect the answer.

Using a Set removes them automatically.

Example:

[1,0,1,2]

Set

{0,1,2}

Sequence

0 → 1 → 2

Length = 3

Important Steps:

-> Store all numbers in a HashSet (or HashMap).
-> Traverse only unique numbers.
-> Start counting only when (num - 1) is absent.
-> Continue checking consecutive numbers.
-> Update the maximum sequence length.
-> Ignore duplicate numbers automatically.

Key Intuition:

Every consecutive sequence
has exactly one starting element.

Instead of checking
from every number,

only begin counting
from numbers
whose previous value
does not exist.

This guarantees that
every sequence
is visited exactly once,
making the algorithm O(n).

Pattern:

HashSet
+
Sequence Detection
+
Linear Traversal
=
Longest Consecutive Sequence
'''