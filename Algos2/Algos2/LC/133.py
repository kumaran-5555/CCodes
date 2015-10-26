# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """

        if node is None:
            return None

        
        visited = {}
        labelToNodeMapping = {}
        labelToNewNodes = {}


        stack = []

        stack.append(node)

        root = node

        while len(stack):

            node = stack.pop()

            if node.label in visited:
                # we have already visited this node
                continue

            labelToNodeMapping[node.label] = node

            visited[node.label] = True

            for n in node.neighbors:
                if n.label in visited:
                    continue
                stack.append(n)


        for l in labelToNodeMapping:
            labelToNewNodes[l] = UndirectedGraphNode(l)


        for l in labelToNodeMapping:
            oldNode = labelToNodeMapping[l]
            newNode = labelToNewNodes[l]

            for n in oldNode.neighbors:
                newNode.neighbors.append(labelToNewNodes[n.label])


        return labelToNewNodes[root.label]



