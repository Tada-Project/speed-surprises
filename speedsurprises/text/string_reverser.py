"""Function that reverses strings."""

# Source and/or inspiration for function(s):
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
