#! usr/bin/env python3
import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import pickle

plt.style.use('ggplot')

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/ df['Adj. Low'] * 100
#df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df))) # num days to forecast out (34)

df['label'] = df[forecast_col].shift(-forecast_out) # set target to be 34 days out

X = np.array(df.drop(['label'], axis=1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:] # data to predict
X = X[:-forecast_out] # all data up to the last 34 days (slice X) 

df.dropna(inplace=True) # drop up to the point of predictions
y = np.array(df.label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

##clf = LinearRegression(n_jobs=-1)
##clf.fit(X_train, y_train)
# pickling 
# this step only needs to be done once after training
##with open('linreg.pickle', 'wb') as f:
##	pickle.dump(clf, f)

# every pass after, comment out all lines above using clf and load
pickle_in = open('linreg.pickle', 'rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name # last date with a precise prediction
last_unix = last_date.timestamp() 
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
	# add in the predictions to df 
	# next_date = date associated with forecasted prediction 
	# besides 'Forecast' col and date idx, all other cols == np.nan
	next_date = datetime.datetime.fromtimestamp(next_unix) 
	next_unix += one_day
	df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.tail())

df[forecast_col].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
