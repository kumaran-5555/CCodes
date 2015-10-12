
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


        
class Solution(object):

    def reverseList(self, node):

        head = None

        temp = node
        while temp:
            next = temp.next
            if head is None:
                head = temp
                head.next = None
            else:
                temp.next = head
                head = temp
                
            temp = next

        return head


                


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = head
        slow = head

        if head is None:
            return True


        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = self.reverseList(slow)



        h1 = head
        h2 = l2

        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next


        return True



if __name__ == '__main__':

    l = Node(1)
    l.next = Node(0)
    l.next.next = Node(1)

    s = Solution()
    s.isPalindrome(l)



