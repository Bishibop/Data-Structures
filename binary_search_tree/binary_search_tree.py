from stack import Stack
from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Recursive
    #  def insert(self, value):
    #      if value == self.value:
    #          new_node = BSTNode(value)
    #          old_node = self.right
    #          self.right = new_node
    #          new_node.right = old_node
    #      elif value < self.value:
    #          if self.left:
    #              self.left.insert(value)
    #          else:
    #              self.left = BSTNode(value)
    #      elif value > self.value:
    #          if self.right:
    #              self.right.insert(value)
    #          else:
    #              self.right = BSTNode(value)

    # Iterative
    def insert(self, value):
        target_node = self
        parent_node = self
        while target_node:
            parent_node = target_node
            if value < target_node.value:
                target_node = target_node.left
            else:
                target_node = target_node.right
        if value < parent_node.value:
            parent_node.left = BSTNode(value)
        else:
            parent_node.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    # Recursive
    #  def contains(self, target):
    #      if target == self.value:
    #          return True
    #      elif target < self.value:
    #          if self.left:
    #              return self.left.contains(target)
    #          else:
    #              return False
    #      elif target > self.value:
    #          if self.right:
    #              return self.right.contains(target)
    #          else:
    #              return False

    # Iterative
    def contains(self, target):
        target_node = self
        while True:
            if target == target_node.value:
                return True
            elif target < target_node.value:
                if target_node.left:
                    target_node = target_node.left
                else:
                    return False
            elif target > target_node.value:
                if target_node.right:
                    target_node = target_node.right
                else:
                    return False

    # Return the maximum value found in the tree
    # Recursive
    #  def get_max(self):
    #      if self.right:
    #          return self.right.get_max()
    #      else:
    #          return self.value

    # Iterative
    def get_max(self):
        target_node = self
        while target_node.right:
            target_node = target_node.right
        return target_node.value

    # Call the function `fn` on the value of each node
    # Recursive
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Iterative
    #  def for_each(self, fn):
    #      #  How would you do this iteratively???

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        node_queue = Queue()
        node_queue.enqueue(self)
        while len(node_queue) > 0:
            current_node = node_queue.dequeue()
            print(current_node.value)
            if current_node.left:
                node_queue.enqueue(current_node.left)
            if current_node.right:
                node_queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        node_stack = Stack()
        node_stack.push(self)
        while len(node_stack) > 0:
            current_node = node_stack.pop()
            print(current_node.value)
            if current_node.left:
                node_stack.push(current_node.left)
            if current_node.right:
                node_stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # I added this because it is called below and was missing here
    def in_order_dft(self):
        if self.left:
            self.left.in_order_dft()
        print(self.value)
        if self.right:
            self.right.in_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
#  bst = BinarySearchTree(1)
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
