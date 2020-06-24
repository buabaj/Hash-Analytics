# importing the needed libraries
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd


# reaading the data
irisData = pd.read_csv('Iris.csv')
print(irisData)  # checking the imported dataset

# setting the dependent and independent variables as x and y
x = irisData[['SepalLengthCm', 'SepalWidthCm',
              'PetalLengthCm', 'PetalWidthCm']].values
y = irisData['Species'].values

# using LabelEncoder to preprocess the data
le = LabelEncoder()
y = le.fit_transform(y)
print(y)  # checking the preprocessed data of the Species

# splitting the dataset into training an testing data
# setting the training size to 70% and testing size to 30%
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, train_size=0.7)

# assigning the DecisionTreeClasssifier() method to the a variable
dTreeClasssifier = tree.DecisionTreeClassifier()

# using the DecisionTreeClassifier() method to fit the training data
dTreeClasssifier.fit(x_train, y_train)

# using the DecisionTreeClassifier() method to make a prediction using the x_test data
predictions = dTreeClasssifier.predict(x_test)

# printing the accuracy of the prediction
print('The Accuracy of the Decision Tree Clasifier is: ' +
      str(accuracy_score(y_test, predictions)))
