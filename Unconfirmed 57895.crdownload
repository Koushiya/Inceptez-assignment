#!/usr/bin/env python
# coding: utf-8

# # Create a program that asks the user to enter their name and their age. Print out a message that tells them the year that they will turn 100 years old

# In[15]:


name = input("Enter your name: ")
current_age = int(input("Enter your age: "))
hundredth_year = 2022 + (100 - current_age)
print(f'{name} will become 100 years old in the year {hundredth_year}.')


# # What is pandas groupby? Demonstrate with your own example

# In[19]:


import pandas as pd


# In[22]:


School = {'name': ['ramya', 'vidya', 'ram', 'anand'], 
         'sub': ['Science', 'maths', 'English', 'sanscrit'],
          'marks': [98, 65, 99, 75]}
df = pd.DataFrame(School)
print(df)


# # How to create a dataframe from list?

# In[40]:


name = ['john', 'andrea', 'gulf', 'mark']
ages = [32, 32, 36, 31]
Zipped = list(zip(name, ages))
df = pd.DataFrame(Zipped, columns=['name', 'ages'])
print(df)


# # What are the ways to combine the dataframe in pandas. Give an example for each

# In[60]:


df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': ['a1', 'b2', 'c3']})
df2 = pd.DataFrame({'col1': [4, 5, 6], 'col2': ['d', 'e', 'f'], 'col3': ['d4', 'e5', 'f6']})
df3 = pd.DataFrame({'col1': [7, 8, 9], 'col2': ['g', 'h', 'i'], 'col4': ['g7', 'h2', 'i3']})
print(df1)
print(df2)
print(df3)


# In[58]:


df_concat = pd.concat([df1, df2],  ignore_index = True)
print(df_concat)


# # What is the difference between list and tuples in Python?
# 

# In[74]:


# It is mutable, you can alter like insert, delete, replace etc..
list1 = ['a', 'b', 'c', 'd', 'e']
tuple1 = ('a', 'b', 'c', 'd', 'e')
print(list1)
print(tuple1)


# # Find out the mean, median and standard deviation of this numpy array -> np.array([1,5,3,100,4,48])

# In[76]:


import numpy as np


# In[78]:


mmsd = np.array([1,5,3,100,4,48])
np.mean(mmsd)


# In[79]:


np.median(mmsd)


# In[80]:


np.std(mmsd)


# # How will you remove duplicate elements from a list?

# In[89]:


duplist1 = [10,20,30,40,10,20,50,60]
duplist2 = list()
for i in duplist1:
    if i not in duplist2:
        duplist2.append(i)
print(duplist2)


# # What is a map() function in Python? Give an example

# In[93]:


def square(n):
    return n*n

my_list = [2,3,4,5,6,7,8,9]
updated_list = map(float, my_list)
print(updated_list)
print(list(updated_list))


# # What is pass in Python?

# In[112]:


for name in 'koushiya': 
   if name == 'h':
      pass
   print(name)
   


# # What is vstack() in numpy? Give an example

# In[122]:


np_array1 = np.array([[1, 2], [4, 5]])
np_array2 = np.array([[7, 8], [10, 11]])
np_array3 = np.vstack((np_array1, np_array2))
print(np_array3)


# In[ ]:





# In[ ]:





# In[ ]:




