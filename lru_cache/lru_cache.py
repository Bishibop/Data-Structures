import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.recency_list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            key_node = self.recency_list.find(lambda x: x[0] == key)
            self.recency_list.move_to_end(key_node)
            return key_node.value[1]
        else:
            return

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            key_node = self.recency_list.find(lambda x: x[0] == key)
            self.recency_list.delete(key_node)
        else:
            if self.size == self.limit:
                print("deleting old element")
                removed_pair = self.recency_list.remove_from_head()
                del self.storage[removed_pair[0]]
            else:
                self.size += 1
        self.storage[key] = value
        self.recency_list.add_to_tail((key, value))
