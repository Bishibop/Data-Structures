"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # List of 1 or more elements
        if self.head:
            old_head = self.head
            new_head = ListNode(value, None, old_head)
            old_head.prev = new_head
            self.head = new_head
        # Empty list
        else:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head

        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # List of > 1 elements
        if self.head and self.head.next:
            old_head_val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return old_head_val
        # List of 1 element
        elif self.head:
            old_head_val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return old_head_val
        # Empty list
        else:
            return None

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # List of 1 or more elements
        if self.head:
            new_tail = ListNode(value, self.tail)
            self.tail.next = new_tail
            self.tail = new_tail
        # Empty list
        else:
            new_tail = ListNode(value)
            self.head = new_tail
            self.tail = new_tail

        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # List of > 1 elements
        if self.head and self.head.next:
            old_tail_val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return old_tail_val
        # List of 1 element
        elif self.head:
            old_tail_val = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return old_tail_val
        # Empty list
        else:
            return None

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        # List of > 1 elements
        if self.head and self.head.next:
            previous_node = node.prev
            next_node = node.next
            if previous_node:
                previous_node.next = next_node
            else:
                self.head = next_node
            if next_node:
                next_node.prev = previous_node
            else:
                self.tail = previous_node
            self.length -= 1
        # List of 1 element
        elif self.head is node:
            self.head = None
            self.tail = None
            self.length = 0
        # Empty list
        else:
            return None

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        # Non-empty list
        if self.head:
            current_max = self.head.value
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                if current_node.value > current_max:
                    current_max = current_node.value
                else:
                    pass
            return current_max
        # Empty list
        else:
            return None
