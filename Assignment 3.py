#!/usr/bin/env python
# coding: utf-8

# # 1. Create a file calc.py which has following functions
# a. Function to find the factorial of a number
# b. Function to convert degree to Fahrenheit
# Write a new program in file “maths.py” such that you import functions of the file calc.py to your new program.
# Use from import statement to import the functions from the calc module

# In[16]:


import numpy as np
import pandas as pd
import os


# In[29]:


import maths


# In[28]:


def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print(fact(5))


# In[26]:


celsius =float(input('enter temp in celsius:'))
fahrenheit = (celsius * 9/5) + 32
print(celsius, 'celsius is:', fahrenheit, 'fahrenheit')


# # Write a new program in file “maths.py” such that you import functions of the file calc.py to your new program. Use from <module> import <functions> statement to import the functions from the calc module

# # 2. Implement a simple generator for Fibonacci series

# In[36]:


if n == 1:
    return 0
elif n == 2:
    return 1
else:
    return fibonacci(n - 1) + fibonacci(n - 2)

        


# In[37]:


def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


# In[39]:


gen = fib(10)


# In[40]:


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# # 3. Write an iterator class to iterate over a sequence of values in the reverse direction

# In[41]:


a = ([1, 2, 3, 4,5])
a.reverse()
print(a)

my_iter=iter(a)
for i in range(len(a)-1,-1,-1):
    print(next(my_iter))def decorating_fn(func):
    def tax_calculation(basepay,hra,allowance):
        print('BasePay : ',basepay, 'HRA : ',hra, 'SpecialAllowance : ',allowance, end='  ,')
        tax_calc = (30/100) * basepay
        basepay = tax_calc
        print('Basepay after tax reduction : ', basepay)
        return func(basepay,hra,allowance)
    return tax_calculation


# # 4. Write a function “salary” that takes in base pay, HRA and special allowance as arguments and returns the sum of all the 3 salary elements. Then create a decorator function to add an additional element “Tax” (30% of base pay) and assign it back to base pay variable, and return the function (i.e., the final calculation of salary also includes tax)

# In[44]:


def decorating_fn(func):
    def tax_calculation(basepay,hra,allowance):
        print('BasePay : ',basepay, 'HRA : ',hra, 'SpecialAllowance : ',allowance, end='  ,')
        tax_calc = (30/100) * basepay
        basepay = tax_calc
        print('Basepay after tax reduction : ', basepay)
        return func(basepay,hra,allowance)
    return tax_calculation
@decorating_fn
def salary(basepay,hra,allowance):
    sum = basepay + hra + allowance
    return sum


# In[51]:


salary(100,200,300)


# # 5. Write 3 examples on possible methods to changing a tuple

# In[48]:


tuple1 = (1, 2, 3, [1, 2, 3], 5)
print(tuple1)


# In[53]:


tuple2 = tuple1[:2]
tuple2


# In[ ]:




