class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry >= 10:
                carry = 1
                digits[i] = (digits[i] + carry) % 10
            else:
                digits[i] += 1
                carry = 0
                break


        if carry == 1:
            return [1] + digits

        return digits




