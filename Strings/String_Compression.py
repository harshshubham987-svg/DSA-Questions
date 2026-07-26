'''
443. String Compression

Given an array of characters,
compress it in-place.

For every consecutive group:

If count = 1

Store only the character.

If count > 1

Store:

Character
followed by
its frequency.

Return the new length
of the compressed array.

Example 1:

Input:

["a","a","b","b","c","c","c"]

Output:

6

Compressed:

["a","2","b","2","c","3"]

Example 2:

Input:

["a"]

Output:

1

Compressed:

["a"]

Example 3:

Input:

["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:

4

Compressed:

["a","b","1","2"]
'''

# Solution


def main():

    # Input characters
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    # Read pointer
    read = 0

    # Write pointer
    write = 0

    # Traverse the array
    while read < len(chars):

        # Store current character
        curr = chars[read]

        # Count frequency
        count = 0

        # Count consecutive occurrences
        while read < len(chars) and chars[read] == curr:

            read += 1

            count += 1

        # Write the character
        chars[write] = curr

        write += 1

        # If frequency is greater than 1
        if count > 1:

            # Store every digit separately
            for dig in str(count):

                chars[write] = dig

                write += 1

    # Print compressed array
    print(chars[:write])

    # Return compressed length
    return write


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(n)
# Space Complexity: O(1)


'''
Theory Explanation:

1. This problem uses
   the Two Pointer technique.

2. Two pointers are maintained:

   read

   -> Reads the original array.

   write

   -> Writes the compressed result
      back into the same array.

3. The read pointer
   moves through one group
   of identical characters.

Example:

a a a b b c

Initially

read

↓

a a a b b c

Count how many consecutive
'a' characters exist.

Count = 3

4. After counting,

write the character.

Array becomes:

a

Then,

since count > 1,

write

3

Result:

a3

5. Continue from
the next unread character.

Example:

b b

Count = 2

Write:

b2

6. If count == 1,

write only the character.

Example:

c

Write:

c

No count is stored.

7. If count has multiple digits,

convert count into a string.

Example:

Count = 12

Store separately:

'1'

'2'

Result:

b12

Array:

b 1 2

Each digit occupies
its own position.

8. Since writing happens
inside the original array,

no extra array is required.

Therefore,

space complexity
remains O(1).

Example Dry Run:

Input:

a b b b b b b b b b b b b

read

↓

Count:

a = 1

Write:

a

Next

Count:

b = 12

Write:

b

1

2

Final Array:

a b 1 2

Length:

4

Important Steps:

-> Use read pointer to count consecutive characters.
-> Use write pointer to overwrite the original array.
-> Write the character first.
-> Write count only when it is greater than 1.
-> Store each digit of the count separately.
-> Return the final write pointer as the new length.

Key Intuition:

The read pointer scans groups
of identical characters,

while the write pointer
builds the compressed string
directly inside the same array.

Since every character
is read exactly once
and written at most once,

the algorithm is both
efficient and in-place.

Pattern:

Two Pointers
+
Group Counting
+
In-Place Array Modification
=
String Compression
'''