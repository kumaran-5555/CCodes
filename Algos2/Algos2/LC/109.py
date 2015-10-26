# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _buildTree(self, list):

        if list is None:
            return None

        root = None

        slow = list
        fast = list
        prev = None

        while fast and fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow points root
        # prev points end of left
        # slow.next point start of right

        if prev:

            prev.next = None
            left = list

        else:
            left = None


        right = slow.next

        slow.next = None

        root = TreeNode(slow.val)

        root.left = self._buildTree(self, left)
        root.right = self._buildTree(self, right)


        return root






        

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        return self._buildTree(head)

