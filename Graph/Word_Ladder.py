'''
127. Word Ladder

A transformation sequence changes
one character at a time.

Each transformed word
must exist in wordList.

Return the length of the
shortest transformation sequence.

If no sequence exists,
return 0.

Example 1:

Input:
beginWord = "hit"
endWord = "cog"

wordList =
["hot","dot","dog","lot","log","cog"]

Output:
5

Transformation:

hit
→ hot
→ dot
→ dog
→ cog

Example 2:

Input:
beginWord = "hit"
endWord = "cog"

wordList =
["hot","dot","dog","lot","log"]

Output:
0
'''

# Solution

from collections import deque


def main():

    # Starting word
    beginword = "hit"

    # Target word
    endword = "cog"

    # Dictionary of valid words
    wordlist = ["hot","dot","dog","lot","log","cog"]

    # Store words for O(1) lookup
    wordset = set()

    # Store current transformation length
    count = 0

    # All lowercase letters
    alpha = [
        'a','b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

    # Insert all words into set
    for word in wordlist:
        wordset.add(word)

    # Queue for BFS
    q = deque()

    # Start from beginWord
    q.append(beginword)

    # Remove beginWord if present
    if beginword in wordset:
        wordset.remove(beginword)

    # If target word does not exist
    if endword not in wordset:
        return 0

    # Apply BFS
    while q:

        # Number of words in current BFS level
        size = len(q)

        # Increase transformation length
        count += 1

        # Process current BFS level
        for _ in range(size):

            # Remove current word
            word = q.popleft()

            # Change every character
            for i in range(len(word)):

                # Prefix
                f = word[:i]

                # Suffix
                en = word[i + 1:]

                # Try every alphabet
                for c in alpha:

                    # Skip same character
                    if c == word[i]:
                        continue

                    # Create neighbouring word
                    neb = f + c + en

                    # If neighbour exists in dictionary
                    if neb in wordset:

                        # Add into BFS queue
                        q.append(neb)

                        # Mark as visited
                        wordset.remove(neb)

                        # Destination reached
                        if neb == endword:
                            return count + 1

    # No transformation exists
    return 0


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(N × L × 26)
# Space Complexity: O(N)

'''
Theory Explanation:

1. This problem uses BFS on an Implicit Graph.

2. Every word is treated
   as a graph node.

3. Two words are connected
   if they differ
   by exactly one character.

Example:

hot

↓

dot
lot

4. BFS is used because
   we need the shortest transformation.

5. Start BFS from beginWord.

6. For every word:

   Change each character
   one position at a time.

Example:

hit

Position 0:

ait
bit
cit
...

zit

Position 1:

hat
hbt
...

Position 2:

hia
hib
...

7. Every generated word
   is checked inside wordSet.

8. If the generated word exists:

   -> Push into queue.
   -> Remove from wordSet.

9. Removing immediately
   marks the word as visited.

10. One BFS level
    represents one transformation.

11. As soon as endWord is found,
    return current level + 1.

Because BFS always reaches
the shortest path first.

Important Steps:

-> Convert wordList into a set.
-> Use BFS for shortest transformation.
-> Generate neighbours by replacing one character.
-> Remove visited words immediately.
-> One BFS level = one transformation step.

Key Intuition:

Imagine every word
as a node in a graph.

Instead of storing all edges,
generate neighbouring words
by changing one letter.

BFS guarantees
the first time we reach endWord
is the shortest transformation.

Pattern:

Implicit Graph
+
BFS
+
Word Generation
=
Shortest Word Ladder
'''