#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]


# In[7]:


plt.plot(x, y)


# In[8]:


plt.scatter(x, y)


# In[11]:


t=np.linspace(0, 10, num=51)
t


# In[12]:


f = np.cos(t)
f


# In[18]:


plt.plot(t,f, color='green')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.title('График f(t)')
plt.xlim(0.5,9.5)
plt.ylim(-2.5, 2.5)


# In[20]:


x1=np.linspace(-3, 3, num=51)
y1 = x1**2
y2 = 2 * x1 + 0.5
y3 = -3 * x1 - 1.5
y4 = np.sin(x1)
x1, y1, y2, y3, y4


# In[21]:


from matplotlib.figure import Figure


# In[25]:


fig, axes = plt.subplots(nrows=2, ncols=2, figsize =(8, 8))
axes[0].plot(x1, y1)
axes[1].plot(x1, y2)
axes[2].plot(x1, y3)
axes[3].plot(x1, y4)   
    
        
fig.tight_layout()


# In[ ]:




