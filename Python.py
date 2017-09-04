# Tech Month 2017 presented by SIM IT Club

##----------Python 

Part 1 - Data Preprocessing

# 1) Importing the libraries

import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
import pandas as pd

# 2) Importing the dataset

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

#Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0 ) #axis = 0 stand for column,1 stand for row
imputer = imputer.fit(X[: , 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# 3) Encoding Categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

# 4) Splitting the dataset into the Training set and Test set

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)



