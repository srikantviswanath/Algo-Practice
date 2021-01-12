import heapq


class MedianOfAStream(object):
    """
    Design a class to calculate the median of a number stream. The class should have the following two methods:

    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class
    If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
    """
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    @property
    def minlen(self):
        return len(self.minheap)

    @property
    def maxlen(self):
        return len(self.maxheap)

    @property
    def max_of_max_heap(self):
        return -self.maxheap[0]

    @property
    def min_of_min_heap(self):
        return self.minheap[0]

    def _re_balance(self):
        if self.minlen - self.maxlen > 1:
            min_popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -min_popped)
        elif self.maxlen - self.minlen > 1:
            max_popped = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -max_popped)

    def insert_num(self, num):
        if not self.maxheap:
            heapq.heappush(self.maxheap, -num)
        elif num <= self.max_of_max_heap:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        self._re_balance()

    def find_median(self):
        if self.maxlen > self.minlen:
            return -self.max_of_max_heap
        elif self.minlen > self.maxlen:
            return self.min_of_min_heap
        else:
            return (self.max_of_max_heap + self.min_of_min_heap) / 2


if __name__ == '__main__':
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(8)
    medianOfAStream.insert_num(7)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(6)
    medianOfAStream.insert_num(5)
    medianOfAStream.insert_num(5)
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(2)
    medianOfAStream.insert_num(-1)
    print("The median is: " + str(medianOfAStream.find_median()))
