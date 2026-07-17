'''
752. Open the Lock

A lock contains 4 wheels.

Each wheel contains digits:

0 1 2 3 4 5 6 7 8 9

Each move:

Rotate exactly one wheel
either forward or backward.

9 -> 0
0 -> 9

Initial State:

"0000"

Some combinations are deadends.

If the lock reaches
a deadend,
it cannot be used further.

Return the minimum number
of moves required
to reach the target.

If impossible,
return -1.

Example 1:

Input:

deadends =
["0201","0101","0102","1212","2002"]

target = "0202"

Output:

6

Example 2:

Input:

deadends = ["8888"]

target = "0009"

Output:

1

Example 3:

Input:

deadends =
["8887","8889","8878","8898",
 "8788","8988","7888","9888"]

target = "8888"

Output:

-1
'''

# Solution

from collections import deque


def main():

    # Deadend combinations
    deadends = []

    # Target combination
    target = "0000"

    # Initial lock state
    start = "0000"

    # Store deadends and visited combinations
    deadset = set()

    # Store current number of moves
    count = 0

    # Insert all deadends into set
    for d in deadends:
        deadset.add(d)

    # Queue for BFS
    q = deque()

    # If starting state is not blocked
    if start not in deadset:
        q.append(start)
    else:
        return -1

    # Apply BFS
    while q:

        # Number of combinations
        # at current BFS level
        size = len(q)

        # Process one BFS level
        for _ in range(size):

            # Remove current combination
            comb = q.popleft()

            # Target reached
            if target == comb:
                return count

            # Try rotating each wheel
            for i in range(len(comb)):

                # Left substring
                lef = comb[:i]

                # Right substring
                rig = comb[i + 1:]

                # Current digit
                dig = int(comb[i])

                # Rotate forward
                first = (dig + 1) % 10

                # Rotate backward
                sec = (dig - 1) % 10

                # New forward combination
                first_comb = lef + str(first) + rig

                # New backward combination
                sec_comb = lef + str(sec) + rig

                # Process forward move
                if first_comb not in deadset:

                    # Target found
                    if first_comb == target:
                        return count + 1

                    # Mark visited
                    deadset.add(first_comb)

                    # Add into queue
                    q.append(first_comb)

                # Process backward move
                if sec_comb not in deadset:

                    # Target found
                    if sec_comb == target:
                        return count + 1

                    # Mark visited
                    deadset.add(sec_comb)

                    # Add into queue
                    q.append(sec_comb)

        # Move to next BFS level
        count += 1

    # Target cannot be reached
    return -1


# Main function execution
if __name__ == "__main__":
    print(main())

# Time Complexity: O(10⁴)
# Space Complexity: O(10⁴)

'''
Theory Explanation:

1. This problem uses BFS
   on an Implicit Graph.

2. Every lock combination
   is considered as a graph node.

Example:

0000

Its neighbours are:

1000
9000
0100
0900
0010
0090
0001
0009

There are always
8 possible neighbours.

3. BFS is used because
   every move has equal cost (1).

Therefore,
the first time we reach
the target
is the minimum number of moves.

4. Start from:

0000

5. Before starting,

check whether
0000 is a deadend.

If yes,

return -1.

6. For every wheel:

Generate two neighbours.

Forward rotation:

digit + 1

Backward rotation:

digit - 1

Wrap-around is handled using:

Forward:

(digit + 1) % 10

Examples:

9 → 0

Backward:

(digit - 1) % 10

Examples:

0 → 9

because

(-1) % 10 = 9
in Python.

7. Every valid neighbour
is added into the queue.

8. As soon as a combination
is pushed into the queue,

it is added into deadset.

This serves two purposes:

• Deadends are skipped.
• Visited combinations
  are not processed again.

9. One BFS level
represents one move.

After processing one level:

count += 1

10. If target is never reached,

return -1.

Example:

0000

↓

1000
9000
0100
0900
0010
0090
0001
0009

These are processed first.

Then their neighbours.

This continues level by level
until target is found.

Important Steps:

-> Convert deadends into a set.
-> Treat each lock combination as a graph node.
-> Generate exactly 8 neighbouring combinations.
-> Use modulo for wheel wrap-around.
-> Mark combinations as visited immediately.
-> One BFS level represents one move.
-> First time reaching target gives the minimum moves.

Key Intuition:

The lock forms an implicit graph
of 10⁴ possible combinations
(from "0000" to "9999").

Instead of building all edges,
generate neighbouring combinations
by rotating one wheel
forward or backward.

Since every move costs exactly one,
BFS guarantees the shortest path.

Pattern:

Implicit Graph
+
State Space Search
+
Breadth First Search (BFS)
=
Minimum Turns to Open the Lock
'''