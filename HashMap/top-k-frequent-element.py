'''
347. Top K Frequent Elements

Given an integer array nums
and an integer k.

Return the k most
frequent elements.

The answer may be
returned in any order.

Example 1:

Input:

nums = [1,1,1,2,2,3]

k = 2

Output:

[1,2]

Example 2:

Input:

nums = [1]

k = 1

Output:

[1]

Example 3:

Input:

nums = [1,2,1,2,1,2,3,1,3,2]

k = 2

Output:

[1,2]
'''

# Solution


def main():

    # Input array
    nums = [1,1,1,2,2,3]

    # Number of frequent elements required
    k = 2

    # Store frequency of every number
    mapp = {}

    # Length of input array
    n = len(nums)

    # Count frequency of every element
    for num in nums:

        if num in mapp:

            mapp[num] += 1

        else:

            mapp[num] = 1

    # Bucket array where
    # index = frequency
    bucket = [[] for _ in range(n + 1)]

    # Place every number
    # into its frequency bucket
    for key, freq in mapp.items():

        bucket[freq].append(key)

    # Store final answer
    ans = []

    # Traverse buckets
    # from highest frequency
    # to lowest frequency
    for i in range(n, -1, -1):

        arr = bucket[i]

        if len(ans) < k:

            if len(arr) != 0:

                # Add all numbers
                # having same frequency
                for val in arr:

                    ans.append(val)

        else:

            break

    # Print answer
    print(ans)


# Main function execution
if __name__ == "__main__":
    main()


# Time Complexity: O(n)
# Space Complexity: O(n)


'''
Theory Explanation:

1. The first step is to count
   how many times each number
   appears in the array.

Example:

nums

[1,1,1,2,2,3]

Frequency Map

1 → 3

2 → 2

3 → 1

2. Instead of sorting the
frequency map,

we use Bucket Sort.

Why?

The maximum possible frequency
of any element is

n

(where n is the length
of the array).

So we create

n + 1

buckets.

Each bucket index
represents a frequency.

Example:

bucket[0]

Numbers occurring
0 times

bucket[1]

Numbers occurring
1 time

bucket[2]

Numbers occurring
2 times

...

bucket[n]

Numbers occurring
n times

3. Place every number
inside its frequency bucket.

Example:

Frequency Map

1 → 3

2 → 2

3 → 1

Bucket becomes

Index 0

[]

Index 1

[3]

Index 2

[2]

Index 3

[1]

4. Now traverse the buckets
from the highest frequency
to the lowest.

Start from

bucket[n]

because it contains
the most frequent elements.

Whenever a bucket
contains values,

add them to the answer.

Example:

bucket[3]

[1]

Answer

[1]

Next

bucket[2]

[2]

Answer

[1,2]

Now we already have

k = 2

elements,

so stop.

5. This avoids sorting
the frequencies.

Sorting would require

O(n log n)

Bucket Sort allows us
to solve the problem
in linear time.

6. Why does Bucket Sort work?

Every element belongs
to exactly one frequency.

Each frequency has
its own bucket.

By visiting the buckets
from largest frequency
to smallest,

we automatically process
elements in decreasing
order of occurrence.

Important Steps:

-> Count the frequency of every element.
-> Create n + 1 buckets.
-> Store every number inside its frequency bucket.
-> Traverse buckets from highest frequency to lowest.
-> Collect elements until k elements are obtained.
-> Return the collected elements.

Key Intuition:

Instead of sorting
the frequency map,

group elements
according to
their frequencies.

Since the maximum frequency
cannot exceed n,

the frequency itself
can be used
as an array index.

Scanning the buckets
backwards directly gives
the most frequent elements
without any sorting.

Pattern:

HashMap
+
Frequency Counting
+
Bucket Sort
+
Reverse Traversal
=
Top K Frequent Elements
'''