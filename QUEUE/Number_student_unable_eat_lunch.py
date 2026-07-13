'''
1700. Number of Students Unable to Eat Lunch

The cafeteria provides two types of sandwiches:

0 -> Circular
1 -> Square

Students stand in a queue.

If the front student's preference matches
the top sandwich,
the student takes the sandwich and leaves.

Otherwise,
the student moves to the end of the queue.

Return the number of students
who are unable to eat.

Example 1:

Input:
students = [1,1,0,0]
sandwiches = [0,1,0,1]

Output:
0

Example 2:

Input:
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

Output:
3
'''

# solution

from collections import deque


def main():

    # Students preference list
    students = [1,1,1,0,0,1]

    # Sandwich stack
    sandwiches = [1,0,0,0,1,1]

    # Convert students into queue
    stuq = deque(students)

    # Convert sandwiches into queue
    swque = deque(sandwiches)

    # Count students who rejected current sandwich
    r = 0

    # Store total waiting students
    wating = len(stuq)

    # Continue while students and sandwiches exist
    # and not all students reject current sandwich
    while stuq and swque and r < wating:

        # If student does not want current sandwich
        if stuq[0] != swque[0]:

            # Remove student from front
            p = stuq.popleft()

            # Move student to end of queue
            stuq.append(p)

            # Increase rejection count
            r += 1

        # If student wants current sandwich
        else:

            # Student leaves queue
            stuq.popleft()

            # Sandwich is taken
            swque.popleft()

            # Reset rejection count
            r = 0

            # Update remaining waiting students
            wating = len(stuq)

    # Print students unable to eat
    print(len(stuq))


# Main function execution
if __name__ == "__main__":
    main()

# Time Complexity: O(n²)
# Space Complexity: O(n)

'''
Theory Explanation:

1. This problem uses Queue Simulation.

2. Students behave like a queue:

   -> Front student is checked.
   -> If sandwich does not match,
      student moves to the back.

3. Sandwiches are processed
   from the front.

4. If student preference matches
   the current sandwich:

   -> Remove student.
   -> Remove sandwich.
   -> Reset rejection count.

5. If preference does not match:

   -> Move student to queue end.
   -> Increase rejection count.

6. r stores how many students
   rejected the current sandwich.

7. wating stores the number
   of students currently in queue.

8. If:

   r == wating

   it means every remaining student
   has rejected the current sandwich.

9. Therefore,
   no student can eat the current sandwich
   and the process must stop.

Important Steps:

-> Students rotate in the queue.
-> Sandwich changes only after a match.
-> Reset r after a sandwich is taken.
-> Update wating after a student leaves.
-> Stop when all remaining students reject
   the same sandwich.

Key Intuition:

If every student in the queue
has seen the current sandwich once
and nobody takes it,
then rotating the queue again
will never change the result.

Pattern:

Queue Simulation
+
Full Rotation Detection
=
Unable to Eat Students
'''