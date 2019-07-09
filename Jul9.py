#!/usr/bin/env python
# coding: utf-8

# In[4]:


#default values in fn
def describe_pet(pet_name,animal_type='dog'):
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type} name is {pet_name}")
    
describe_pet('jimmy')


# In[5]:


describe_pet('jimmy','cat')


# In[7]:


# output printing in dictinry
def build_person(first_name, last_name):
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('AR','Rehman')
print(musician)
    


# In[9]:


#FOR loop in fn
def greet_users(names):
    for name in names:
        msg = f"Hello,{name.title()}"
        print(msg)
        
usernames = ['kirn','sarat','gupta']
greet_users(usernames)


# In[11]:


#arbitrary no of args
def make_pizza(*toppings):
    print(toppings)
make_pizza('mushroom','chicken','olives')


# In[ ]:




