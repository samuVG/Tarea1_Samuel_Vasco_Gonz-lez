#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np # importación de librerías para comparar resultados
import scipy.special 
import funciones


# In[18]:


funciones.Factorial(4)==np.math.factorial(4) #test función factorial


# In[19]:


funciones.Binomial(3,2)==scipy.special.binom(3,2) #test función binomial


# In[ ]:




