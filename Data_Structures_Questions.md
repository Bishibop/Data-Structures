Answer the following questions for each of the data structures you implemented as part of this project.


## Stack

1. What is the runtime complexity of `push` using a list?

    O(1)

2. What is the runtime complexity of `push` using a linked list?

    O(1)

3. What is the runtime complexity of `pop` using a list?

    O(1)

4. What is the runtime complexity of `pop` using a linked list?

    O(1)

5. What is the runtime complexity of `len` using a list?

    O(1)

6. What is the runtime complexity of `len` using a linked list?

    O(n)


## Queue

1. What is the runtime complexity of `enqueue` using a list?

    O(1)

2. What is the runtime complexity of `enqueue` using a linked list?

    O(1)

3. What is the runtime complexity of `dequeue` using a list?

    O(n)
    I think this could alternatively be swapped with `enqueue` if you just
    switched which ends of the list you used for each operation.

4. What is the runtime complexity of `dequeue` using a linked list?

    O(1)

5. What is the runtime complexity of `len` using a list?

    O(1)

6. What is the runtime complexity of `len` using a linked list?

    O(n)


## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

    O(1)

2. What is the runtime complexity of `ListNode.insert_before`?

    O(1)

3. What is the runtime complexity of `ListNode.delete`?

    O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

    O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

    O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

    O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

    O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

    O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The worst-case runtime of JS `Array.splice` is O(n) because you would have
    to copy as many as n-1 elements to a new array. The doubly linked lists's
    `delete` is just O(1) because all you do is remap the references of
    elements on either side of it, which the element to be deleted has
    references too.


## Binary Search Tree

1. What is the runtime complexity of `insert`? 

    O(log(n))

2. What is the runtime complexity of `contains`?

    O(n)

3. What is the runtime complexity of `get_max`? 

    O(log(n))

4. What is the runtime complexity of `for_each`?

    O(n)


## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
