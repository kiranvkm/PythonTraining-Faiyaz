#!/usr/bin/env python
# coding: utf-8

# In[8]:


dimensions = (200,300,400)
print("original dim defined")
for dim in dimensions:
    print(dimensions)


dimensions = (500,600,700)
print("modified")
for dim in dimensions:
    print(dim)


# In[19]:


#FOR Loop in Tuple
dimensions = (200,300,400)
print("original dim defined")
for dim in dimensions:
    print(dim)


dimensions = (500,600,700)
print("\nmodified")
for dim in dimensions:
    print(dim)


# In[12]:


cars = ['audi','bmw','merc','honda']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# In[16]:


cars = ['audi','bmw','merc','honda']
for car in cars:
    if car == 'bmw':
        print(car.lower())
    else:
        print(car.title())


# In[18]:


#Python is CASE SENSITIVE
cars = ['audi','bmw','merc','honda']
for car in cars:
    if car == 'bmw':
        print(car.lower())
    else:
        print(Car.title())


# In[27]:


#Equality condition
car = "Audi"
car == "audi"


# In[26]:


car = "Audi"
car.lower() == "audi"


# In[31]:


#Not Equality condition
req_Topping = "Mushroom"
if req_Topping != "Mushroom":
    print("get mushroom")
else:
    print("get chicken")


# In[ ]:




