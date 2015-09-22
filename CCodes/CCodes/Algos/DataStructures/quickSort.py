#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    def quickStart(self, list, start, end):
        if start >= end:
            return

        pivot = list[end]
        i=start
        j=end-1

        while i <= j:
            while i < end and list[i] <= pivot:
                i += 1

            while j>=0 and list[j] > pivot:
                j -= 1

            if i < j:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


        # put pivot at right place
        temp = list[i]
        list[i] = pivot
        list[end] = temp

        self.quickStart(list, start, i-1)
        self.quickStart(list, i+1, end)

        return list






if __name__ == '__main__':
    s = Solution()
    print(s.quickStart([9,10], 0, 1))
    print(s.quickStart([10,9], 0, 1))
    print(s.quickStart([11,9,10], 0, 2))
    a = [1,23,34,0,19,410,123,-9,923,939,29,84,2]
    print(s.quickStart(a, 0, len(a)-1))
