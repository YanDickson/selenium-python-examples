class Student:
  
  my_purpose = "I'm here to learn"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Class method that accepts a second parameter `current_year`
  def calculate_grad_year(self, current_year):
    grad_year = current_year - self.age + 18
    return grad_year

  # Class method that only accepts `self` parameter
  def say_introduction(self):
    introduction = "My name is {} and {}.".format(self.name, self.my_purpose)
    return introduction

new_student = Student("John", 8)

# Accessing the variables of the `Student`class
new_student.calculate_grad_year(2022)
new_student.say_introduction()
new_student.my_purpose
new_student.age
