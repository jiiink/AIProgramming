from sklearn.datasets import load_diabetes
dataset = load_diabetes()
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/house-price-prediction/master/kc_house_data.csv')
# df.head()



import numpy as np

class UnivariateLinearRegression:
  def __init__(self):
    self.w0 = 0
    self.w1 = 0

  def fit(self, X, y):
    # Please refer to page 4 of the lecture (AIP_10_Linear Regression and k-NN (A)).
    n = len(y)
    self.w1 = (n * (X @ y) - sum(X) + sum(y)) / (n * sum(X**2) - sum(X)**2)
    self.w0 = (sum(y) - self.w1 * sum(X)) / n
    

  def predict(self, X):
    return self.w0 + self.w1 * X

from sklearn import datasets
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target)
X_train_uni, X_test_uni = X_train[:, 2], X_test[:, 2]

uni_regression = UnivariateLinearRegression()
uni_regression.fit(X_train_uni, y_train)
y_pred = uni_regression.predict(X_test_uni)

print('Coefficients: \n', uni_regression.w1)
print('Intercept: \n', uni_regression.w0)
print('Mean squared error: %.2f' % np.mean((y_pred - y_test) ** 2))

import matplotlib.pyplot as plt

plt.scatter(X_test_uni, y_test, color='red', label='Actual')
sorted_idx = np.argsort(X_test_uni)
plt.plot(X_test_uni[sorted_idx], y_pred[sorted_idx], color='blue', linewidth=3, label='Predicted (Univariate)')
plt.xlabel('BMI')
plt.ylabel('Diabetes progression') # 1년 후 질병 진행의 정량적 측정
plt.title('Univariate Linear Regression')
plt.legend()
plt.show()