import sys


class BinarySearch:
    @staticmethod 
    def findExact(list, k):
        n = len(list)

        start = 0
        end = n-1

        

        while start <= end:
            mid = start + (end - start)//2

            if list[mid] == k:
                return mid

            elif list[mid] > k:
                end = mid - 1

            elif list[mid] < k:
                start = mid + 1


        return -1
    @staticmethod
    def findFirstYes(list, k):
        # predicate: first number which is greater than or equal to k
        
        n = len(list)

        start = 0
        end = n-1

        while start < end:
            mid = start + (end - start)//2

            if list[mid] >= k:
                end = mid

            else:
                start = mid + 1

        if list[end] >= k:
            return end
        return -1


    @staticmethod
    def findLastNo(list, k):
        # predicate: biggest number which is <= k

        n = len(list)
        start = 0
        end = n - 1

        while start < end:
            mid = start + (end - start + 1)//2

            if list[mid] <= k:
                start = mid

            else:
                end = mid - 1

        if list[start] <= k:
            return start
        
        return -1




     




if __name__ == '__main__':

    c = BinarySearch()
    l = [1,2,3,4,5,6,7,10,111,300,1111]
    #l = [1,4]
    print(c.findLastNo(l, 4))
    print(c.findLastNo(l, 1110))
    print(c.findLastNo(l, 2000))
    print(c.findLastNo(l, 0))
    print(c.findLastNo(l, 11))
    print(c.findLastNo(l, 1.5))


