#!/usr/bin/env python
# coding: utf-8

# In[7]:


class ClassName:
    def createName(self,name):
        self.name=name
    
    def displayName(self):
        return self.name
    
    def saying(self):
        print(f"Hello, {self.name}")
        
ClassName

first = ClassName()
first.createName('Kiran')
first.saying()


# sdsvsdvsdv
# 

# In[8]:


ululuill


# In[9]:


class ClassName:
    def createName(self,name):
        self.name=name
    
    def displayName(self):
        return self.name
    
    def saying(self):
        print(f"Hello, {self.name}")
        
ClassName

first = ClassName()
first.createName('Kiran')
first.saying()


# In[14]:


class Dog:
    """Modelling a dog"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(f"{self.name} is now sitting")
    
    def rollover(self):
        print(f"{self.name} has rolled over")
    
my_dog = Dog('Sweety',13)

my_dog.sit()
my_dog.rollover()


# In[16]:


print(f"My dogs name is {my_dog.name}")


# In[18]:


print(f"My dog's age is {my_dog.age}")


# In[ ]:




