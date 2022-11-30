def test_assertions():
  sample_string = "the string"
  starts_with_the = sample_string.startswith("the")
  small_num = 15
  large_num = 45

  # Asserting in or not in
  assert "the" in sample_string
  assert "apple" not in sample_string

  # Asserting equal to or not equal to
  assert starts_with_the == True
  assert starts_with_the != False

  # Asserting greater than or less than
  assert small_num < large_num
  assert large_num > small_num 
  