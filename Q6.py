# Q6:

# Creating a list
my_list = [1, 2, 3, 4]

# Modifying an element
my_list[1] = 99
print(my_list)

# Adding an element
my_list.append(5)
print(my_list)

# Removing an element
my_list.pop(2)
print(my_list)

# Creating a string
my_string = "hello"

# Trying to change a character
try:
    my_string[0] = 'H'
except TypeError as e:
    print(f"Error: {e}")