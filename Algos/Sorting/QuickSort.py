l = [10, 12, 3, 4, 56, 7, 0, 8, 9, 11, 12]
l = [0, 1, 2, 3, 4, 5, -1]


class QuickSort():
    def __init__(self, listToSort):
        self.listToSort = listToSort

    def __str__(self):
        return str(self.listToSort)

    def quickSort(self, left, right):
        """

        :rtype : object
        """
        if left < right:

            pivotIdx = int(left + ((right - left) / 2))
            pivotNewIdx = pivotIdx
            i = left
            j = right
            pivot = self.listToSort[pivotIdx]
            while (i < j):
                while (self.listToSort[i] <= pivot and i < right):
                    i = i + 1
                while (self.listToSort[j] > pivot):
                    j = j - 1
                if (i < j):
                    if (i == pivotIdx):
                        pivotNewIdx = j
                    elif (j == pivotIdx):
                        pivotNewIdx = i

                    temp = self.listToSort[i]
                    self.listToSort[i] = self.listToSort[j]
                    self.listToSort[j] = temp
            temp = self.listToSort[pivotNewIdx]
            self.listToSort[pivotNewIdx] = self.listToSort[j]
            self.listToSort[j] = temp
            self.quickSort(left, j - 1)
            self.quickSort(j + 1, right)

    def testQuickSort(self, left, right):
        i = left
        j = right
        pivot = self.listToSort[int(left + (right - left) / 2)]
        while (i <= j):
            while (self.listToSort[i] < pivot):
                i = i + 1
            while (self.listToSort[j] > pivot):
                j = j - 1
            if (i <= j):
                tmp = self.listToSort[j]
                self.listToSort[j] = self.listToSort[i]
                self.listToSort[i] = tmp
                i = i + 1
                j = j - 1
        if (i < right):
            self.testQuickSort(left, i)
        if (j > left):
            self.testQuickSort(j, right)


q = QuickSort(l)
q.testQuickSort(0, len(l) - 1)
print(q.listToSort)
print(QuickSort.quickSort.__doc__)