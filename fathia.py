#!/usr/bin/env python
# coding: utf-8

# In[2]:


#inital list of lists
import pandas as pd
data = [['ayo',10] ,['ade' ,15] , ['checker',14]]

# create the ponds DataFrame from the list and addingb column headers
df = pd.DataFrame (data,columns = ['name','age'])

#print dataframe
print(df)


# In[4]:


# create the DataFrame from the dictionary of array list
df = pd.DataFrame(data)

# print dataframe
df


# In[11]:


dict_data = {'State':['Abia','Adamawa', 'Lagos','osun','river'],
             'Capital':['Umuahia', 'yola', 'Ikeja' , 'Osogbo' , 'portharcourt'],
             'puplation':[6974,457,345,8754,3426],
             'Area':[5437,4328,9876,98063,5437]}
df = pd.DataFrame(dict_data)
df


# In[14]:


csv_df= pd.read_csv('Desktop/ADEBAYO FATHIA.csv')
print(csv_df)


# In[ ]:




