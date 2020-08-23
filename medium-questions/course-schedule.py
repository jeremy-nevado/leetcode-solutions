'''
numCourses: int
prerequisites: List[List[int]]
This program returns a boolean that states whether or not
you can complete all courses
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        classes = {}
        for pair in prerequisites:
            course = pair[1]
            prereq = pair[0] 
            if course in classes.keys():
               classes[course].append(prereq)
            else:
                classes[course] = [prereq]
        for course in classes.keys():
            for prereq in classes[course]:
                if prereq in classes.keys():
                    if course in classes[prereq]:
                        return False
                    for secondary in classes[prereq]:
                        if secondary in classes.keys():
                            if course in classes[secondary]:
                                return False
        return True

