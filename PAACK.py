#!/usr/bin/env python
# coding: utf-8

# In[139]:


#1- In this case I sort them through a for loop and converting the list into integers


# In[140]:


import numpy as np
import pandas as pd


# In[141]:


list = ['5', '8', '1', '2', '10']


# In[142]:


list = [int(x) for x in list]


# In[143]:


list.sort()
list


# In[144]:


#2- In this case I also use a for loop however I sum the different columns separately


# In[145]:


drivers = pd.read_csv('drivers_table.csv')


# In[146]:


drivers.head()


# In[147]:


drivers.info()


# In[148]:


print("Capital Letters: ", sum(1 for c in drivers['vehicle'] if c.isupper()))


# In[149]:


drivers['vehicle'].str.count(r'[A-Z]').sum() + drivers['invoice_details'].str.count(r'[A-Z]').sum() + drivers['vehicle'].str.count(r'[A-Z]').sum()


# In[153]:


#3- the below code is an example using one of my pcs drive, listdir allows us to do that


# In[154]:


from os import listdir


# In[155]:


arr = listdir('D:\FRAN\JOB HUNTING\PAACK\Data')


# In[156]:


arr


# In[157]:


import glob
print(glob.glob("D:\FRAN/*.rns"))


# In[160]:


#4- this is the queston I have struggled the most :(, I have ended up having number of orders per driver per day through joining both datasets, converting the date column to date, separating day through a for look an then counting


# In[161]:


import numpy as np
import pandas as pd


# In[162]:


drivers = pd.read_csv('drivers_table.csv')
orders = pd.read_csv('orders_table.csv')


# In[163]:


drivers.head(3)


# In[164]:


orders.head(3)


# In[165]:


merged = pd.merge(drivers,orders, how='inner', left_on='id', right_on='driver_id')


# In[166]:


merged.head(2)


# In[167]:


merged[['driver_id','driver','Paack order number','Attempted time']]


# In[168]:


prod = merged[['driver_id','driver','Paack order number','Attempted time']]


# In[169]:


prod.head(2)


# In[170]:


prod.info()


# In[174]:


prod['Attempted time']=pd.to_datetime(prod['Attempted time'])


# In[175]:


prod.info()


# In[181]:


prod.head(10)


# In[182]:


list_days=[]
for i in range(prod.shape[0]):
    list_days.append(prod['Attempted time'][i].month)


# In[183]:


list_days


# In[184]:


prod['Day']=list_days


# In[185]:


prod.head(4)


# In[195]:


prod2 = prod.groupby(['driver','Day']).count()


# In[199]:


prod2.drop(['driver_id','Attempted time'], axis=1)


# In[200]:


#5- here I am joining two of the files provided and at the same time querying the driver id to be between 1 and 10


# In[201]:


import numpy as np
import pandas as pd


# In[202]:


drivers = pd.read_csv('drivers_table.csv')
orders = pd.read_csv('orders_table.csv')


# In[ ]:


df.merge(probes, left_on='Chromosome', right_on='Chrom').query('Start < Position < End')


# In[208]:


merged = pd.merge(drivers,orders, how='inner', left_on='id', right_on='driver_id').query('1<id_x<10')


# In[209]:


merged

