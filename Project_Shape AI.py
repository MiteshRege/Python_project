#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


pwd


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("Titanic\\train.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


print(df)


# In[8]:


df=pd.read_csv("Titanic\\train.csv",usecols=["PassengerId","Survived","Pclass"])
df.head()


# In[2]:


df.info()


# In[12]:


df=pd.read_csv("Titanic\\train.csv")
df.describe()


# In[13]:


df.info()


# In[14]:


df.dtypes


# In[15]:


df.sort_values("Fare")


# In[16]:


df.sort_values("Fare").head(3)


# In[17]:


# fare in desrnding
df.sort_values("Fare",ascending=False).head(10)


# In[18]:


df["Sex"].value_counts()


# In[19]:


df.nunique()


# In[20]:


df["Embarked"] = df["Embarked"].astype("category")
df["Embarked"].dtype
df["Embarked"] == "C" 


# In[21]:


df_fare_mask = df["Fare"] < 100
df_sex_mask = df["Sex"] == "female"
df[df_fare_mask & df_sex_mask]


# In[22]:


df_fare_mask2 = df["Fare"] > 500
df_age_mask = df["Age"] > 70
df[df_fare_mask2 | df_age_mask]


# In[23]:


df.isnull().sum()


# In[24]:


import matplotlib.pyplot as plt
ax= df["Survived"].value_counts().plot(kind='bar',color=['k','g'])
ax.set_xticklabels(["dead","survived"])
ax.set(xlabel="Casuality information")
ax.set(ylabel='Number of passengers')
plt.show()


# In[25]:


ax= df[df["Sex"]=='male']["Survived"].value_counts().plot(kind='bar',color=['r','g'])
ax.set_xticklabels(["dead","survived"])
ax.set(ylabel='Number of passengers')
plt.show()


# In[30]:


ax= df[df["Sex"]=='female']["Survived"].value_counts().plot(kind='bar',color=['k','b'])
ax.set_xticklabels(["dead","survived"])
ax.set(ylabel='Number of passengers')
plt.show()


# In[31]:





# In[3]:



import matplotlib.pyplot as plt
ax= df["Survived"].value_counts().plot(kind='bar',color=['k','g'])
ax.set_xticklabels(["dead","survived"])
ax.set(xlabel="Casuality information")
ax.set(ylabel='Number of passengers')
plt.show()


# In[1]:


'''Using Titanic dataset find out
information about how many male survived who had cabin and age is less than 50.
Also show graphical representation of male and female survived and dead in the
tragedy.  '''

import pandas as pd
df=pd.read_csv("Titanic\\train.csv")
df_fare_mask2 = df["Survived"] == 1
df_sex_mask = df["Sex"] == "male"
df_cabin =df['Cabin'].notnull()
df_age_mask = df["Age"] < 50
df[df_fare_mask2 & df_sex_mask & df_cabin & df_age_mask]


# In[1]:


import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


# In[ ]:




