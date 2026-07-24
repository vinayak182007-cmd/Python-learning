
"""Module and Import 1: Basics.ipynb

This file Include:
1. Creating User defined module
2. Importing module
3. Creating User defined package
4. Path of directories where python looks for importing a module

"""

# Commented out IPython magic to ensure Python compatibility.
# # Creating User defined module
# %%writefile areaofcircle.py
# 
# def c_area(r):
#   area= 3.14*(r**2)
#   return area

# Using user defined module
import areaofcircle

print(areaofcircle.c_area(2))
print(__name__)
print(areaofcircle.__name__)

# Creating User defined package

import os
os.makedirs("my_package", exist_ok=True)

# __init__.py
with open("my_package/__init__.py", "w") as f:
    f.write("")

# math_func.py
with open("my_package/math_func.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b

def square(x):
    return x * x
""")

# greet.py
with open("my_package/greet.py", "w") as f:
    f.write("""
def greet(name):
    return f"Hello, {name}!"
""")

# Locating a module

import sys
for p in sys.path:
  print(p)
