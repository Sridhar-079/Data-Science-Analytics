# WEEK 4 – DATA VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y)
plt.show()

data = [10,20,20,30,40,40,40]
sns.histplot(data)
plt.show()

df = sns.load_dataset("iris")
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.show()

sns.pairplot(df, hue="species")
plt.show()
