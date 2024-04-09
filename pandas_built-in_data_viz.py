import numpy as np
import pandas as pd
import seaborn as sns
#%matplotlib inline

df1 = pd.read_csv('./sample_data/df1', index_col=0)
df1.head().hist()

df2 = pd.read_csv('./sample_data/df2')
df2.head()

df1['A'].hist(bins=30)

df1['A'].plot(kind='hist', bins =40)

df1['A'].plot.hist()

df2.plot.area(alpha=0.5)

df2.plot.bar()

df2.plot.bar(stacked=True)

df2.plot.hist()

df2.plot.hist(bins=30)

df1.plot.line()

df2.plot.line(figsize=(12,4),lw=1)

df1.plot.scatter(x='A', y='B', c= 'C')

df1.plot.scatter(x='A', y='B', s= df1['C']*20)

df2.plot.box()

df = pd.DataFrame(np.random.randn(1000,2),columns= ['a','b'])
df.head()

df.plot.hexbin(x='a',y='b', gridsize= 20, cmap='Paired')

df2['a'].plot.kde()

df2['b'].plot.density()

df2.plot.density()

f = plt.figure()
df3.loc[0:30].plot.area(alpha=0.4)
plt.legend(loc='center left', bbox_to_anchor=(1.0,0.5))
plt.show()