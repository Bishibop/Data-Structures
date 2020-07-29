"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    # Why not just put all of this in the AVLTree class?
    # Why have a separate one, if the AVLTree class is recursive?
    # I get it when it's a doubly linked list, and you want
    # meta-data for the whole structure. But we don't have any of that here
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        if node:
            self.height = 0
        else:
            self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node is not None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.right is not None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node.left:
            left_height = self.node.left.height
        else:
            left_height = -1

        if self.node.right:
            right_height = self.node.right.height
        else:
            right_height = -1

        if right_height > left_height:
            self.height = right_height + 1
        else:
            self.height = left_height + 1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        self.balance = self.node.right.height - self.node.left.height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent.
    """
    def left_rotate(self):
        # what about the left node of the right child? It's just getting
        # overwritten. This only works on certain nodes
        # You would have to cascade that left node down that whole subtree
        parent_tree = self
        right_node = self.node.right.node
        self.node = right_node
        self.node.left = parent_tree
        parent_tree.node.right = None

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent.
    """
    def right_rotate(self):
        parent_node = self.node
        left_node = self.left
        self.node = left_node
        self.node.right = parent_node
        parent_node.left = None

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        if self.balance > 1:
            self.left_rotate()
            self.update_balance()
            self.update_height()
        elif self.balance < -1:
            self.right_rotate()
            self.update_balance()
            self.update_height()
        else:
            pass

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        ancestors = []
        target = self
        parent = self
        while target:
            parent = target
            ancestors.append(parent)
            if key < target.node.value:
                target = target.node.left
            else:
                target = target.node.right
        if key < parent.node.value:
            parent.node.left = AVLTree(Node(key))
        else:
            parent.node.right = AVLTree(Node(key))

        while ancestors:
            parent = ancestors.pop()
            parent.update_height()
            parent.update_balance()
            parent.rebalance()
