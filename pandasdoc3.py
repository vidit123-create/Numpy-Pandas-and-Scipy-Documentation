#PANDAS DOCUMENTATION
#Import pandas
import pandas as pd
#Import or read csv file from the RAM using read_csv
dataset=pd.read_csv('C:\\Users\\arpit\\Desktop\\50_Startups.csv')
print(dataset)
#Data Analysis
#Datatype of the dataset
print(dataset.dtypes)
#Datatype of a particular variable
print(dataset.Administration.dtype)
#Size of the matrix
print(dataset.shape)
#length of a particular column
print(len('Administration'))
#Want to know all the unique values in dataset
print(dataset['Administration'].unique())
print(dataset['State'].unique())
#Want to sort the values in a particular variable
a=dataset.sort_values(['Administration'])
print(a)
#Want to know the maximum value and minimum value in Administration
print(dataset['Administration'].max())
print(dataset['Administration'].min())
#Want to see value of a particular coulmn from the top
print(dataset['Administration'].head(20))
#Want to see value from the bottom of a particular column
print(dataset['Administration'].tail(5))
#Want to see total index
print(dataset.index)
#Want to data on the basis of conditions
print(dataset['Marketing Spend'][dataset['State']=="New York"])
print(dataset['Administration'][(dataset['State']=="California")&(dataset['Profit']<=71498.49)])
print(dataset['Marketing Spend'][dataset['Administration']>=140000])
#Want to konw about uppercase and lowercase
print(dataset.State.apply(lambda x:x.upper()))
print(dataset.State.apply(lambda x:x.lower()))
#Want to check mean value,sd,median,contant,etc of a particular column
print(dataset['Administration'].describe())
print(dataset['R&D Spend'].describe())
#Want to use groupby variable
print(dataset.groupby(['State']).first())
print(dataset.groupby(['State']).get_group("New York"))
print(dataset.groupby(['State','Administration']).last())
print(dataset.groupby(['State']))
#Want to stored all the changes in a csv file in the form of excel
print(dataset.to_csv('Pandasdoc7.csv'))