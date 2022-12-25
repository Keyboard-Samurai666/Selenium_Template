import re

def is_python_file(filename):
  # Check if the filename ends with '.py'
  pattern = r'\.py$'
  if re.search(pattern, filename):
    return True
  else:
    return False

# Test the function
print(is_python_file('hello.py'))  # prints True
print(is_python_file('hello.txt'))  # prints False
print(is_python_file('hello.pyc'))  # prints False
