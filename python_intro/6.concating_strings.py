greeting = 'Hello, my name is'
name = 'Zoe'
age = 14

# Adding strings together
# The result is 'Hello, my name is Zoe.'
a = greeting + ' ' + name + '.'
print(a)

# .format()  
# The result is 'Hello, my name is Zoe. I am 14.'
b = '{} {}. I am {}.'.format(greeting, name, age)
print(b)

# f-strings
# The result is 'Hello, my name is Zoe. I am 14.'
c = f'{greeting} {name}. I am {age}.' 
print(c)
