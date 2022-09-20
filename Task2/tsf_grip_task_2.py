# -*- coding: utf-8 -*-
"""TSF GRIP Task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R4GfJ8ZsRIc3YZxlPRqAyE5iajb1TfGJ

#**The Sparks Foundation GRIP Internship Task 2**

##**Prediction using Unsupervised Machine Learning**
**(Level - Beginner)**

Author: **Arnab Chakraborty** (*Data Science and Business Analytics Intern at The Sparks Foundation*) 

LinkedIn Profile: https://www.linkedin.com/in/arnab-chakraborty27/

# **Problem Statement**

From the given `Iris Dataset`, predict the Optimum Number of Clusters and represent them visually.

Dataset: https://bit.ly/3kXTdox

**Importing Necessary Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
# %matplotlib inline

"""**Importing the IRIS Dataset**"""

df = pd.read_csv('/content/Iris.csv', index_col=False)

"""**Exploring The Data**"""

df.set_index('Id', inplace=True)
df.head()

df.Species.value_counts()

df.info()

df.describe()

df.dtypes.value_counts()

df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].hist()

"""**Visualizing the Data**"""

fig = plt.figure(1, figsize=(8,6))
sns.scatterplot(x='SepalLengthCm', y ='SepalWidthCm', data=df, label='Sepal')
sns.scatterplot(x='PetalLengthCm', y ='PetalWidthCm', data=df, label='Petal')
plt.xlabel('Length(cm)')
plt.ylabel('Width(cm)')

df.corr()

fig = plt.figure(1, figsize=(8, 6))
sns.heatmap(df.corr(),cmap="Blues", linewidth=0.3, cbar_kws={"shrink":.8})

sns.pairplot(df, hue='Species')

x = df.iloc[:, [0, 1, 2, 3]].values
sse = []
k_rng = range(1,11)
for k in k_rng:
    km = KMeans(n_clusters=k, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(x)
    sse.append(km.inertia_)

fig = plt.figure(1, figsize=(8, 6))
plt.plot(k_rng, sse)
plt.xlabel('k')
plt.ylabel('Sum of Squared Error')

"""**Applying KMeans Clustering**"""

km = KMeans(n_clusters=3)
km_pred = km.fit_predict(x)
km_pred

km.cluster_centers_

df['cluster'] = km_pred
fig = plt.figure(1, figsize=(8, 6))
df['cluster'].value_counts().plot(kind='bar')
plt.legend()

df.head()

"""**Visualizing Clusters and their Centroids**"""

fig = plt.figure(1, figsize=(11, 7))
plt.scatter(x[km_pred == 0, 0], x[km_pred == 0, 1], alpha=0.7, label = 'Iris-setosa', color='blue')
plt.scatter(x[km_pred == 1, 0], x[km_pred == 1, 1], alpha=0.7, label = 'Iris-versicolour', color='green')
plt.scatter(x[km_pred == 2, 0], x[km_pred == 2, 1], alpha=0.7, label = 'Iris-virginica', color='red')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:,1], s = 100, marker='+', c='black', label = 'Centroids')
plt.legend()

from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
plt.cla()
ax.set_xlabel('Iris-setosa')
ax.set_ylabel('Iris-versicolour')
ax.set_zlabel('Iris-virginica')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], x[:,3], c= km_pred.astype(np.float))

"""# **We can conclude that the optimum number of Clusters for the Iris dataset is `3`**"""