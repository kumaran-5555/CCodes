from collections import defaultdict

class Solution(object):

    def topologicalOrder(self, node):
        # returns if graph has cycle

        self.colors[node] = 'G'


        if node not in self.edges:
            # no neighbours
            self.o.append(node)
            self.colors[node] = 'B'
            
            return False

        for e in self.edges[node]:
            if self.colors[e] == 'G':
                self.hasCycle = True
                return True
            if self.colors[e] == 'W':
                self.topologicalOrder(e)

        self.colors[node] = 'B'
        self.o.append(node)
        return False
       
               



    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.o = []
        self.hasCycle = False

        self.colors = {}
        self.edges = defaultdict(list)

        for i in range(numCourses):
            self.colors[i] = 'W'

        for i in prerequisites:
            self.edges[i[1]].append(i[0])

        for i in range(numCourses):
            if self.colors[i] != 'W':
                continue

            self.topologicalOrder(i)
            if self.hasCycle:
                return []

  
        self.o = self.o[::-1]

        return self.o



if __name__ == '__main__':
    s = Solution()
    s.findOrder(2, [[1,0]])

