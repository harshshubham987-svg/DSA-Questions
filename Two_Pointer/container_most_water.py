'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= heigh
'''

height = [1,8,6,2,5,4,8,3,7]

lef = 0
rig = len(height)-1
most_water = 0

while lef < rig:
    lef_v = height[lef]
    rig_v = height[rig]
    
    curr = rig-lef
    if rig_v > lef_v:
        lef += 1
        curr = curr*lef_v
    elif rig_v == lef_v:
        rig -= 1
        lef += 1
        curr = curr*lef_v
    else:
        rig -= 1
        curr = curr*rig_v
    
    most_water = max(most_water , curr)
    print(f"left value : {lef_v} , Right value : {rig_v}, current : {curr}")


print(most_water)