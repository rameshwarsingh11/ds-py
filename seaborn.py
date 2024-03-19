#%pip install seaborn
import seaborn as sns
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