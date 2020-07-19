from math import ceil


class Heap(object):  # implementing a min heap for now. Will extend this to max heap later
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return str(self)

    @property
    def length(self):
        return len(self.array)

    def _left_child(self, index):
        child = index * 2 + 1
        return (child, self.array[child]) if child < self.length else (None, float('inf'))

    def _right_child(self, index):
        child = index * 2 + 2
        return (child, self.array[child]) if child < self.length else (None, float('inf'))

    def _parent(self, index):
        if index >= len(self.array):
            raise IndexError('No parent :(')
        if index == 0:
            return index, self.array[index]
        parent = ceil(index / 2 - 1)
        return parent, self.array[parent]

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def sink(self, index: int):
        """sink does the magic of heapifying in O(N) since the nodes that have to sink is far
        less than the ones that have to bubble. This is because the tree is a complete tree implying that
        about half the nodes are at the last level"""
        curr = index
        while True:
            left_child_index, left_child_value = self._left_child(curr)
            right_child_index, right_child_value = self._right_child(curr)
            min_child_index, min_child_value = min((left_child_index, left_child_value), (right_child_index, right_child_value), key=lambda tup: tup[1])
            if min_child_index is not None and self.array[curr] > min_child_value:
                self.swap(curr, min_child_index)
                curr = min_child_index
            else:
                break

    def bubble(self, index):
        curr = index
        while True:
            parent_index, parent_value = self._parent(curr)
            if parent_value > self.array[curr]:
                self.swap(parent_index, curr)
                curr = parent_index
            else:
                break

    def push(self, item):
        self.array.append(item)
        self.bubble(len(self.array) - 1)

    def pop(self):
        if self.length == 0:
            raise ValueError('Heap is empty. Add more items')
        elif self.length == 1:
            self.array.pop(-1)
        else:
            to_return = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop(-1)
            self.sink(0)
            return to_return

    @property
    def min(self):
        return self.array[0]

    def heapify(self):
        """This operation should always take O(N) time"""
        last_child = self.length - 1
        last_parent_with_child = ceil(last_child / 2 - 1)
        while last_parent_with_child >= 0:
            self.sink(last_parent_with_child)
            last_parent_with_child -= 1


if __name__ == '__main__':
    heap = Heap([10, 3, 5, 6, 7, 8, -3, 4])
    heap.heapify()
    print(heap.pop())
    print(heap)