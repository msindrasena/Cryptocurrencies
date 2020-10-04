#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import hvplot.pandas
import plotly.express as px


# In[2]:


# Read in the file
file_path = "crypto_data.csv"
crypto_df = pd.read_csv(file_path)
crypto_df.head()


# In[3]:


# look at what data types you are working with
crypto_df.dtypes


# In[4]:


# Remove cryptocurrencies that aren't trading
crypto_df.drop(crypto_df[crypto_df['IsTrading'] == False].index, inplace=True)
crypto_df.head()


# In[5]:


# Remove all the cryptocurrencies that dont have an algorithm defined
crypto_df = crypto_df[crypto_df.Algorithm != '']


# In[6]:


# Remove the IsTrading column
crypto_df.drop(columns=['IsTrading'], inplace=True)
crypto_df.head()


# In[7]:


# (null values)
# Use isnull method to check for missing values
# Loop through each column, check if there are null values, sum them up, and print readable total

for column in crypto_df.columns:
    print(f"Column {column} has {crypto_df[column].isnull().sum()} nullvalues")


# In[8]:


# Remove all cryptocurrencies with at least one null value
crypto_df = crypto_df.dropna()
crypto_df.head()


# In[9]:


# Remove all cryptocurrencies without coins mined
crypto_df = crypto_df[crypto_df['TotalCoinsMined']>0]
crypto_df.head()


# In[10]:


# Store the names of all cryptocurrencies on a DataFramed named coins_name
coins_name = pd.DataFrame([crypto_df.CoinName]).transpose()
coins_name.head()


# In[11]:


# use the crypto_df.index as the index for this new DataFrame.
coins_name.set_index(crypto_df['Unnamed: 0'])


# In[12]:


# Remove the CoinName column.
crypto_df.drop(columns=["CoinName"], inplace=True)
crypto_df.head()


# In[13]:


# Create dummies variables for all of the text features, and store the resulting data on a DataFrame named X.
X = pd.get_dummies(crypto_df, columns=['Algorithm', 'ProofType'])
X.head()


# In[18]:


# Standardize the data
X_scaled = StandardScaler().fit_transform(X)
print(X_scaled[:5])


# In[ ]:




