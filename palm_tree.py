#!/usr/bin/python3
        #tips
# I:
# Going to print a tree
# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 space : 9 hashes

# need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hash by 2 each time through the loop
# 3. Save spaces to the stump by collacting tree height -1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# Get the number of rows for the tree
tree_height = input("How tall is tree height: ")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces untill later
stump_spaces = tree_height - 1 

# Make sure the right number of rows are printed 
while tree_height != 0:

# print the spaces
    for i in range(spaces):
        print(' ', end="")

# Print the hashes
    for i in range(hashes):
        print('#', end="")

# Newline after each row is printed 
    print()
# That spaces is decrement by 1 each time
    spaces -= 1
# That hashes is incremented by 2 each time
    hashes += 2
# Decrement tree height each time to jump out of the loop
    tree_height -= 1
# Print the spaces before the stump and then the hash
for i in range(stump_spaces):
    print(' ', end="")
print('#')
