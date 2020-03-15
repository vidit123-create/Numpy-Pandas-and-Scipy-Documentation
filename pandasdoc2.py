import pandas as pd
print(pd.__version__)
#Import csv file from RAM or read data from RAM
df3=pd.read_csv('C:\\Users\\arpit\\Downloads\\K_Nearest_Neighbors\\Social_Network_Ads.csv')
#Data Analysis1
print(df3)
print(df3.Gender.dtype)
print(df3.dtypes)
print(df3.shape)
print(df3.describe())
print(df3['Age'].unique())
print(df3['EstimatedSalary'].max())
print(df3['EstimatedSalary'].min())
print(df3.sort_values(['Purchased']))
#df3['EstimatedSalary']=df3.EstimatedSalary.apply(lambda y:y.upper())
#print(df3['EstimatedSalary'])
print(df3.head(10))
print(df3.tail(10))
#Using of groupby function
print(df3.groupby(['Gender']).first())
print(df3.groupby(['Gender']).last())
print(df3.groupby(df3['Gender']=="Male").first())
#Using groupby() for multiple criteria 
print(df3.groupby(['Gender','EstimatedSalary']).last())
#Data Analysis2 using conditions
print(df3['EstimatedSalary'][(df3['Gender']=="Female")&(df3['Age']<=26)])
print(df3['User ID'][(df3['Gender']=="Female")&(df3['Age']==20)])
print(df3['Purchased']==False)
#Data Slicing in data analysis
print(df3.iloc[:3,[2]])
#To find index of the dataframe
print(df3.index)
print(df3.groupby(['EstimatedSalary']))
print(df3['Gender'].unique())