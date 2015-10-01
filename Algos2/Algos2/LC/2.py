

class Solution(object):
    def addTwoNumbers(self, list1, list2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        temp1 = list1
        temp2 = list2
        newHead = None
        newTail = None


        carry = 0

        while temp1 and temp2:
            s = temp1.val + temp2.val + carry

            if s > 9:
                carry = 1
                s %= 10
        
            else:
                carry = 0

            node = ListNode(s)

            if newTail:
                newTail.next = node
                newTail = node

            else:
                newTail = node
                newHead = node
        
            temp1 = temp1.next
            temp2 = temp2.next


        if temp1:
            temp = temp1
        elif temp2:
            temp = temp2
        else:
            temp = None


        while temp:
            s = temp.val + carry

            if s > 9:
                carry = 1
                s %= 10

            else:
                carry = 0

            node = ListNode(s)

            if newTail:
                newTail.next = node
                newTail = node

            else:
                newTail = node
                newHead = node
           
            temp = temp.next


        if carry > 0:
            node = ListNode(carry)
            newTail.next = node
            newTail = node

            
        return newHead