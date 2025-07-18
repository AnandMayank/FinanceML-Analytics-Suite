# -*- coding: utf-8 -*-
"""LSTM_closePricePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zAXMJKmUantaCZ7oEDDqlMiuW3RoPtGv
"""



#Import the libraries
import math
import pandas_datareader as web
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Get the stort data
#df = web.DataReader('AAPL', data_source='yahoo', start='2017-01-01', end ='2021-12-20')
stock = 'MSFT'
df = yf.download(stock, '2017-01-01', '2025-01-19')
#Show the data
df

#Check the number of rows and columns in the data set
df.shape

#Visualize the closing price
plt.figure(figsize=(15,6))
plt.title('MSFT Close price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()

#Create a dataframe with close column.
data = df[['Close']]
#Convert the dataframe to numpy array
dataset = data.values
#Get the number of rows to train the model
training_data_len = math.ceil(len(dataset) *0.8)
training_data_len

#Scale the data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)
#Show the scaled data
scaled_data

#Create the scaled training dataset
train_data = scaled_data[0:training_data_len, :]
#Split the dataset into x_trian, y_trian data set
x_train = []
y_train = []

for i in range(60, training_data_len):
  x_train.append(train_data[i-60:i, :])
  y_train.append(train_data[i, :])
  if i <= 60:
    print(x_train)
    print(y_train)

#Convert the x_trian and y_train data set into numpy array.
x_train, y_train = np.array(x_train), np.array(y_train)
#print(y_train)
x_train.shape

y_train.shape

#Reshape the data for LSTM model
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_train.shape

#Build the LSTM Model
model = Sequential()
model.add(LSTM(50, activation='tanh', return_sequences= True, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(LSTM(50, activation='tanh', return_sequences=False))
#model.add(Dropout(0.2))
model.add(Dense(25))
model.add(Dense(1))

#Compile the model
model.compile(optimizer='Adam', loss='mean_squared_error')

#Train the model
model.fit(x_train, y_train, epochs=1, batch_size=1, validation_split=0.1)

#Create the test data set
test_data = scaled_data[training_data_len-60:, :]
#Create the x_test(Features to perdict y_test) , y_test(Actual value) data set
x_test = []
#y_test = scaled_data[training_data_len: , :]
y_test = dataset[training_data_len:, :]
for i in range(60, len(test_data)):
  x_test.append(test_data[i-60:i, :])

# Convert x_test into numpy array
x_test = np.array(x_test)
x_test.shape

#Get the model prediction price
predictions = model.predict(x_test)

predictions = scaler.inverse_transform(predictions)
#print(predictions)
#y_test = scaler.inverse_transform(y_test)
y_test = np.reshape(y_test, (y_test.shape[0], 1))
#type(predictions)
print(y_test)

print(predictions)

#Check the model accuracy using root mean squared error
RMSE = np.sqrt(np.mean((predictions - y_test)**2))
RMSE

#Plot the data
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
#Visualize the data
plt.figure(figsize=(15,6))
plt.title('Model Price Prediction')
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Close Price in ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Prediction'], loc='upper left')
plt.show()