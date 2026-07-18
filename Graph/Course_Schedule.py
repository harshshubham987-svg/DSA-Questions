"""
207. Course Schedule

There are numCourses courses
numbered from:

0 to numCourses - 1

A prerequisite pair:

[a, b]

means:

Take course b first,
then course a.

Return:

True  -> if all courses can be completed.

False -> if it is impossible
because of a cycle.

Example 1:

Input:

numCourses = 2

prerequisites =
[[1,0]]

Output:

True

Order:

0 → 1


Example 2:

Input:

numCourses = 2

prerequisites =
[[1,0],[0,1]]

Output:

False

Reason:

0 depends on 1
and
1 depends on 0

Cycle exists.
"""

# Solution

from collections import deque


def main():

    # Total number of courses
    numCourse = 2

    # Prerequisite list
    prerequ = [[1,0]]

    # Adjacency list
    graph = {}

    # Store indegree of every node
    indegree = {}

    # Count completed courses
    complete = 0

    # Create graph and indegree
    for i in range(numCourse):

        graph[i] = []

        indegree[i] = 0

    # Build graph
    for pair in prerequ:

        # Source course
        u = pair[1]

        # Destination course
        v = pair[0]

        # Create directed edge
        u = > v
        graph[u].append(v)

        # Increase indegree
        indegree[v] += 1

    # Queue for Kahn's Algorithm
    q = deque()

    # Add all nodes having indegree 0
    for deg in indegree:

        if indegree[deg] == 0:
            q.append(deg)

    # If no starting node exists,
    # cycle is present
    if not q:
        return False

    # Topological Sort
    while q:

        # Remove current course
        nod = q.popleft()

        # One course completed
        complete += 1

        # Visit all dependent courses
        for nei in graph[nod]:

            # Remove incoming edge
            indegree[nei] -= 1

            # If prerequisite becomes satisfied
            if indegree[nei] == 0:

                # Add into queue
                q.append(nei)

    # If every course was completed
    if complete == numCourse:

        return True

    # Otherwise cycle exists
    return False


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

"""
Theory Explanation:

1. This problem is solved using
   Topological Sorting
   (Kahn's Algorithm).

2. Think of every course
   as a graph node.

3. Every prerequisite creates
   a directed edge.

Example:

[1,0]

means

0 → 1

because

Course 0
must be completed
before Course 1.

4. indegree[node]

stores

How many prerequisites
are still required
before taking this course.

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

5. Every course
having indegree = 0

can be taken immediately.

Push them into the queue.

6. Remove one course
from the queue.

That means
the course has been completed.

7. Visit all neighbouring courses.

Decrease their indegree.

Because one prerequisite
has now been completed.

8. Whenever
indegree becomes zero,

push that course
into the queue.

9. Continue
until the queue becomes empty.

10. Count how many courses
were completed.

If:

completed == total courses

Every course
was successfully finished.

Return True.

Otherwise,

some courses
could never reach indegree 0.

That means
a cycle exists.

Return False.

Example:

0 → 1
↓

2

Topological Order:

0
↓

1
2

Possible.

Example with cycle:

0 → 1
↑   ↓
└───┘

Indegree:

0 : 1
1 : 1

Queue is empty.

No course can be started.

Return False.

Important Steps:

-> Build adjacency list.
-> Calculate indegree of every course.
-> Push all indegree 0 courses into queue.
-> Remove one course at a time.
-> Reduce indegree of neighbours.
-> Push neighbour when indegree becomes 0.
-> Count completed courses.
-> If completed equals total courses, return True.

Key Intuition:

A course can only be taken
after all its prerequisites
have been completed.

Indegree tells us
how many prerequisites
are still pending.

By repeatedly taking
courses with indegree 0,

we naturally build
a valid course order.

If at the end
some courses are still unfinished,

they are trapped inside a cycle.

Pattern:

Directed Graph
+
Indegree
+
Queue
+
Topological Sort (Kahn's Algorithm)
=
Course Schedule
"""