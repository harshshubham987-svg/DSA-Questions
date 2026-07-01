"""1732. Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1."""

gain = [-5,1,5,0,-7]

# Initialize variables
num = 0  # Current cumulative altitude
max_hig = 0  # Tracks the highest altitude encountered

# Process each altitude change in the gain array
for i in gain:
	num += i  # Update current altitude by applying this segment's change
    max_hig = max(max_hig, num)  # Update maximum if current is higher	

# Output the highest altitude
print(max_hig)

# Time Complexity: O(n) - Single pass through gain array (n elements)
# Space Complexity: O(1) - Uses constant extra space (2 variables)