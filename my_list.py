# Create an empty list called my_list
my_list = []
# Append elements to my_list
my_list.extend([10, 20, 30, 40])
# Inserting the value 15 at the second position in the list
my_list.insert(1, 15)
# Extending my_list with another list
my_list.extend([50, 60, 70])
# Removeing the last element from my_list
my_list.pop()
# Sorting my_list in ascending order
my_list.sort()
# Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)
# Print updated list
print("Updated my_list:", my_list)
