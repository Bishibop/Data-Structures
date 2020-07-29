import math


class Heap:
    def __init__(self):
        self.storage = []

    def _parent_index(self, child_index):
        return math.floor((child_index - 1) / 2)

    def insert(self, value):
        self.storage.append(value)

        index = len(self.storage) - 1
        while self._bubble_up(index):
            index = self._parent_index(index)
        return

    def _bubble_up(self, index):
        parent_index = self._parent_index(index)

        if parent_index < 0:
            return False

        parent_value = self.storage[parent_index]
        child_value = self.storage[index]

        if parent_value >= child_value:
            return False
        else:
            self.storage[index] = parent_value
            self.storage[parent_index] = child_value
            return True

    def delete(self):
        if not len(self.storage):
            return

        index = 0
        priority_value = self.storage[0]
        self.storage[0] = self.storage[-1]
        del self.storage[-1]

        while index >= 0:
            index = self._sift_down(index)

        return priority_value

    def _sift_down(self, index):
        heap_max_index = len(self.storage) - 1
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        if left_index > heap_max_index:
            return -1
        elif right_index > heap_max_index:
            target_value = self.storage[index]
            self.storage[index] = self.storage[left_index]
            self.storage[left_index] = target_value
            return -1
        else:
            target_value = self.storage[index]
            left_value = self.storage[left_index]
            right_value = self.storage[right_index]
            if right_value >= left_value:
                self.storage[right_index] = target_value
                self.storage[index] = right_value
                return right_index
            else:
                self.storage[left_index] = target_value
                self.storage[index] = left_value
                return left_index

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)
