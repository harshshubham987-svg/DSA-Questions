"""
733. Flood Fill

You are given an image represented by an m x n grid.

Starting from pixel (sr, sc),
change its color and all connected pixels
having the same original color.

A connected pixel means:
-> Up
-> Down
-> Left
-> Right

Return the modified image.

Example 1:

Input:
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]

sr = 1
sc = 1
color = 2

Output:
[[2,2,2],
 [2,2,0],
 [2,0,1]]

Example 2:

Input:
image = [[0,0,0],
         [0,0,0]]

sr = 0
sc = 0
color = 0

Output:
[[0,0,0],
 [0,0,0]]
"""

# Solution

def dfs(arr, row, col, color, area):

    # Base case:
    # If original color and new color are same,
    # no need to perform flood fill
    if area == color:
        return

    # Return if indices go outside the image
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        return

    # Return if current pixel is not part of target area
    elif arr[row][col] != area:
        return

    # Change current pixel color
    arr[row][col] = color

    # Visit upper pixel
    dfs(arr, row - 1, col, color, area)

    # Visit lower pixel
    dfs(arr, row + 1, col, color, area)

    # Visit left pixel
    dfs(arr, row, col - 1, color, area)

    # Visit right pixel
    dfs(arr, row, col + 1, color, area)


def main():

    # Input image
    image = [[1,1,1],
             [1,1,0],
             [1,0,1]]

    # Starting row
    sr = 1

    # Starting column
    sc = 1

    # New color
    color = 2

    # Store original color
    area = image[sr][sc]

    # Start DFS
    dfs(image, sr, sc, color, area)

    # Print modified image
    print(image)


# Main function execution
main()

# Time Complexity: O(m × n)
# Space Complexity: O(m × n)   # Recursive call stack (worst case)

"""
Theory Explanation:

1. This problem uses DFS (Depth First Search).

2. Start from the given pixel.

3. Store its original color.

4. Visit all connected pixels
   having the same original color.

5. Change their color to the new color.

6. Continue DFS in four directions:
   -> Up
   -> Down
   -> Left
   -> Right

7. Stop when:
   -> Out of boundary
   -> Different color encountered

Important Steps:

-> Save original color before DFS.
-> If original color equals new color,
   immediately return.
-> Mark current pixel before recursive calls.
-> Visit only four adjacent cells.

Key Intuition:

Start from one pixel,
spread to all connected pixels
having the same original color,
and repaint the entire connected region.
"""