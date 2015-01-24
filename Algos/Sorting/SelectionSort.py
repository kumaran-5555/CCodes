__author__ = 'serajago'
l = [10, 12, 3, 4, 56, 7, 0, 8, 9, 11, 12]


class SelectionSort():
    def __init__(self, listToSort):
        self.listToSort = listToSort

    def __str__(self):
        return str(self.listToSort)

    def selectionSort(self, left, right):
        """

        :rtype : object
        """
        for i in range(0, len(self.listToSort) - 1):
            minVal = self.listToSort[i]
            minIdx = i
            for j in range(i + 1, len(self.listToSort) - 1):
                if self.listToSort[j] < minVal:
                    minIdx = j
                    minVal = self.listToSort[j]
            temp = self.listToSort[i]
            self.listToSort[i] = self.listToSort[minIdx]
            self.listToSort[minIdx] = temp


q = SelectionSort(l)
print(q)
q.selectionSort(0, len(l) - 1)
print(q)


# print(SelectionSort.quickSort.__doc__)