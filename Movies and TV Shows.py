#!/usr/bin/env python
# coding: utf-8

# # <centre>Movies and TV Shows</centre>

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


df= pd.read_csv(r"C:\Users\R A H U L\Desktop\movies and tv shows.csv")


# # Displaying the dataframe

# In[3]:


df


# # TOP 5 Records

# In[4]:


df.head()


# # Displaying all the field names

# In[5]:


df.columns


# # Displaying the shape

# In[6]:


df.shape


# # Displaying the information about the DataFrame

# In[7]:


df.info()


# # Checking for null values

# In[8]:


df.isnull()


# # Sum of null values in  every fields

# In[9]:


df.isnull().sum()


# # Percentage of null values

# In[10]:


df.isnull().sum()/(len(df))*100


# # Number of movies released in various years.

# In[11]:


df.release_year.value_counts() 


# # Displaying the countries by the total number of users.

# In[12]:


df.country.value_counts()


# In[13]:


x= df.country.value_counts().head(20)
plt.figure(figsize=(10,10))
sns.set_style("whitegrid")   #set style to whitegrid
ax= sns.barplot(x.values,x.index)   #using bar for visualization
ax.set_xlabel("Number of content")
ax.set_ylabel("Number of country")


# # Displaying the count of ratings.

# In[14]:


df.rating.value_counts()


# In[15]:


plt.figure(figsize=(16,6))
sns.countplot(x= "rating",data= df)


# In[16]:


x= df.rating.value_counts()
plt.figure(figsize=(10,10))

labels= list(x.index)
plt.pie(x.values,labels= labels,autopct= "%1.1f%%")
plt.show()


# # Distribution of Movies and TV Shows

# In[17]:


plt.figure(figsize=(9,9))

x= df.type.value_counts()
sns.countplot(x= "type",data= df)


# In[18]:


plt.figure(figsize=(8,10))

label= ["Movies","Tv Shows"]

plt.pie(x.values, labels= label ,autopct= "%1.1f%%") # visualizing using pie
plt.show()   


# # Content releases over the years

# In[19]:



x= df.release_year.value_counts().head(16)
plt.figure(figsize=(16,6))
plt.xlabel("Year")

sns.lineplot(x=x.index ,y= x.values)

