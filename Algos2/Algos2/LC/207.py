from collections import defaultdict


class Solution(object):

    def dfsCycleDetection(self, node):
        flags = {}

        stack = []

        if node not in self.edges:
            # don't have any edges, can't have cycle
            return False

        stack.append(node)

        while len(stack):
            n = stack.pop()

            for e in self.edges[n]:                
                if e in flags:
                    return True

                stack.append(e)
                flags[e] = 1


        return False

    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        self.edges = defaultdict(list)

        for i in range(numCourses):
            self.edges[i] = []
        for i in prerequisites:
            self.edges[i[0]].append(i[1])


        for e in self.edges:
            if self.dfsCycleDetection(e):
                # cycle found
                return False

        return True




