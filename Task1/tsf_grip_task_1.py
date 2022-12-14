# -*- coding: utf-8 -*-
"""TSF GRIP Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BDp_8KDqA27f4KnzIPIH-JNk3bgLDjEz

#**The Sparks Foundation GRIP Internship Task 1**

##**Prediction using Supervised Machine Learning**
**(Level - Beginner)**

Author: **Arnab Chakraborty** (*Data Science and Business Analytics Intern at The Sparks Foundation*) 

LinkedIn Profile: https://www.linkedin.com/in/arnab-chakraborty27/

# **Problem Statement**

Predict the percentage obtained by a student based on the number of hours studied by the student per day. This is a simple linear regression problem as it involves only 2 variables.

What will be the predicted percentage if a student studies 9.25 hours/day?

Dataset: http://bit.ly/w-data

**Importing Necessary Libraries**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score

"""**Importing the Dataset**"""

data = pd.read_csv('http://bit.ly/w-data')

"""**Previewing the Data**"""

data.head()

data.describe()

data.shape

"""**Visualizing the Data**"""

plt.scatter(data['Hours'], data['Scores'])
plt.title('Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Score Obtained')
plt.show()

"""**Dividing the Data**

- x -> Stores Number of Hours studied per day
- y -> Stores Percentage obtained 
"""

x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
print(x)
print(y)

"""**Splitting the Data**

`train_test_split()` splits the data into Training and Test sets for buliding the Regressor model.
"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

"""Creating the `LinearRegressor` model and training the model using the training set."""

regressor = LinearRegression()
regressor.fit(x_train, y_train)

"""Visualizing the values of `No. of Hours` using a Scatter Plot and plotting a best-fit line."""

line = regressor.coef_ * x  + regressor.intercept_
plt.scatter(x,y)
plt.plot(x, line, color='red')
plt.show()

"""Testing the `LinearRegressor` model using the Test data set and displaying the predicted results"""

y_pred = regressor.predict(x_test)
print(y_pred)

"""Visualizing the predictions made by the `LinearRegressor` model with input as the ***training dataset*** using a Scatter Plot and plotting a best-fit line."""

plt.scatter(x_train, y_train, color='green')
plt.plot(x_train, regressor.predict(x_train), color='violet')
plt.title('Hours vs Scores (Training Dataset)')
plt.xlabel('Hours Studied')
plt.ylabel('Score Obtained')
plt.show()

"""Visualizing the predictions made by the `LinearRegressor` model with input as the ***test dataset*** using a Scatter Plot and plotting a best-fit line."""

plt.scatter(x_test, y_test, color='orange')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Hours vs Scores (Test Dataset)')
plt.xlabel('Hours Studied')
plt.ylabel('Score Obtained')
plt.show()

"""**Comparing the Actual Result and Predicted Result**"""

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df

"""**Predicting the Percentage** if No. of Hours studied is `9.25 hours/day`"""

test_case = np.array(9.25)
test_case = test_case.reshape(-1, 1)
pred = regressor.predict(test_case)
print('If the student studies for 9.25 hours per day, the predicted score obtained is {}%.'.format(pred[0]))

"""Finding out the **error in the prediction**"""

print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))
print('The R-Square of the model is: ', r2_score(y_test, y_pred))