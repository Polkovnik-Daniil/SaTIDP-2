import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns

df = pd.read_csv("data/ds_salaries.csv")
df.info()
print(df[df.eq(0)].count())

cols = df.columns[:]
colors = ['#eeeeee', '#00ff00']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colors))

df.isnull().any()

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

df = df.drop(["Checking account"], axis=1)
df = df.drop(["Purpose"], axis=1)
df.head()

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


df["Saving accounts"]=df["Saving accounts"].fillna("quite little")
df["Saving accounts"]


for col in df.columns:
    pct_missing = df[col].isnull().sum()
    print('{} - {}'.format(col, round(pct_missing)))

sns.histplot(data=df["Saving accounts"], log_scale=(False, True), bins=30)


start_df = pd.read_csv('D:\Program Files\Python\My CSV\german_credit_data.csv')
sns.histplot(data=start_df["Saving accounts"], log_scale=(False, True), bins=30)



# функция map() используется для применения функции к каждому элементу итерируемого объекта
df["Saving accounts"]=df["Saving accounts"].map({"quite little": 0, "little": 1, "moderate": 2,"rich": 3, "quite rich": 4})
df.head()


df["Sex"]=df["Sex"].map({"male": 1, "female": 0})
df["Housing"]=df["Housing"].map({"own": 0, "free": 1, "rent": 2})
df.head()

sns.boxplot(df['Age'])


df['Age'].describe()


print(np.where(df['Age']>65))
df = df.apply(lambda x: x[(x>df.loc[0,x.name]) &
                                    (x < df.loc[3,x.name])], axis=0)

df.info()

df = pd.DataFrame(df)

df.to_csv('german_credit_data_clear.csv', index=False)