#!/usr/bin/env python
# coding: utf-8

# In[2]:


#inro to positional args
def describe_pet(animal_type, pet_name):
    """Display pet info"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}")
    
describe_pet('dog','sweety')


# In[3]:


describe_pet('cat','peach')


# In[7]:


def add(a,b):
    print(f"\n addition of {a} and {b} numbers is {a+b}")
    
add(2,3)


# In[8]:


#keyword args
describe_pet(pet_name='jimmy',animal_type='dog')


# In[13]:


#Intro to returning values from a function
def get_formatted_name(firstname,lastname):
    full_name = f"{firstname}{lastname}"
  

musician=get_formatted_name('Jimmy','Hendricks')
print(musician)


# In[15]:


def get_formatted_name(firstname,lastname):
    full_name = f"{firstname} {lastname}"
    return full_name.title()

musician=get_formatted_name('Jimmy','Hendricks')
print(musician)


# In[21]:


myname=get_formatted_name('Kiran','mommileti')
print(myname)


# In[22]:


describe_pet('dog','sweety')


# In[ ]:




