# Fucntion with no value specified after the return statement
# Function will return None
def return_none(a, b):
  c = a + b
  return

# None is returned when the fucntion is executed
return_none(3, 5)

# Fucntion with 'c' specified as the return value
# Function will return the value of 'c'
def return_value(a, b):
  c = a + b
  return c

# 8 is returned
return_value(3, 5)
