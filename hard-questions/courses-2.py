class Solution:
    def minNumberOfSemesters(self, n, dependencies, k) -> int:
        dict = {}
        doable_courses = []
        completed_courses = []
        sems = 0
        prerequisites = []
        priority = {}
        running = True
   
        # Create a dictionary of requirements
        for dpc in dependencies:
            if dpc[1] in dict.keys():
                dict[dpc[1]].append(dpc[0])
            else:
                dict[dpc[1]] = [dpc[0]]
                
        # Print statement for testing
        print(dict)

        def depthFinder(head_course, courses_seen):
          courses_seen.append(head_course)
          depth = 1
          for prereq in dict[head_course]:
            if prereq in dict.keys():
              new_depth, courses_seen = depthFinder(prereq, courses_seen)
              depth += new_depth
            else:
              courses_seen.append(prereq)
          return depth, courses_seen
        
        for key in dict.keys():
          new_depth, child_courses = depthFinder(key, [])
          for item in child_courses:
            if new_depth in priority.keys():
              priority[new_depth].append(item)
            else:
              priority[new_depth] = [item]
        print(priority)
        
        # Create a priority list to tell which elements have highest priority
        for prereqs in dict.values():
            prerequisites = prerequisites + prereqs
            
        # Base case for when all courses have no prerequisites
        if not dict.keys():
            if n % 2:
                return n // 2 + 1
            else:
                return n // 2
        
        '''
        A loop that iterates until all keys are removed.
        It starts by finding all courses that have no prerequisites.
        One loop iteration represents one semester.
        Each semester the most priorty courses are completed.
        At the end of the semester the completed prerequisites are updated.
        New potential courses are added to the list after each semester.
        This loop breaks when all "prerequisite courses" are completed
        '''
        while dict.keys():
            temp = []
            for i in range(1, n+1):
                if i not in dict.keys() and i not in completed_courses:
                    doable_courses.append(i)
                    completed_courses.append(i)
            print(doable_courses)
            if len(doable_courses) >= k:
                j = 0
                for step in range(max(priority), 0, -1):
                  for i in doable_courses:
                    if i in priority[step]:
                      j += 1
                      for prereqs in dict.values():
                        if i in prereqs:
                          prereqs.remove(i)
                      doable_courses.remove(i)
                    if j == k: break
                # for i in doable_courses:
                #   # if i in prerequisites:
                #   #     j += 1
                #   #     for prereqs in dict.values():
                #   #         if i in prereqs:
                #   #             prereqs.remove(i)
                #   #     doable_courses.remove(i)
                #   if j == k: break
                # for i in range(0, k - j):
                #     for prereqs in dict.values():
                #         if doable_courses[i] in prereqs:
                #             prereqs.remove(doable_courses[i])
                # doable_courses = doable_courses[k-j:]
                sems += 1
            else:
                for i in doable_courses:
                    for prereqs in dict.values():
                        if i in prereqs:
                            prereqs.remove(i)
                doable_courses = []
                sems += 1
            for key in dict.keys():
                if not dict[key]:
                    temp.append(key)
            for item in temp:
                dict.pop(item)
            if not dict.keys():
                doable_courses = doable_courses + temp

        '''
        This loop continues to check if there are courses that need doing.
        Each loop iteration represents a semester.
        Simply completes all remaining courses based on possible courseloads.
        '''
        if doable_courses:
            while doable_courses:
                if len(doable_courses) >= k:
                    j = 0
                    sems += 1
                    doable_courses = doable_courses[k:]
                else:
                    doable_courses = []
                    sems += 1
                if not doable_courses:
                    return sems
        
        # Returns +1 to account for missed iteration. To Be Fixed
        return sems + 1

sol = Solution()
print(sol.minNumberOfSemesters(12, [[1,2],[1,3],[7,5],[7,6],[4,8],[8,9],[9,10],[10,11],[11,12]], 2))

            