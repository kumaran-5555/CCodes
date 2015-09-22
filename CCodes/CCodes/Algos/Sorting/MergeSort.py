__author__ = 'serajago'
l = [12, 10, 3, 4, 56, 7, 0, 8, 9, 11, 12]
# l = [0, 1, 2, 3, 4, 5, -1]


class MergeSort():
    def __init__(self, listToSort):
        self.listToSort = listToSort
        self.tempList = []
        for i in listToSort:
            self.tempList.append("")

    def __str__(self):
        return str(self.listToSort)

    def merge(self, left, leftEnd, rightStart, right):
        print(left, leftEnd, rightStart, right)

        cursor = left
        leftCursor = left
        rigtCursor = rightStart

        while cursor <= right:
            if rigtCursor > right:
                self.tempList[cursor] = self.listToSort[leftCursor]
                leftCursor += 1
                cursor += 1
            elif leftCursor > leftEnd:
                self.tempList[cursor] = self.listToSort[rigtCursor]
                rigtCursor += 1
                cursor += 1
            elif self.listToSort[leftCursor] <= self.listToSort[rigtCursor]:
                self.tempList[cursor] = self.listToSort[leftCursor]
                cursor += 1
                leftCursor += 1
            elif self.listToSort[leftCursor] > self.listToSort[rigtCursor]:
                self.tempList[cursor] = self.listToSort[rigtCursor]
                cursor += 1
                rigtCursor += 1
        for i in range(left, right+1):
            self.listToSort[i] = self.tempList[i]
        print(self.tempList)

    def mergeSort(self, left, right):
        """

        :rtype : object
        """

        pivot = left + int((right - left) / 2)

        if left < right:
            self.mergeSort(left, pivot)
            self.mergeSort(pivot + 1, right)
            self.merge(left, pivot, pivot + 1, right)


q = MergeSort(l)

q.mergeSort(0, len(l) - 1)

print(q.tempList)

