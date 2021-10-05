# Unfinished

# References: 

# https://www.cpp.edu/~ftang/courses/CS241/notes/graph.htm
# https://www.tutorialspoint.com/definition-and-properties-of-trees

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("len_prerequisites =",len(prerequisites)," numCourses =",numCourses)
        # Case tree has too many connections
        if len(prerequisites) > (numCourses - 1):
            return False
        else:
            return True
