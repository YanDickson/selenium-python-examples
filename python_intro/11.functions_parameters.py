# Function with two positional arguments, "name" and "company"
def employee_info(name, company):
  print("My name is {} and I work at {}".format(name, company))

# Calling the `employee_info` function and 
# passing it the parameters for name and company
employee_info("Yanique", "QualityWorks")

# Function with two keyword arguments, "name" and "age"
def personal_info(name="Luna", age=10):
  print("My name is {} and I'm {}".format(name, age))

# Calling the `personal_info` function with no arguments
personal_info()

# Calling the `personal_info` function with one of two keyword arguments
personal_info(name="John")

# Calling the `personal_info` function with both keyword arguments
personal_info(name="Sam", age="15")

# Calling the `personal_info` function with the arguments in any order
personal_info(age=19, name="Paula")
