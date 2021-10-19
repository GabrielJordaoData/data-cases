#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


athletes = pd.read_excel("athletes.xlsx")
coaches = pd.read_excel("Coaches.xlsx")
gender = pd.read_excel("EntriesGender.xlsx")
medals = pd.read_excel("Medals.xlsx")
teams = pd.read_excel("Teams.xlsx")


# In[5]:


athletes.head()


# In[9]:


coaches.head()


# In[10]:


gender.head()


# In[11]:


medals.head()


# In[12]:


teams.head()


# In[49]:


athletes_by_sport = athletes.groupby(by=["Discipline"]).size()


# In[81]:


athletes_by_sport_sorted = athletes_by_sport.sort_values(ascending = False)


# In[82]:


# Distribution of Athletes across different Sports
ax = athletes_by_sport_sorted.plot(kind = 'bar',figsize = (12, 9), color='indigo', fontsize = 14)
ax.set_ylabel("Athletes Count", fontsize = 15)
ax.set_xlabel("Sports", fontsize = 15)
ax.set_title("Distribution of athletes by sport", fontsize = 22)


# In[94]:


athletes_by_country = athletes.groupby(by=["NOC"]).size()
athletes_by_country_sorted = athletes_by_country.sort_values(ascending = False)
countries_head= athletes_by_country_sorted.head(50)


# In[96]:


# Distribution of Athletes across Countries
ax_country = countries_head.plot(kind = 'bar',figsize = (16, 9), color='indigo', fontsize = 14)
ax_country.set_ylabel("Athletes Count", fontsize = 15)
ax_country.set_xlabel("Country", fontsize = 15)
ax_country.set_title("Distribution of athletes by country (TOP 50)", fontsize = 22)


# In[105]:


coaches_by_sports = coaches.groupby(by=["Discipline"]).size()
coaches_sorted = coaches_by_sports.sort_values(ascending = False) 


# In[106]:


# Distribution of Coaches across different Sport Categories
ax_coaches = coaches_sorted.plot(kind = 'bar',figsize = (12, 9), color='indigo', fontsize = 14)
ax_coaches.set_ylabel("Coaches Count", fontsize = 15)
ax_coaches.set_xlabel("Sports", fontsize = 15)
ax_coaches.set_title("Distribution of coaches by sport", fontsize = 22)


# In[108]:


coaches_by_country = coaches.groupby(by=["NOC"]).size()
coaches_sorted = coaches_by_country.sort_values(ascending = False)


# In[111]:


# Distribution of Coaches across different Countries
ax_coaches = coaches_sorted.plot(kind = 'bar',figsize = (12, 9), color='indigo', fontsize = 10)
ax_coaches.set_ylabel("Coaches Count", fontsize = 15)
ax_coaches.set_xlabel("Countries", fontsize = 15)
ax_coaches.set_title("Distribution of coaches by country", fontsize = 22)


# In[124]:





# In[ ]:




