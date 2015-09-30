import sys

class QuickSort:
    @staticmethod
    def partition(listToSort, start, end):
        pivot = listToSort[end]

        i = start
        j = end-1

        while i <= j:
            if listToSort[i] <= pivot:
                i += 1
            elif listToSort[j] <= pivot:
                # swap i and j
                temp = listToSort[i]
                listToSort[i] = listToSort[j]
                listToSort[j] = temp
                i += 1
                j -= 1
            else:
                j -= 1

        # swap i with pivot
        temp = listToSort[i]
        listToSort[i] = pivot
        listToSort[end] = temp
        return i
        

    @staticmethod
    def _quickSort(listToSort, start, end):
        # start, end inclusive
        if start < end:
            mid = QuickSort.partition(listToSort, start, end)
            
            QuickSort._quickSort(listToSort, start, mid-1)
            QuickSort._quickSort(listToSort, mid + 1, end)


    @staticmethod
    def quickSort(listToSort):
        print(listToSort)
        QuickSort._quickSort(listToSort, 0, len(listToSort)-1)
        print(listToSort)

if __name__ == '__main__':
    c = QuickSort()

    c.quickSort([129,24,13,560,12,40,10,1,2,0])
    c.quickSort([1,0])
    c.quickSort([1])
    c.quickSort([1,2,3,4])
    c.quickSort([0,1])
    c.quickSort([4,3,2,1])
    c.quickSort([0,1,2])
    c.quickSort([2,1,0])


