from sklearn.datasets import load_diabetes
dataset = load_diabetes()
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/house-price-prediction/master/kc_house_data.csv')
# df.head()
from sklearn import datasets
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target)

import numpy as np
from numpy.linalg import inv

class MultivariateLinearRegression:
  def __init__(self):
    self.weights = None

  def fit(self, X, y):
    # Please refer to page 5 of the alecture (AIP_10_Linear Regression and k-NN (A)).
    print(X.shape, y.shape)
    self.weights = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    pass

  def predict(self, X):
    return X.dot(self.weights)


regression = MultivariateLinearRegression()
regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)

print('Weights: \n', regression.weights)
print('Mean squared error: %.2f' % np.mean((y_pred - y_test) ** 2))