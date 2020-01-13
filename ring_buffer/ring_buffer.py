from doubly_linked_list import DoublyLinkedList


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    # current is oldest item.
    self.current = None
    self.storage = DoublyLinkedList()
    self.size = 0

  def append(self, item):

    if self.size < self.capacity:
      self.storage.add_to_tail(item)
      self.current = self.storage.head
      self.size += 1
    else:
      # change the value of the oldest element to the new value coming in
      self.current.value = item

      # if the current oldest item is the tail, change it to the head
      if self.current == self.storage.tail:
        self.current = self.storage.head
        # otherwise make it the next node in the dll.
      else:
        self.current = self.current.next        
    

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

ring = RingBuffer(2)

ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')
ring.append('e')

print(ring.get())
# print(ring.storage.length)