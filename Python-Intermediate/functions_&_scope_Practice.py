"""# Practice Questions

#Conceptual & Error Finding

***Question 1***
1. Output prediction
```
x=10
def f():
    print(x)
f()
```
Why does this work?

-> Output= 10

---


This works because first python search for local variable, but when it did not find in local scope, it searches for global scope an put value of x from global scope.

***Question 2***
"""

# 2. Scope confusion
x = 10

def f():
    x = x + 5
    return x

f()

# What happens? Why?
#-----------------------------------------------
# o/p> UnboundLocalError
# This happen because local variable x is assigned inside defination of function f, hence python assume it as a local variable.

# Fix
def f():
  global x
  x=x+5
  return x
f()

"""***Question 3***"""

#args vs kwargs
def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, a=3, b=4)
# Predict output
# Explain structure
#---------------------------------------
# o/p> (1,2){'a':3, 'b':4}
# *args stores tuple and **kwargs posses dictionary

"""***Question 4***"""

# Returning multiple values
def stats(nums):
    return sum(nums), len(nums)

s = stats([1,2,3])
print(s)
# What is returned?
# How to unpack?
# --------------------------------------------
# In the form of tuple, sum of numbers and number of numbers passed is returned

# Unpack
total, length= stats([1,2,3])
print(total, length)

""" ***Question 5***"""

# kwargs misuse
def f(**kwargs):
    print(kwargs['a'])

f(b=10)
# What error occurs? Why?
#-------------------------------------------
#KeyError: 'a'
#Fix: use >> print(kwargs.get('a'))

"""***Question 6***"""

#Flexible sum

# Accept any number of numbers
# Return sum

def flexible_sum(*args):
  return sum(args)

flexible_sum(1,2,3,1.1)

"""***Question 7***"""

# Configurable filter
# Return values > threshold

def filter_data(data, threshold=10):
  return [x for x in data if x>10]

filter_data([15,12,5,68,5,2,9,0])

"""***Question 8***"""

# Multi-output function
# Return:
# mean, max and min

def analyze(nums):
  return sum(nums)/len(nums), max(nums), min(nums)

analyze([1,2,3,4,5])

"""***Question 9***"""

def configure_model(**kwargs):
  '''kwargs-driven function

  Accept parameters like lr, epochs
  Return dict of config'''
  return kwargs

configure_model(lr=0.1, epochs=10)

"""# Related to Real World use cases

***Question 10***
"""

def clean_data(data):
  '''Data cleaning pipeline

  Remove None values
  Remove negatives'''
  return [item for item in data if item is not None and item >= 0]

print(clean_data([None, 23,-45,0, 55, -55]))

"""***Question 11***"""

def scale_data(data, method="minmax"):
  '''Feature scaling

  If "minmax" → scale between 0–1
  If "standard" → normalize'''
  if method == 'minmax':
    mn, mx= min(data), max(data)
    return [x-mn/(mx-mn) for x in data]
  if method== 'standard':
    mean= sum(data)/len(data)
    std= (sum((x-mean)**2 for x in data))/ len(data)
    return [(x-mean)/std for x in data]

print(scale_data([1,2,3,4,5], method='minmax'))
print(scale_data([1,2,3,4,5], method='standard'))

"""***Question 12***"""

def pipeline(data, threshold):
  '''Pipeline function

  Steps:
  clean data
  filter > threshold
  square values'''

  data_filter= [x for x in data if x is not None and x> threshold]
  return [y**2 for y in data_filter]

pipeline([1,-12, None, 38, 86, -9, 0, None, 34, 56, 6, 9, 11], 10)

"""***Question 13***"""

def run_experiment(data, threshold, scale=True):
  '''Experiment runner

  Optional scaling
  Filtering
  Return processed data'''
  data_filter= [x for x in data if x is not None and x> threshold]
  if scale==False:
    print('Scaling is disabled')
    return data_filter
  if scale==True:
      print('Minmax Scaling is enabled')
      mn, mx= min(data_filter), max(data_filter)
      return [x-mn/(mx-mn) for x in data_filter]


a= run_experiment([1,-12, None, 38, 86, -9, 0, None, 34, 56, 6, 9, 11], 10, True)
print(a)
b= run_experiment([1,-12, None, 38, 86, -9, 0, None, 34, 56, 6, 9, 11], 10, False)
print(b)

"""***Question 14***"""

def train_model(data, **params):
  '''kwargs in ML-style API

  Accept:
  learning_rate
  epochs
  Return config + data size'''
  return{ 'Data Size':len(data), 'Params': params}

train_model([24,56,23,68,68], learning_rate= 1, epochs= 50)

"""***Question 15***"""

#Avoid global state
#Bad code:
model = {}

def update_model(x):
    model['data'] = x

#Task:
#Refactor into proper function design

# Refactor
def update_model(x):
  model={'data':x}
  return model

update_model([24,56,23,68,68])