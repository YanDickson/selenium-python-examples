# Creating lists
number_list = [21, 5, 7, 9, 3]

# Returns the value of the last item in the list
# The result is 3
last_number = number_list[-1]

# Returns the value of the first item in the list
# The result is 21
first_number = number_list[0]

# Returns the 2nd to 3rd items in the list
# The results is [5, 7]
sub_list_0 = number_list[1:3]

# Returns the all items up to but not including index 3
# The result is [21, 5, 7]
sub_list_1 = number_list[:3]

# Returns all items from index 3 to the last ietm
# The result is [9, 3]
sub_list_2 = number_list[3:]
