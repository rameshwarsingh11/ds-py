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