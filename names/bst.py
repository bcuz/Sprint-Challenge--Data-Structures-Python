from dll_queue import Queue

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    # like the root
    self.root = None
    self.left = None
    self.right = None
    self.length = 0

  # Insert the given value into the tree
  def insert(self, value):
    newNode = Node(value)
    self.length += 1

    if self.root == None:
      self.root = newNode
      return

    current = self.root

    while True:
      # accounting for duplicate values made it work
      if value == current.value:
        break
      elif newNode.value > current.value:
        if current.right:
          current = current.right
        else:
          current.right = newNode
          break
      elif newNode.value < current.value:
        if current.left:
          current = current.left
        else:
          current.left = newNode
          break

    # def recursion(current):
    #   if newNode.value > current.value:
    #     if current.right:
    #       current = current.right
    #       recursion(current)
    #     else:
    #       current.right = newNode          
    #   elif newNode.value < current.value:
    #     if current.left:
    #       current = current.left
    #       recursion(current)
    #     else:
    #       current.left = newNode          
    # recursion(current)    

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    current = self.root

    while True:
      if target == current.value:
        return target
      elif target > current.value:
        if current.right:
          current = current.right
        else:
          return False
      elif target < current.value:      
        if current.left:
          current = current.left
        else:
          return False                  
  
  def bft_print(self):
    queue = Queue()

    queue.enqueue(self.root)

    while queue.len() > 0:
      current = queue.dequeue()
      # need to call func on the value of the node
      print(current.value)

      if current.left:
        queue.enqueue(current.left)
      if current.right:
        queue.enqueue(current.right)          

bst = BinarySearchTree()
bst.insert('adam')
bst.insert('adam')
# bst.insert(3)
# bst.insert(7)

#    5
# 2    7
#  3

# bst.bft_print()        