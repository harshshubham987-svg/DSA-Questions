'''
547. Number of Provinces

There are n cities.

A province is a group of cities
that are directly or indirectly connected.

Given an adjacency matrix isConnected,
return the total number of provinces.

Example 1:

Input:
isConnected = [
[1,1,0],
[1,1,0],
[0,0,1]
]

Output: 2

Example 2:

Input:
isConnected = [
[1,0,0],
[0,1,0],
[0,0,1]
]

Output: 3
'''

# Solution:

def dfs(isconect, city, visit):

    # Return if city is already visited
    if city in visit:
        return

    # Mark current city as visited
    visit.add(city)

    # Traverse all connected cities
    for next_city in range(len(isconect[0])):

        # If cities are connected and not visited
        if isconect[city][next_city] == 1 and next_city not in visit:

            # Visit the connected city
            dfs(isconect, next_city, visit)


def main():

    # Input adjacency matrix
    isconnected = [[1,0,0],
                   [0,1,0],
                   [0,0,1]]

    # Store visited cities
    visit = set()

    # Store total provinces
    count = 0

    # Traverse every city
    for city in range(len(isconnected)):

        # If city is not visited,
        # a new province is found
        if city not in visit:

            # Increase province count
            count += 1

            # Visit all cities in this province
            dfs(isconnected, city, visit)

    # Print final answer
    print(count)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n²)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses DFS on a Graph.

2. Here:
   -> Each city is a node.
   -> isConnected represents edges.

3. Traverse every city.

4. If a city is not visited:
   -> It belongs to a new province.
   -> Increase province count.
   -> Start DFS.

5. DFS visits every city
   directly or indirectly connected
   to the current city.

6. After DFS completes,
   the entire province is marked visited.

Important Steps:

-> Use visited set to avoid revisiting cities.
-> Start DFS only from unvisited cities.
-> One DFS finishes one complete province.
-> Count how many DFS calls are made.

Key Intuition:

Every unvisited city starts
a new connected component.
Each connected component
represents one province.
'''


""" =======================    DSU - Disjoint Set Union (Approach) Algorithm===================================="""

"""
547. Number of Provinces

There are n cities.

Some cities are directly connected.

If city A is connected to city B,
and city B is connected to city C,

then

A, B and C belong
to the same province.

Return the total number
of provinces.

Example:

Input:

[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output:

2

Province 1:

0 → 1

Province 2:

2
"""

# Solution


class DSU:

    def __init__(self, n):

        # Total number of nodes
        self.n = n

        # Initially every node
        # is its own parent
        self.parent = [i for i in range(n)]

        # Every component starts
        # with size 1
        self.size = [1] * n

        self.count = 1

    # Find Ultimate Parent
    def find(self, x):

        # Node is its own parent
        if self.parent[x] == x:
            return x

        # Path Compression
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Union By Size
    def union(self, x, y):

        # Find ultimate parents
        u = self.find(x)
        v = self.find(y)

        # Already in same component
        if u == v:
            return

        # Component sizes
        sz1 = self.size[u]
        sz2 = self.size[v]

        # Attach smaller tree
        # below larger tree
        if sz1 >= sz2:

            self.parent[v] = u

            self.size[u] += self.size[v]

        else:

            self.parent[u] = v

            self.size[v] += self.size[u]


def main():

    # Adjacency Matrix
    con = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]

    # Number of cities
    n = len(con)

    # Create DSU
    d = DSU(n)

    # Traverse upper triangle only
    for i in range(len(con)):

        for j in range(i + 1, len(con[0])):

            # If two cities are connected
            if con[i][j] == 1:

                # Merge both provinces
                d.union(i, j)

    # Store unique province leaders
    leader = set()

    # Find ultimate parent
    # of every city
    for i in range(n):

        leader.add(d.find(i))

    # Number of provinces
    print("Total Group :- ", len(leader))


# Main function execution
if __name__ == "__main__":
    main()


# Time Complexity: O(n² × α(n))
# Space Complexity: O(n)


"""
Theory Explanation:

1. This problem uses

Disjoint Set Union (DSU)

also known as

Union Find.

2. Initially,

every city
is considered
its own province.

Example:

0

1

2

Parent:

[0,1,2]

3. Traverse
the adjacency matrix.

Whenever

con[i][j] == 1

it means

City i
and
City j

belong to
the same province.

4. Merge them
using Union.

Example:

0 ---- 1

After Union

Parent:

0

↓

1

becomes

0

Parent:

[0,0,2]

5. Union By Size

always attaches

the smaller component

below

the larger component.

This keeps
the tree shallow.

6. Path Compression

Whenever

find(node)

is called,

every node
directly points

to its ultimate parent.

Example:

Before:

3

↓

2

↓

1

↓

0

After find(3):

3

↓

0

2

↓

0

1

↓

0

Future searches
become almost O(1).

7. After processing
all connections,

find the leader
of every city.

Example:

Leader Set:

{0,2}

Total Provinces:

2

8. Size of the leader set
is the answer.

Important Steps:

-> Initially every city is its own parent.
-> Traverse only the upper triangle of the matrix.
-> Whenever connection exists, perform Union.
-> Use Union By Size for efficient merging.
-> Use Path Compression inside Find.
-> Store every ultimate parent in a set.
-> Number of unique leaders equals the number of provinces.

Key Intuition:

Every connected city
belongs to the same group.

DSU continuously merges
connected cities
into one component.

At the end,

every connected component
has exactly one ultimate parent.

Counting unique parents
gives the number
of provinces.

Pattern:

Graph
+
Disjoint Set Union (Union Find)
+
Union By Size
+
Path Compression
=
Number of Connected Components (Provinces)
"""