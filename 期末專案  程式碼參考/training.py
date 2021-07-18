import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

import tensorflow.keras as keras
from tensorflow.keras.models import load_model
 

cwd = os.getcwd()
df = pd.read_csv('C:\\tsmc_predict\台積電近2年股價爬蟲.csv', index_col=['Date'])
df = df[['Open', 'Low', 'High', 'Volume', 'Close']]
print("有", len(df), "天")

df['Return'] = df['Close'].shift(-1, axis = 0)
df = df.iloc[:-1,:]

ss = StandardScaler()
df_scaled = ss.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, index=df.index, columns=df.columns)
df_scaled['Return'] = df['Return']

n = 3
featured_names = list(df_scaled.drop('Return', axis=1).columns)
x = []
y = []
indexes = []
df_scaled_x = df_scaled[featured_names]

for i in range(0, (len(df_scaled)-n) -1):
    x.append(df_scaled_x.iloc[i:i+n].values)
    y.append(df_scaled['Return'].iloc[i+n])
    indexes.append(df_scaled.index[i+n-1])

import numpy as np
X = np.array(x)
Y = np.array(y)


model = keras.models.Sequential()

model.add(keras.layers.LSTM(100, return_sequences=True, input_shape=X[0].shape))
model.add(keras.layers.LSTM(100))

model.add(keras.layers.Dense(8))
model.add(keras.layers.Dense(1, kernel_initializer='uniform',activation='linear'))

adam = keras.optimizers.Adam(0.0006)
model.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

import datetime

trainset_indexes = []

limit_date1 = datetime.datetime(2021,6,30)
limit_date2 = datetime.datetime(2021,6,1)

for i in indexes:
    if (datetime.datetime.strptime(i, "%Y-%m-%d") > limit_date1 or datetime.datetime.strptime(i, "%Y-%m-%d") < limit_date2):
        trainset_indexes.append(False)
    else:
        trainset_indexes.append(True)

X_train = X[trainset_indexes]
Y_train = Y[trainset_indexes]

model.save('stock.h5')
del model