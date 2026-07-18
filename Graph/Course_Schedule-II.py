"""
210. Course Schedule II

There are numCourses courses
numbered from:

0 to numCourses - 1

A prerequisite pair:

[a, b]

means

Course b must be completed
before Course a.

Return one valid order
to complete all courses.

If no valid order exists,
return an empty list.

Example 1:

Input:

numCourses = 2

prerequisites =
[[1,0]]

Output:

[0,1]

Example 2:

Input:

numCourses = 4

prerequisites =
[[1,0],[2,0],[3,1],[3,2]]

Output:

[0,2,1,3]

Another valid answer:

[0,1,2,3]

Example 3:

Input:

numCourses = 1

prerequisites = []

Output:

[0]
"""

# Solution

from collections import deque


def main():

    # Total number of courses
    numCourses = 4

    # Prerequisite list
    prereq = [[1,0],[2,0],[3,1],[3,2]]

    # Adjacency list
    graph = {}

    # Store indegree of every course
    indegree = {}

    # Count completed courses
    complete = 0

    # Create graph and indegree
    for i in range(numCourses):

        graph[i] = []

        indegree[i] = 0

    # Build directed graph
    for pair in prereq:

        # Source course
        u = pair[1]

        # Destination course
        v = pair[0]

        # Create edge: u -> v
        graph[u].append(v)

        # Increase indegree
        indegree[v] += 1

    # Queue for Kahn's Algorithm
    q = deque()

    # Push all courses having indegree 0
    for deg in indegree:

        if indegree[deg] == 0:
            q.append(deg)

    # Store final course order
    ans = []

    # Perform Topological Sort
    while q:

        # Remove current course
        nod = q.popleft()

        # One course completed
        complete += 1

        # Add course into answer
        ans.append(nod)

        # Visit dependent courses
        for neb in graph[nod]:

            # Remove one prerequisite
            indegree[neb] -= 1

            # If prerequisite count becomes zero
            if indegree[neb] == 0:

                # Add into queue
                q.append(neb)

    # If all courses completed
    if complete == numCourses:
        return ans

    # Cycle exists
    return []


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

"""
Theory Explanation:

1. This problem is an extension
   of Course Schedule (207).

2. Instead of returning

True / False,

we must return

the actual order
of taking the courses.

3. Every course
is treated as a graph node.

4. Every prerequisite

[a, b]

creates a directed edge

b → a

because

Course b
must be completed
before Course a.

5. indegree[node]

stores

How many prerequisites
are still remaining
before taking that course.

Example:

0 → 1
0 → 2
1 → 3
2 → 3

Indegree:

0 : 0
1 : 1
2 : 1
3 : 2

6. Every course
having indegree = 0

can be taken immediately.

Push all such courses
into the queue.

7. Remove one course
from the queue.

This means

the course is completed.

Add it to the answer list.

8. Visit all neighbouring courses.

Decrease their indegree.

Because one prerequisite
has now been satisfied.

9. Whenever
indegree becomes zero,

push that course
into the queue.

10. Continue until
the queue becomes empty.

11. If

completed == numCourses

then

answer list
contains one valid
topological ordering.

Return answer.

12. Otherwise,

some courses
could never become available.

A cycle exists.

Return [].

Example:

0 → 1
↓

2

↓

3

Possible order:

0
↓

1
↓

2
↓

3

or

0
↓

2
↓

1
↓

3

Both are correct.

Example with cycle:

0 → 1
↑   ↓
└───┘

Indegree:

0 : 1
1 : 1

Queue is empty.

No ordering exists.

Return [].

Important Steps:

-> Build adjacency list.
-> Calculate indegree of every course.
-> Push all indegree 0 courses into the queue.
-> Remove one course at a time.
-> Append it to the answer list.
-> Decrease indegree of neighbouring courses.
-> Push neighbour when indegree becomes 0.
-> If all courses are processed, return the answer.
-> Otherwise, return an empty list.

Key Intuition:

A course becomes available
only after all its prerequisites
have been completed.

Indegree tells us
how many prerequisites
are still pending.

By repeatedly selecting
courses with indegree 0,

we naturally generate
a valid order of completion.

If some courses
can never reach indegree 0,

they belong to a cycle,
making it impossible
to finish all courses.

Pattern:

Directed Graph
+
Indegree
+
Queue
+
Topological Sort (Kahn's Algorithm)
=
Course Ordering
"""