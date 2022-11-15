# Creating a string
greeting = 'Hello, my name is Zoe'

# .split() - splits a string using the separator ", "
# The reulst is ['Hello', 'my name is Zoe']
result_list = greeting.split(', ')

# .upper() - converts the string, greeting, to uppercase
# The results is "HELLO, MY NAME IS ZOE"
upper_string = greeting.upper()

# .isupper() will return True if all letters are uppercased
# The result is True
is_it_upper = upper_string.isupper()

# .endswith() will return True if the string, greeting, ends with "Zoe"
# The result is True
ends_with_it = greeting.endswith('Zoe')

# .startswith() will return True if the string, greeting, starts with "Hello"
# The result is True
starts_with_it = greeting.startswith('Hello')

# len() will return the number of characters in the string, greeting
# The result is 21
the_length = len(greeting)
