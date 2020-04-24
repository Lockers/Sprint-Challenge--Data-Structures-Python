import time
import os

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new nodes value is less than our current nodes value
        if value < self.value:
            # if there is no left child already here
            if not self.left:
                # place a new bst with the value passed in to the left
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process recursively on the left
                self.left.insert(value)

        # check if new nodes value is greater than or equal to our current nodes value
        if value >= self.value:
            # if there is no right child already here
            if not self.right:
                # place a new bst with the value passed in to the right
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process recursively on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case. if value matches current target
        if self.value == target:
            # return True
            return True

        # if target less than value
        if target < self.value:
            # check left child recursively
            # if no left child
            if not self.left:
                # return false
                return False
            # otherwise
            else:
                # call contains on the left
                return self.left.contains(target)
        # otherwise
        else:
            # check right child recursively
            # if no right child
            if not self.right:
                # return false
                return False
            # otherwise
            else:
                # call contains on the right
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if tree empty return false
        if not self:
            return None


        # if there is no right child
        if not self.right:
            # return the value
            return self.value

        # recursive case
        # call get max on the right child
        return self.right.get_max()

        # TODO: iterative approach
        # # init a max val variable
        # max_val = self.value

        # # take ref to current node
        # current = self

        # # while current node exists
        # while current:
        #     # check if current val is greather than max val
        #     if current.value > max_val:
        #         # set max val to current val
        #         max_val = current.value

        #     # move to the next right node
        #     current = current.right

        # # return max val
        # return max_val

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # do the call back using self.value as the parameter
        cb(self.value)

        # if left exists
        if self.left:
            # call foreach on left
            self.left.for_each(cb)

        # if right exists
        if self.right:
            # call foreach on right
            self.right.for_each(cb)

start_time = time.time()
path = 'C:\\Users\\mattl\\Documents\\Git\\Computer Science\\Sprint Challenge\\Sprint-Challenge--Data-Structures-Python\\names\\'
file_path = os.path.join(path, 'names_1.txt')
f = open(file_path, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

path = 'C:\\Users\\mattl\\Documents\\Git\\Computer Science\\Sprint Challenge\\Sprint-Challenge--Data-Structures-Python\\names\\'
file_path2 = os.path.join(path, 'names_2.txt')
f = open(file_path2, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_1_bst = BinarySearchTree(names_1)
for name_1 in names_1:
    names_1_bst.insert(name_1)

for name_2 in names_2:
    if names_1_bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()

# from 0(n2) to 0(n) 0.1 seconds ftw

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
