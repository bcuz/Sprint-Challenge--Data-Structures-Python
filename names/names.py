import time
from doubly_linked_list import DoublyLinkedList
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

dll = DoublyLinkedList()
# starting complexity of n^2.
length = 0

for name in names_1:
  dll.add_to_head(name)

for name in names_2:
  if dll.get(name) != None:
    length += 1

  # if name_1 in names_2:
  #   duplicates.add_to_head(name_1)

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"{length}")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
