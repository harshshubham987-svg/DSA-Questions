'''
1319. Number of Operations to Make Network Connected

There are n computers
numbered from:

0 to n-1

Some computers are connected
using ethernet cables.

A cable can be removed
from one connection
and used to connect
two disconnected computers.

Return the minimum number
of operations required
to connect the entire network.

If impossible,
return -1.

Example 1:

Input:

n = 4

connections =
[[0,1],[0,2],[1,2]]

Output:

1

Example 2:

Input:

n = 6

connections =
[[0,1],[0,2],[0,3],[1,2],[1,3]]

Output:

2

Example 3:

Input:

n = 6

connections =
[[0,1],[0,2],[0,3],[1,2]]

Output:

-1
'''

# Solution


class DSU:

    def __init__(self, n):

        # Total number of computers
        self.n = n

        # Initially every computer
        # is its own leader
        self.leader = [i for i in range(n)]

        # Every component
        # starts with size 1
        self.size = [1] * n

        # Count redundant cables
        self.extra = 0

        # Initially every node
        # is an individual component
        self.component = n

    # Find Ultimate Parent
    def find(self, x):

        # Node is its own leader
        if self.leader[x] == x:
            return x

        # Path Compression
        self.leader[x] = self.find(self.leader[x])

        return self.leader[x]

    # Union By Size
    def union(self, x, y):

        # Find ultimate parents
        u = self.find(x)
        v = self.find(y)

        # Both computers
        # already belong
        # to the same component
        if u == v:

            # Extra cable found
            self.extra += 1

        # Merge smaller component
        # into larger component
        elif self.size[u] >= self.size[v]:

            self.leader[v] = u

            self.size[u] += self.size[v]

            # Components decrease
            self.component -= 1

        else:

            self.leader[u] = v

            self.size[v] += self.size[u]

            # Components decrease
            self.component -= 1


def main():

    # Network connections
    connection = [[0,1],
                  [0,2],
                  [0,3],
                  [1,2]]

    # Total computers
    n = 6

    # Create DSU
    d = DSU(n)

    # Total available cables
    operation = len(connection)

    # At least (n-1) cables
    # are required to connect n nodes
    if operation < n - 1:
        return -1

    # Process every cable
    for i in connection:

        u = i[0]
        v = i[1]

        d.union(u, v)

    # Total redundant cables
    extra = d.extra

    # Cables needed
    # to connect all components
    component = d.component - 1

    # Enough extra cables available
    if component <= extra:
        return component

    # Impossible to connect
    return -1


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(E × α(N))
# Space Complexity: O(N)


'''
Theory Explanation:

1. This problem uses

Disjoint Set Union (DSU)

also known as

Union Find.

2. Initially,

every computer
is its own component.

Example:

0

1

2

3

Components = 4

3. Traverse every cable.

For each cable,

perform Union.

4. If two computers
already belong
to the same component,

then

this cable is redundant.

It is called

an extra cable.

Example:

0 ----- 1
 \     /
  \   /
    2

When processing

1 ----- 2

all three computers
are already connected.

Therefore,

this cable
can be removed later.

extra += 1

5. Whenever two
different components merge,

component decreases.

Example:

Initially:

Components = 6

After connecting

0-1

Components = 5

After connecting

2-3

Components = 4

6. Suppose finally

Components = 3

Then

to connect
all components,

we need

Components - 1

extra cables.

Required cables:

3 - 1 = 2

7. If

extra >= required

we can reconnect
those redundant cables.

Return

required.

Otherwise,

return -1.

8. Important Observation

Before even using DSU,

check whether

Total Cables < n - 1

If true,

it is impossible
to connect all computers,

because

a connected graph
with n nodes

always requires
at least

n - 1 edges.

Return -1 immediately.

Example:

n = 6

Connections = 4

Minimum required:

5

Impossible.

Return -1.

Example:

n = 6

Connections = 5

After DSU:

Components = 3

Extra = 2

Required:

3 - 1 = 2

Since

extra >= required,

Answer:

2

Important Steps:

-> Initially every computer is its own component.
-> If two computers already have the same leader, count it as an extra cable.
-> Otherwise merge both components.
-> Reduce component count after every successful union.
-> Check if total cables are at least (n-1).
-> Required operations = components - 1.
-> If extra cables are enough, return required operations.
-> Otherwise return -1.

Key Intuition:

Every successful union
reduces the number
of disconnected components.

Every failed union
(indicating both nodes are already connected)

creates an extra cable
that can be reused later.

Finally,

to connect

k disconnected components,

exactly

k - 1

cables are needed.

If enough extra cables exist,

the network can be connected.

Pattern:

Graph
+
Disjoint Set Union (Union Find)
+
Union By Size
+
Path Compression
+
Connected Components
=
Minimum Operations to Connect Network
'''