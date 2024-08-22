# -*- coding: utf-8 -*-
"""CIE2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_C47GjVUNIO916WMjyRIhWuzva2FPIHA
"""

import pandas as pd
data=pd.read_csv('/content/titanic.csv')
print(data)

data.describe()

data.head(5)

data.shape

data.info()

data.isnull().sum()

data['Pclass'].unique()

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
mean1=np.mean(data['Age'])
median1=np.median(data['Age'])
mode1=stats.mode(data['Age'],keepdims=True).mode[0]
mean2=np.mean(data['Fare'])
median2=np.median(data['Fare'])
mode2=stats.mode(data['Age'],keepdims=True).mode[0]
print("central tendency")
print("mean age:", mean1)
print("median age:", median1)
print("mode age:", mode1)
print("mean fare:", mean2)
print("median fare:", median2)
print("mode fare:", mode2)

import matplotlib.pyplot as plt
import pandas as pd
filtered_data = data[(data['Survived'].isin([0, 1])) & (data['Pclass'].isin([1, 2, 3]))]
counts = filtered_data.groupby(['Survived', 'Pclass'])['Survived'].count().unstack()
counts.plot(kind='bar', color=['red', 'pink','yellow'])
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Number of Passengers')
plt.title('Total Numbers of Survived and Not Survived by Class')
plt.legend(title='Pclass')
plt.show()

import pandas as pd
data=pd.read_csv('/content/titanic.csv')
print(data.head())
null_values=data.isnull().sum()
titanic_filled_data=data.fillna(data.mean(numeric_only=True))
null_values,titanic_filled_data.head()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
mean=np.mean(data['Age'])
std=np.std(data['Age'])
print("mean:",mean)
print("std of data:",std)
threshold=3
outlier=[]
for i in data['Age']:
  z_sc=(i-mean)/std
  if z_sc>threshold:
    outlier.append(i)
print("outliers in the dataset is :",outlier)
sns.boxplot(data['Age'])
plt.title("boxplot")
plt.show()

