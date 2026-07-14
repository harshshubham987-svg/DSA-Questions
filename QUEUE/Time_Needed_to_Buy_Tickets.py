'''
2073. Time Needed to Buy Tickets

There are n people standing in a queue
to buy tickets.

Each person can buy only one ticket
at a time.

Buying one ticket takes exactly 1 second.

If a person still needs more tickets,
they move to the end of the queue.

If a person finishes buying tickets,
they leave the queue.

Return the time taken by the person
at index k to finish buying all tickets.

Example 1:

Input:
tickets = [2,3,2]
k = 2

Output:
6

Example 2:

Input:
tickets = [5,1,1,1]
k = 0

Output:
8
'''

from collections import deque


def main():

    # Tickets required by each person
    tickets = [5,1,1,1]

    # Target person's original index
    k = 0

    # Queue stores person index and remaining tickets
    ticque = deque()

    # Store total time
    time = 0

    # Add every person into the queue
    for i, tic in enumerate(tickets):

        # Store original index and ticket count
        ticque.append((i, tic))

    # Process people in queue
    while ticque:

        # Remove front person from queue
        i, rem = ticque.popleft()

        # Person buys one ticket
        rem -= 1

        # Buying one ticket takes one second
        time += 1

        # Check if target person finished buying tickets
        if i == k and rem == 0:
            break

        else:

            # If person still needs tickets
            if rem > 0:

                # Move person to end of queue
                ticque.append((i, rem))

    # Print total time
    print(time)


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(total number of tickets bought until person k finishes)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Queue Simulation.

2. Every person is stored as:

   (index, remaining_tickets)

Example:

tickets = [5,1,1,1]

Queue:

[(0,5), (1,1), (2,1), (3,1)]

3. Remove the front person.

4. The person buys one ticket:

   remaining_tickets -= 1

5. Increase time by 1
   because one ticket takes one second.

6. If the current person is k
   and remaining tickets become 0:

   The target person has finished.

   Stop the simulation.

7. Otherwise,
   if the person still needs tickets:

   Add the person back
   to the end of the queue.

Example Dry Run:

tickets = [5,1,1,1]
k = 0

Initial Queue:

[(0,5), (1,1), (2,1), (3,1)]


Person 0 buys:

time = 1

Queue:

[(1,1), (2,1), (3,1), (0,4)]


Person 1 buys:

time = 2

Person 1 leaves.

Queue:

[(2,1), (3,1), (0,4)]


Person 2 buys:

time = 3

Person 2 leaves.

Queue:

[(3,1), (0,4)]


Person 3 buys:

time = 4

Person 3 leaves.

Queue:

[(0,4)]


Person 0 buys four more tickets:

time = 8

Person 0 finishes.

Answer:

8

Important Steps:

-> Store original index with ticket count.
-> Remove person from front.
-> Decrease ticket count by 1.
-> Increase time by 1.
-> Move unfinished person to queue end.
-> Stop exactly when person k finishes.

Key Intuition:

Simulate the ticket queue exactly.

Every queue operation represents
one person buying one ticket.

Pattern:

Queue Simulation
+
Remaining Work Tracking
=
Time Needed to Buy Tickets
'''