from sklearn.datasets import load_diabetes
dataset = load_diabetes()
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/house-price-prediction/master/kc_house_data.csv')
from sklearn import datasets
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target)

import numpy as np
from numpy.linalg import inv

class MultivariateLinearRegressionWithGradientDescent:
  def __init__(self, learning_rate=0.5, iterations=1000):
    self.learning_rate = learning_rate
    self.iterations = iterations
    self.weights = None
    self.bias = None

  def fit(self, X, y):
    m, n = X.shape
    self.weights = np.zeros(n)
    self.bias = 0

    for _ in range(self.iterations):
      y_pred = self.predict(X)

      # h = np.dot(X, self.weights) + self.bias
      error = y_pred - y
      dw = (2/m) * np.dot(X.T, error)
      db = (2/m) * np.sum(error)
      self.weights -= dw * self.learning_rate
      self.bias -= db * self.learning_rate

  def predict(self, X):
    return np.dot(X, self.weights) + self.bias



regression = MultivariateLinearRegressionWithGradientDescent()
regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)

print('Weights: \n', regression.weights)
print('Bias: \n', regression.bias)
print('Mean squared error: %.2f' % np.mean((y_pred - y_test) ** 2))


X_train_mul, X_test_mul = X_train[:, [0, 2]], X_test[:, [0, 2]]
regression = MultivariateLinearRegressionWithGradientDescent()
regression.fit(X_train_mul, y_train)
y_pred = regression.predict(X_test_mul)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_test_mul[:, 0], X_test_mul[:, 1], y_test, color='b')

x1_range = np.linspace(X_test_mul[:, 0].min(), X_test_mul[:, 0].max(), 100)
x2_range = np.linspace(X_test_mul[:, 1].min(), X_test_mul[:, 1].max(), 100)

x1, x2 = np.meshgrid(x1_range, x2_range)
y_pred = regression.bias + regression.weights[0]*x1 + regression.weights[1]*x2
ax.plot_surface(x1, x2, y_pred, color='r', alpha=0.5)

ax.set_xlabel('Age')
ax.set_xlim((-0.1, 0.1))
ax.xaxis.set_major_locator(LinearLocator(6))
ax.set_ylabel('BMI')
ax.set_ylim((-0.1, 0.1))
ax.yaxis.set_major_locator(LinearLocator(6))
ax.set_zlabel('Target Variable')
plt.title('Linear Regression with Two Variables')

plt.show()