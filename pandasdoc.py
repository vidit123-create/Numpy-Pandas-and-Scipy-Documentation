#how to import the pandas module
import pandas as pd
#how to create dataframe in pandas
df=pd.DataFrame([["Aman",989],["Ankit",976],["Shivam",456]])
print(df)
#how to read data from pandas
dataset=pd.read_csv('C:\\Users\\arpit\\Downloads\\input.csv')
print(dataset)
#how to sort the data in pandas
x=dataset.sort_values(['Age'])
print(x)
#how to find the minimum value in a dataframe
y=dataset['Age'].min()
print(y)
#how to find maximum value in a dataframe
z=dataset['Age'].max()
print(z)
#how to display the elements from the top
s=dataset.head(1)
print(s)
#how to find elements by using conditions
a=dataset[dataset['Name']=="Salman"]
print(a)
#how to use logical operators using pandas
c=dataset[(dataset['Name']=="Vidit")&(dataset['Age']==21)]
print(c)
g=dataset['Name'][dataset['Age']==dataset['Age'].min()].values
print(g)
#Merging of two lists
a=[2,3,4]
b=[5,6,7]
c=list(zip(a,b))
print(c)