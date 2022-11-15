# A simple class called Simple_class
# `name` and `age` are two attributes of the class
class SimpleClass:
  name = "Sara"
  age = 5

# Creating an instance of class `Simple_class`
my_class_object = SimpleClass()

# Accessing name and age from the created object
my_name = my_class_object.name
my_age = my_class_object.age

# When executed `Sara - 5` is printed
print("name is {} - age is {}".format(my_name, my_age))