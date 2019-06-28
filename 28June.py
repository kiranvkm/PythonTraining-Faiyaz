#!/usr/bin/env python
# coding: utf-8

# In[4]:


Board = {'color':'green'}
print(f"the color board is {Board['color']}.")


# In[6]:


#Modifying values in Dictionary
Board['color']='black'
print(f"the color of board is {Board['color']}.")


# In[9]:


veg = {'color':'green','name':'peas','texture':'beans'}
print(veg)


# In[10]:


veg['name']='chikudi'


# In[11]:


print(veg)


# In[14]:


##Deleting values in Dictionary
del veg['texture']
print(f"after deletion {veg}.")


# In[15]:


print(f"after deletion the color is {veg['color']}")


# In[17]:


#declaring similar objects
#Best Practices
fav_lang = {'kiran':'python','srini':'ruby','shiva':'js',
           }
lang = fav_lang['kiran'].title()
print(lang)


# In[18]:


print(f"Kiran's fav language is {lang}.")


# In[22]:


print(f"Srini's fav lng is {fav_lang['srini'].title()}")


# In[30]:


#GET method

fruit = {'color':'yellow','taste':'sweet'}
fruit_size = fruit.get('size',"size is not availbale")
print(fruit_size)


# In[32]:


fruit_size = fruit.get('color',"size is not availbale")
print(fruit_size)


# In[ ]:




