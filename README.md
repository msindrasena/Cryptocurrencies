# Cryptocurrencies

This project was completed to help an Accounting firm the ability to offer new cryptocurrencies investment portfolio for its customers. We are asked to present a report including what cryptocurrencies are in the market & how they can be grouped toward creating a classification for development. We have used unsupervised learning as there was no known output. 

Data PreProcessing Phase:

  Removed all cryptocurrencies that aren’t trading.
  Removed all cryptocurrencies that don’t have an algorithm defined.
  Removed the IsTrading column.
  Removed all cryptocurrencies with at least one null value.
  Removed all cryptocurrencies without coins mined.
  Stored the names of all cryptocurrencies on a DataFramed named coins_name, and used the crypto_df.index as the index for this new DataFrame.
  Removed the CoinName column.
  Create dummies variables for all of the text features, and stored the resulting data on a DataFrame named X.
  Use the StandardScaler from sklearn to standardize all of the data from the X DataFrame. 
  
  The Ending Data Frame:
  
  [!https://github.com/msindrasena/Cryptocurrencies/blob/master/challenge18.PNG]
  
After the data Preprocessing phase, we reduced the data dimensions using PCA, clustered cryptocurrencies using K-means with an elbow curve and visualized the results with a 3D scatter plot. 
  
