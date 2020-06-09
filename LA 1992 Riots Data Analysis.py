#!/usr/bin/env python
# coding: utf-8

# # Importing and Loading Dataset
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data_df = pd.read_csv('deaths.csv')


# In[3]:


data_df.head()


# In[4]:


data_df.shape


# ### Cleaning the dataset

# In[5]:


#checking for the missing data in the dataset
#checking for null values present in the data set
data_df.isnull().sum()


# In[6]:


#Filling the null values

data_df['Solved*'].fillna(('Unsolved'),inplace=True)


# In[7]:


data_df['lat'].fillna((data_df['lat'].mean()),inplace=True)


# In[8]:


data_df['lon'].fillna((data_df['lon'].mean()),inplace=True)


# In[9]:


data_df.drop('URL',axis=1,inplace=True)


# In[10]:


data_df.isnull().sum()


# In[11]:


data_df.rename(columns={'Solved*':'Solved'},inplace=True)


# In[12]:


data_df.head(10)


# In[13]:


data_df.info()


# # Exploratry Data Analysis

# In[14]:


data_df['first'].value_counts()


# ### Number of Solved and Unsolved Cases

# In[15]:


#making the dataframe
cases_status=data_df.loc[:,'Solved']


# In[16]:


cases_status.head()


# In[17]:


#counting the number of values for each unique element of coloums solved
countcases_df=data_df['Solved'].value_counts()


# In[18]:


countcases_df.head()


# In[19]:


#Visualisation of cases 
plt.ylabel('Number of cases')
plt.title('Status of the cases')
data_df['Solved'].value_counts().plot(kind='bar')


# ### People of various races killed

# In[20]:


#making the dataframe
people_race=data_df.loc[:,'Race']


# In[21]:


#showing the result
people_race.head(63)


# In[22]:


#counting the number of people of various races killed
count_people_race=data_df['Race'].value_counts()
count_people_race


# In[23]:


#Now since we can see that we have two black and two latino and two white so we will include them as same in their category


# In[24]:


plt.ylabel('Number of people Dead')
plt.xlabel('Race')
plt.title('People of various races deceased')
count_people_race.plot(kind='bar')


# In[25]:


#Deaths based on gender
data_df['Gender'].value_counts()


# In[26]:


#visualisation
plt.xlabel('Gender')
plt.ylabel('People killed')
plt.title('Deaths based on gender')
data_df['Gender'].value_counts().plot(kind='bar')


# ## Deaths in various regions

# In[27]:


deaths_df=data_df[['first','lat','lon']]
deaths_df


# In[28]:


plt.scatter(x=deaths_df['lon'], y=deaths_df['lat'],alpha=0.8)
plt.show()


# In[29]:


#How were they killed?

deathMeans= data_df['status'].value_counts()
deathMeans


# In[30]:


deathMeans.plot(kind='barh',color='r')


# In[31]:


new_df=data_df[['status','lon','lat']]
new_df


# In[32]
import seaborn as sns
ax=sns.scatterplot(x="lon",y="lat",hue="status",data=new_df)
