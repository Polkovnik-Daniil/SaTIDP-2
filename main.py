import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns

data = pd.read_csv("data/german_credit_data.csv")
data.info()
print(data[data.eq(0)].count())

cols = data.columns[:]
#определяем цвета
#красный - пропущенные данные
colours = ['#eeeeee','#00ff00']

sns.heatmap(data[cols].isnull(), cmap=sns.color_palette(colours))
plt.show()
data.fillna(data.mean())