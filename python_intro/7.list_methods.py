# Creating lists
string_list = ["shrub", "path", "river", "path"]
number_list = [21, 5, 7, 9, 3]
mixed_list = [13, "tree", [4, 6], True]

# Adds "stream" to the end of the list
# The result is ['shrub', 'path', 'river', 'path', 'stream']
string_list.append('stream')

# Returns the index of "stream" in the list
# The result is 4
item_index = string_list.index('stream')

# Returns the number of instances of "path" in the list
# The results is 2
item_count = string_list.count('path')
