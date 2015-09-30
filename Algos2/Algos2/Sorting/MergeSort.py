import sys


class MergeSort:
    @staticmethod

    def _mergeSortBottomUpMerge(listToSort, start, mid, end):

        # merge runs


        tempList = []

        i =  start
        j = mid+1
        k = 0
        while i <= mid and j <= end:
            if listToSort[i] <= listToSort[j]:
                tempList.append(listToSort[i])
                i += 1
            else:
                tempList.append(listToSort[j])
                j += 1

        while i <= mid:
            tempList.append(listToSort[i])
            i += 1
        while j <= end:
            tempList.append(listToSort[j])
            j += 1

        listToSort[start:end+1] = tempList
    
    @staticmethod
    def mergeSortBottomUp(listToSort):

        n = len(listToSort)
        print(listToSort)

        step = 1
        while step < n:
            start = 0
            while start < n:

                if start + 2 * step - 1 < n:
                    # we have two complete runs to merge
                    MergeSort._mergeSortBottomUpMerge(listToSort, start, start + step - 1, start+2*step -1)
                else:
                    MergeSort._mergeSortBottomUpMerge(listToSort, start, min(start + step - 1, n-1), n-1)

                start += 2 * step
            step *= 2


        print(listToSort)




    @staticmethod
    def _mergeSort(listToSort, start, end):
        
        # start,mid are inclusive
        if end - start == 0:
            return
        if end - start == 1:

            if listToSort[start] <= listToSort[end]:
                return
            else:
                temp = listToSort[end]
                listToSort[end] = listToSort[start]
                listToSort[start] = temp
                return

        mid = start + (end - start) // 2

        # sort parts
        MergeSort._mergeSort(listToSort, start, mid)
        MergeSort._mergeSort(listToSort, mid+1, end)

        # merge runs


        tempList = []

        i =  start
        j = mid+1
        k = 0
        while i <= mid and j <= end:
            if listToSort[i] <= listToSort[j]:
                tempList.append(listToSort[i])
                i += 1
            else:
                tempList.append(listToSort[j])
                j += 1

        while i <= mid:
            tempList.append(listToSort[i])
            i += 1
        while j <= end:
            tempList.append(listToSort[j])
            j += 1

        listToSort[start:end+1] = tempList





            
    @staticmethod
    def mergeSort(listToSort):
        print(listToSort)
        n = len(listToSort)
        MergeSort._mergeSort(listToSort, 0, n-1)

        print(listToSort)
        return listToSort


if __name__ == '__main__':
    c = MergeSort()
    c.mergeSort([129,24,13,560,12,40,10,1,2,0])
    c.mergeSort([1,0])
    c.mergeSort([1])
    c.mergeSort([1,2,3,4])
    c.mergeSort([0,1])
    c.mergeSort([4,3,2,1])
    c.mergeSort([0,1,2])
    c.mergeSort([2,1,0])


    c.mergeSortBottomUp([129,24,13,560,12,40,10,1,2,0])
    c.mergeSortBottomUp([1,0])
    c.mergeSortBottomUp([1])
    c.mergeSortBottomUp([1,2,3,4])
    c.mergeSortBottomUp([0,1])
    c.mergeSortBottomUp([4,3,2,1])
    c.mergeSortBottomUp([0,1,2])
    c.mergeSortBottomUp([2,1,0])
        

