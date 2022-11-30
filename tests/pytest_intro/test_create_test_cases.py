import pytest
greeting = 'Hello, my name is Zoe'
the_list = [23, 6, 12, 17]

# Test case to verify that the greeting string starts with 'the'
# This test is skipped
def test_string():
  is_it = greeting.startswith('Hello')
  assert is_it == True

# Test case to append 56 to the list and 
# verify that '56' is now in the list
def test_list():
  the_list.append(56)
  assert 56 in the_list