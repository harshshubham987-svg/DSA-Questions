'''
933. Number of Recent Calls

You have a RecentCounter class which counts
the number of recent requests within
the past 3000 milliseconds.

For every ping(t),
return the number of requests
inside the inclusive range:

[t - 3000, t]

Example:

Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

Output:
[null, 1, 2, 3, 3]
'''

# solution

class RecentCounter(object):

    def __init__(self):

        # Queue stores request times
        self.q = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        # Add current request time into queue
        self.q.append(t)

        # Calculate oldest valid request time
        old = t - 3000

        # Remove requests older than valid range
        while self.q[0] < old:
            self.q.popleft()

        # Return total valid recent requests
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Time Complexity: O(1) Amortized per ping()
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Queue / Deque.

2. Every ping(t) represents
   a new request at time t.

3. We need to keep only requests
   inside the range:

   [t - 3000, t]

4. First:
   Add current request time
   into the queue.

5. Calculate:

   old = t - 3000

6. Any request smaller than old
   is outside the valid range.

7. Remove old requests
   from the front of the queue.

8. After removing invalid requests,
   every time remaining in the queue
   belongs to the valid range.

9. Queue length gives
   the total number of recent requests.

Example Dry Run:

ping(1)

Queue:
[1]

Range:
[-2999, 1]

1 is valid.

Return:
1


ping(100)

Queue:
[1, 100]

Range:
[-2900, 100]

Both requests are valid.

Return:
2


ping(3001)

Queue:
[1, 100, 3001]

Range:
[1, 3001]

All requests are valid.

Return:
3


ping(3002)

Queue before removing:
[1, 100, 3001, 3002]

Range:
[2, 3002]

1 < 2

Remove 1.

Queue:
[100, 3001, 3002]

Return:
3

Important Steps:

-> Add current request first.
-> Calculate t - 3000.
-> Remove requests smaller than t - 3000.
-> Use popleft() to remove oldest requests.
-> Return queue length.

Key Intuition:

The queue stores only requests
from the last 3000 milliseconds.

Old requests leave from the front,
and new requests enter from the back.

Pattern:

Queue
+
Sliding Time Window
=
Recent Counter
'''
