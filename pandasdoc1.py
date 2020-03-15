import pandas as pd
df=pd.DataFrame([["Sohail",50,"Bandra",5.5,75],["Salman",54,"Bandra",5.6,78],["Aarbaz",51,"Bandra",5.8,73]],columns=['A','B','C','D','E'])
print(df)
df.to_excel('Output.xlsx',index=False)
#To check datatype of a particular column
x=df.A.dtype 
print(x)
y=df.dtypes 
print(y)
z=df.shape 
print(z)
#To change each value to upper case we use upper() and apply()
df['A']=df.A.apply(lambda y:y.upper())
print(df['A'])
#to change each value to lower case we use lower() and apply()
df['C']=df.C.apply(lambda z:z.lower())
print(df['C'])
df1=pd.DataFrame([["Aman","Ajay","Ankit","Shivam","Ajay","Aman","Rishabh"]],columns=['A','B','C','D','E','F','G'])
print(df1)
#To print unique values from a particular column
print(df1['A'].unique())
#DATA CLEANING
#Do Analysis of dataframe on the basis of condition
print(df['D'][(df['A']=="Sohail")&(df['C']=="Bandra")].values)
print(df['D'].max())
print(df['E'].min())
print(df.sort_values(['D']))
#Import Dataset from the excel file 
df2=pd.read_csv('C:\\Users\\arpit\\Desktop\\50_Startups.csv')
print(df2)
#Use Groupby() to split the datasets into groups according to some criteria and show us the data
print(df2.groupby(df2['State']=="Florida").last())
print(df2.groupby(['State']).last())
print(df2.State.apply(lambda p:p.upper()))
print(df2.State.apply(lambda e:e.lower()))
print(df2['State'].unique())
#Use groupby() to group the values but on the basis of some value of a particular column
a=df2.groupby(['State'])
print(a)
#b=a.get_group("California")
#print(b)