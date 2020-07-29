import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


#  class Stack:
#      def __init__(self):
#          self.size = 0
#          self.storage = []
#
#      def __len__(self):
#          return len(self.storage)
#
#      def push(self, value):
#          self.storage.append(value)
#
#      def pop(self):
#          if self.storage:
#              val = self.storage[-1]
#              del self.storage[-1]
#              return val
#          else:
#              return None


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        head = self.storage.head
        if head:
            count = 1
            next_node = head.get_next()
            while next_node:
                count += 1
                next_node = next_node.get_next()
            return count
        else:
            return 0

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.head:
            return self.storage.remove_tail()
        else:
            return None
