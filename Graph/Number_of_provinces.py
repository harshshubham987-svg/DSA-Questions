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
