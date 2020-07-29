class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        return self

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        elif not self.head.get_next():
            original_head_value = self.head.get_value()
            self.head = None
            self.tail = None
            return original_head_value
        else:
            original_head_value = self.head.get_value()
            self.head = self.head.get_next()
            return original_head_value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
        elif self.head is self.tail:
            original_tail_value = self.tail.get_value()
            self.head = None
            self.tail = None
            return original_tail_value
        else:
            original_tail_value = self.tail.get_value()
            current = self.head
            while current.get_next() is not self.tail:
                current = current.get_next()
            self.tail = current
            # Do you actually need to set this to none? If you moved the
            # ll tail reference, maybe you can just leave this  node
            # dangling off the end of the ll. Maybe it doesn't matter...
            self.tail.set_next(None)
            return original_tail_value

    def contains(self, value):
        if self.head is None and self.tail is None:
            return False
        else:
            current = self.head
            while current:
                if current.get_value() == value:
                    return True
                else:
                    current = current.get_next()
            return False

    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        else:
            current = self.head
            current_max = self.head.get_value()
            while current:
                current_val = current.get_value()
                if current_val > current_max:
                    current_max = current_val
                else:
                    pass
                current = current.get_next()
            return current_max
