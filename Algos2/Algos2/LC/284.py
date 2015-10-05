# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peekedObj = None
        self.isPeekedObjValid = False
        self.iterator = iterator

   
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.isPeekedObjValid:
            return self.peekedObj

        else:
            self.isPeekedObjValid = True
            self.peekedObj = self.iterator.next()
            return self.peekedObj


            

        

    def next(self):
        """
        :rtype: int
        """
        
        if self.isPeekedObjValid:
            self.isPeekedObjValid = False
            return self.peekedObj

        else:
            return self.iterator.next()




    def hasNext(self):
        """
        :rtype: bool
        """

        if self.isPeekedObjValid:
            return True

        return self.iterator.hasNext()


        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].