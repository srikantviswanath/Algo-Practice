class MinHeap(object):

    def __init__(self, array):
        self.array = array

    def __str__(self):
        return str(self.array)

    def heapify(self):
        pass

    def heap_pop(self):
        if self.array:
            last_elt = self.array.pop()
            min_elt = self.array[0]
            self.array[0] = last_elt
            curr_idx = 0
            while curr_idx * 2 < len(self.array):
                smaller_val, smaller_idx = min(self.left_child(curr_idx), self.right_child(curr_idx), key=lambda tup: tup[0])
                if smaller_val < self.array[curr_idx]:
                    self._swap(curr_idx, smaller_idx)
                    curr_idx = smaller_idx
                else:
                    return min_elt
            return min_elt

    def heap_push(self, item):
        self.array.append(item)
        curr_idx = len(self.array) - 1
        while curr_idx > 0:
            curr_item = self.array[curr_idx]
            parent_item, parent_idx = self.parent(curr_idx)
            if curr_item < parent_item:
                self._swap(parent_idx, curr_idx)
                curr_idx = parent_idx
            else:
                break

    def _swap(self, idx1, idx2):
        self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]

    def parent(self, idx):
        if idx <= 0 or idx >= len(self.array):
            return None, -1
        parent_idx = idx // 2 - 1 if idx % 2 == 0 else idx // 2
        return self.array[parent_idx], parent_idx

    def left_child(self, idx):
        child_idx = idx * 2 + 1
        if child_idx < len(self.array):
            return self.array[child_idx], child_idx
        else:
            return None, -1

    def right_child(self, idx):
        child_idx = idx * 2 + 2
        if child_idx < len(self.array):
            return self.array[child_idx], child_idx
        else:
            return None, -1


if __name__ == '__main__':
    '''
                   3
            7              10
        12      13      14     16
     15    18

    '''
    heap = MinHeap([3, 7, 10, 12, 13, 14, 16, 15, 18])
    heap.heap_push(2)
    print(heap.heap_pop())