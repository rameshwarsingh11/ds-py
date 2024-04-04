#%pip install seaborn
import seaborn as sns
import numpy as np
# %matplotlib inline

tips = sns.load_dataset('tips')
tips.head()

sns.distplot(tips['total_bill'],kde=False, bins = 30)
sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')

#Pairplots() maps every possible combination
sns.pairplot(tips, hue='sex')

#Rugplot() creates a dashplot
sns.rugplot(tips['total_bill'])

sns.displot(tips['total_bill'], kde=False)

#Kernel Density Estimation(kde) plot
sns.kdeplot(tips['total_bill'])

sns.barplot(x='sex',y='total_bill', data=tips,estimator=np.std)

sns.countplot(x='sex',data=tips)

sns.boxplot(x='day',y='total_bill', data=tips, hue ='smoker')

sns.violinplot(x='day', y='total_bill', data=tips, hue='sex')

sns.stripplot(x='day',y='total_bill',data=tips, jitter=True, hue= 'sex')

#sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips)

#Factorplot is replaced by catplot in Seaborn library.
sns.catplot(x='day',y='total_bill',data=tips, kind='bar')

#Matrix plot
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()
flights.head()
tc=tips.corr()
sns.heatmap(tc, annot= True)

fp =flights.pivot_table(index= 'month', columns = 'year', values= 'passengers')

sns.heatmap(fp,cmap='magma',linecolor='white', linewidths=1)

sns.clustermap(fp, cmap='coolwarm', standard_scale=1)

#Grid plots
iris = sns.load_dataset('iris')
iris.head()
iris['species'].unique()
sns.pairplot(iris)

g= sns.PairGrid(iris)
g.map(plt.scatter)

g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

tips= sns.load_dataset('tips')
tips.head()

g = sns.FacetGrid(data= tips, col='time',row='smoker')

g.map(sns.distplot,'total_bill')

g.map(plt.scatter, 'total_bill', 'tip')

#Styles and mixing matplot with seaborn plots
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)
sns.despine(left = True, bottom= True)

plt.figure(figsize=(12,3))
sns.countplot(x='sex', data=tips)

sns.set_context('poster')
sns.countplot(x='sex', data=tips)

sns.lmplot(x='total_bill', y = 'tip', data =tips, hue= 'sex', palette='seismic')

#Test on titanic data set
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()
sns.jointplot(x='fare', y='age', data= titanic)

sns.distplot(titanic['fare'], kde=False, color='red', bins =30
             
sns.boxplot(x='class', y='age', data=titanic, palette = 'rainbow')

sns.swarmplot(x='class', y='age', data=titanic, palette = 'Set2')

sns.countplot(x='sex', data=titanic)

sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('title.corr()')

g=sns.FacetGrid(data =titanic, col= 'sex')
g.map(plt.hist,'age')





