from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        output = []
        if root is None:
            return ''

        queue = deque()
        queue.append(root)

        while len(queue):
            n = queue.popleft()
            if n is None:
                output.append('#')
                continue
            
            output.append(str(n.val))
            queue.append(n.left)
            queue.append(n.right)

        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')

        root = None

        if nodes[0] == '':
            return root

        root = TreeNode(int(nodes[0]))

        temp = [root]

        i = 1

        while i < len(nodes):
            j = 0
            temp2 = []
            while j < len(temp):
                # full serialization, will have enough nodes
                left = nodes[i]
                right = nodes[i+1]

                if left != '#':
                    n = TreeNode(int(left))
                    temp[j].left = n
                    temp2.append(n)

                if right != '#':
                    n = TreeNode(int(right))
                    temp[j].right = n
                    temp2.append(n)

                j += 1
                i += 2

            temp = temp2

        return root







# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    t = None
    s = Codec()
    s.deserialize(s.serialize(t))

