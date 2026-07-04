'''155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

class MinStack(object):

    def __init__(self):

        # Main stack to store all values
        self.main = []

        # Stack to store minimum values
        self.min = []        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """

        # Push value into main stack
        self.main.append(value)

        # Push into min stack if it is the first element
        # or smaller than/equal to current minimum
        if not self.min or value <= self.min[-1]:
            self.min.append(value)    

    def pop(self):
        """
        :rtype: None
        """

        # Remove top element from main stack
        x = self.main.pop()

        # If removed element is current minimum,
        # remove it from min stack as well
        if x == self.min[-1]:
            self.min.pop()       

    def top(self):
        """
        :rtype: int
        """

        # Return top element of main stack
        return self.main[-1]
        

    def getMin(self):
        """
        :rtype: int
        """

        # Return current minimum element
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time Complexity:
# push()   -> O(1)
# pop()    -> O(1)
# top()    -> O(1)
# getMin() -> O(1)

# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Two Stacks.

2. Main Stack:
   Stores all elements.

3. Min Stack:
   Stores only the minimum elements.

4. While pushing:
   -> Push into main stack.
   -> Push into min stack only if:
      value <= current minimum.

5. While popping:
   -> Remove from main stack.
   -> If removed value is the minimum,
      remove it from min stack also.

6. top():
   Returns last element of main stack.

7. getMin():
   Returns last element of min stack.

Important Steps:

-> Maintain two separate stacks.
-> Min stack always keeps current minimum.
-> Duplicate minimum values should also be stored.
-> Every operation works in O(1).

Key Intuition:

Main stack stores data,
Min stack stores the history of minimum values,
so minimum is always available at the top.
'''