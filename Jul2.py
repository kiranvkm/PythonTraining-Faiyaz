#!/usr/bin/env python
# coding: utf-8

# In[5]:


height = input("how tall are you, in inches?\n")
height = int(height)
if height >= 48:
    print("\nyou are tall enough to ride bike")
else:
    print("\nyou need to grow up")


# In[6]:


#modulo operator
4%3


# In[7]:


11%4


# In[13]:


#how to test if the given number is even or odd
num = input("enter a number\n")
num = int(num)
if num%2==0:
    print(f"the value {num} is even")
else:
    print(f"the value {num} is odd")


# In[7]:


#While loop
num = 1
while num <=10:
    print(num)
    print(f"num executed {num} times")
    num +=1
    


# In[ ]:




