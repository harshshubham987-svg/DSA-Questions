'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

The absolute value represents size,
and the sign represents direction:
+ve → moving right
-ve → moving left

If two asteroids collide:
-> Smaller one explodes
-> If same size, both explode

Return final state after all collisions.
'''

# Solution:

def collision(arr):

    # Stack to store surviving asteroids
    stack = []

    # Traverse each asteroid
    for i in arr:

        # Collision happens only when:
        # top of stack is moving right (+)
        # current asteroid is moving left (-)
        while stack and stack[-1] > 0 and i < 0:
    
            # If current asteroid is bigger
            if stack[-1] < abs(i):
                
                # Destroy top asteroid
                stack.pop()

                # Continue checking with next top
                continue
            
            # If both are same size
            elif stack[-1] == abs(i):
                
                # Destroy both
                stack.pop()
                break
            
            # If stack top is bigger
            else:
                
                # Current asteroid gets destroyed
                break
        
        else:
            # No collision, push current asteroid
            stack.append(i)

    # Return final surviving asteroids
    return stack


def main():
    # Input array
    asteroids = [3,5,-6,2,-1,4]

    # Print final result
    print(collision(asteroids))


# Main function execution
main()

# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Stack.

2. Why Stack?
   Because collisions only happen with the most recent asteroid.

3. Collision condition:
   stack top > 0
   current asteroid < 0

   Means:
   One is moving right
   and other is moving left.

4. Cases:

Case 1:
Top smaller than current
-> Top explodes

Case 2:
Both equal
-> Both explode

Case 3:
Top bigger
-> Current explodes

5. If no collision:
   Add asteroid into stack.

Important Steps:

-> Collision only when opposite directions meet.
-> Same direction never collides.
-> Use abs() for size comparison.
-> while loop handles chain collisions.

Key Intuition:

Always compare with the latest alive asteroid,
because that's the first possible collision.
'''