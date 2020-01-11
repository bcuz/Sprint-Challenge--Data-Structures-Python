from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        # adding when under limit
        self.storage.add_to_tail(item)
        self.size += 1


        # if full, head becomes the newest item.

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # initial impression: iterate through dll and append to array?

        current = self.storage.head
        
        if not current:
            return None

        while current:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

ring = RingBuffer(1)

ring.append('a')

# print(ring.storage.head.value)
print(ring.get())