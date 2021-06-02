# List Comprehension
# [new_item for item in list]
# [new_item for item in list if condition]

# Create new list with incrementing each value by 1
list1 = [1, 2, 3]
new_list1 = [n + 1 for n in list1]
print(new_list1)

# Print letter of the name
name = "Steve"
letter_list = [n for n in name]
print(letter_list)

# Doubled every number from the range
doubled_list = [n * 2 for n in range(1, 5)]
print(doubled_list)

# Create a new list of odd number
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list2 = [n for n in list2 if n % 2 != 0]
print(new_list2)

# Squared list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_list = [n * n for n in numbers]
print(squared_list)