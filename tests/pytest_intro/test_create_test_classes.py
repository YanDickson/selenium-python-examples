greeting = 'Hello, my name is Zoe'
the_list = [23, 6, 12, 17]

class CheckBasics:

  # Test case to verify that the greeting string starts with 'the'
  def test_string(self):
    is_it = greeting.startswith('Hello')
    assert is_it == True

  # Test case to append 56 to the list and 
  # verify that '56' is now in the list
  def test_list(self):
    the_list.append(56)
    assert 56 in the_list

class TestBasics:

  # Test case to verify that the greeting string starts with 'the'
  def test_string(self):
    is_it = greeting.startswith('Hello')
    assert is_it == True

  # Test case to append 56 to the list and 
  # verify that '56' is now in the list
  def test_list(self):
    the_list.append(56)
    assert 56 in the_list