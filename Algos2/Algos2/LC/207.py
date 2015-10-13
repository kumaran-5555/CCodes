from collections import defaultdict

class Solution(object):

    def dfsCycleDetectionDirected(self, node):

        # start exploring node
        self.colors[node] = 'Gray'

        if node not in self.edges:
            # no neighbours, done exploring
            self.colors[node] = 'Black'
            return

        for e in self.edges[node]:
            if self.colors[e] == 'White':
                self.dfsCycleDetectionDirected(e)
            elif self.colors[e] == 'Gray':
                # back edge
                self.hasCycle = True

        # done exploring
        self.colors[node] = 'Black'

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        self.hasCycle = False

        self.colors = {}
        self.edges = defaultdict(list)

        for i in range(numCourses):
            self.colors[i] = 'White'

        for i in prerequisites:
            self.edges[i[0]].append(i[1])

        for i in range(numCourses):
            self.dfsCycleDetectionDirected(i)
            if self.hasCycle:
                return False

        return True






if __name__ == '__main__':
    s = Solution()
    s.canFinish(7, [])

