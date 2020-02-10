import time
from doubly_linked_list import DoublyLinkedList
from bst import BinarySearchTree

start_time = time.time()

f = open('1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst = BinarySearchTree()
# starting complexity of n^2.
# ending complexity of n log(n)
duplicates = []

for name in names_1:
  bst.insert(name)

for name in names_2:
# if name is found in the bst, it's a duplicate
  search = bst.contains(name) 

  if search == name:
    duplicates.append(search)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"{duplicates}")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
