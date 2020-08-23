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
        
