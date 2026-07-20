"""
## Custom Exceptions in Python

This notebook demonstrates how to create and use custom exception classes in Python, including adding custom attributes and providing additional context to exception messages.
"""

# Creating custom exception

class custom_exception(Exception):
  """ This is a custom exception """

  def __init__(a, message='custom error'):
    a.message= message
    super().__init__(a.message)

try:
  raise custom_exception()
except custom_exception as e:
  print(e)

# Adding custom attribute to exception

class custom_exception(Exception):

  def __init__(self, message, error_code):
    self.message= message
    self.error_code = error_code
    super().__init__(message)

  def __str__(self):
    return f"{self.message} (Error Code:{self.error_code})"

error= custom_exception('abc', 500)
print(error)

# Rising Custom Exception

class My_exception(Exception):
  pass

def div(a,b):
  if b==0:
    raise My_exception('Division by zero is not applicable')
  return a/b

print(div(10,0))

# Custom Exception with Additional context

class its_error(Exception):

  def __init__( self, message, filename, lineo):
    super().__init__(message)
    self.message= message
    self.filename= filename
    self.lineo= lineo

  def __str__(self):
    return f'{self.message} in {self.filename} at line {self.lineo}'

try:
  raise its_error('hello error','dummy.txt',15)
except its_error as e:
  print(f'error= {e}')