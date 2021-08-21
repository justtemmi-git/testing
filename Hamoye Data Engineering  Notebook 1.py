#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as sm


# In[2]:


mydata_url= 'https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'


# In[3]:


mydata_fuel= pd.read_csv(mydata_url,error_bad_lines= False)


# In[4]:


mydata_fuel.head(10)


# In[5]:


mydata_fuel.describe(include= 'all')


# In[6]:


len(mydata_fuel)


# In[7]:


mydata_fuel.shape


# In[8]:


mydata_fuel.isnull().sum()


# In[9]:


# Percentage of missing values in fuel_unit
mydata_fuel['fuel_unit'].isnull().value_counts()/len(mydata_fuel)


# The percentage of missing values in fuel_unit is less than 1%, so I will keep it and fill in the missing values with the mode.

# In[10]:


mydata_fuel['fuel_unit'].value_counts()/len(mydata_fuel)


# mcf is the mode of the values in fuel_unit

# In[11]:


mydata_fuel['fuel_unit'].fillna(mydata_fuel['fuel_unit'].mode()[0], inplace = True)


# In[12]:


#re-check for missing values
mydata_fuel.isnull().sum()


# In[14]:


mydata_fuel.groupby('report_year')['report_year'].count()


# In[18]:


mydata_fuel.groupby('fuel_type_code_pudl').first()


# EXPLORATORY DATA ANALYSIS (VISUALISATION AND SUMMARY STATISTICS)

# In[ ]:




