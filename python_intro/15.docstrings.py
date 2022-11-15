## FUNCTIONS
# Using doctring to document a functions
def sum_it(x, y):
  '''Returns the sum of `x` and `y`'''
  sum = x + y
  return sum

## CLASSES
# Using doctring to document a classes
class Student:
  '''Describes the student object'''

  my_purpose = "I'm here to learn"

  # Instance variables
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Class methods
  def calculate_grad_year(self, current_year):
    '''Calculate and return the grad year given the provided `current_year`'''
    grad_year = current_year - self.age + 18
    return grad_year
