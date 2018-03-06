
class BSTNode:
    def __init__(self, val, leftCount):
        self.val = val
        self.leftCount = leftCount
        self.left = None
        self.right = None



class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        if n == 0:
            return []
        result = [0] * n

        root = BSTNode(nums[-1], 0)

        for i in range(n-2, -1, -1):
            result[i] = Solution.addBst(root, nums[i], 0)

        return result


    @staticmethod
    def addBst(node, val, total):
        if node is None:
            raise ValueError('invalid node')

        if node.val < val:
            if node.right:
                # add one for all smaller childer and and 1 for self
                return Solution.addBst(node.right, val, node.leftCount + 1 + total)
                # no need to update anything
            else:
                node.right = BSTNode(val, 0)
                return node.leftCount + 1 + total

        elif node.val >= val:
            if node.left:
                rslt = Solution.addBst(node.left, val, total)
                node.leftCount += 1
                return rslt
            else:
                node.left = BSTNode(val, 0)
                node.leftCount += 1
                return total


if __name__ == '__main__':
    c = Solution()
    print(c.countSmaller([5,2,6,1]))