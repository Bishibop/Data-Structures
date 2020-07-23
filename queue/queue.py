import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


#  class Queue:
#      def __init__(self):
#          self.size = 0
#          self.storage = []
#
#      def __len__(self):
#          return len(self.storage)
#
#      def enqueue(self, value):
#          self.storage.append(value)
#
#      def dequeue(self):
#          if self.storage:
#              val = self.storage[0]
#              self.storage = self.storage[1:]
#              return val
#          else:
#              return


class Queue:
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

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        # Directly manipulating the head and tail properties of the
        # linkedlist feels like cheating...
        head = self.storage.head
        if head is None:
            return
        elif head is self.storage.tail:
            val = head.get_value()
            self.storage.head = None
            self.storage.tail = None
            return val
        else:
            val = head.get_value()
            self.storage.head = head.get_next()
            return val
