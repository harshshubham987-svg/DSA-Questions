"""207. Course Schedule
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
# Solution
from collections import deque

def main():
    numCourse = 2
    prerequ = [[1,0]]

    graph = {}
    indegree = {}
    complete = 0

    for i in range(numCourse):
        graph[i] = []
        indegree[i] = 0
    
    for pair in prerequ:
        u = pair[1]
        v = pair[0]

        graph[u].append(v)
        indegree[v] += 1

    q = deque()

    for deg in indegree:
        if indegree[deg] == 0:
            q.append(deg)
    
    if not q:
        return False
    
    while q:
        
        nod = q.popleft()
        complete += 1
    
        
        for nei in (graph[nod]):
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    if complete == numCourse:
        
        return True

    return False 
    

if __name__ == "__main__":
    print(main())