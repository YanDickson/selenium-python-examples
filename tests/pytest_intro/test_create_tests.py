class TestPytest:
  greeting = 'Hello, my name is Zoe'
  the_list = [23, 6, 12, 17]

  def test_string(self):
    is_it = self.greeting.startswith('Hello')
    assert is_it == True

  def test_list(self):
    self.the_list.append(56)
    assert 56 in self.test_list