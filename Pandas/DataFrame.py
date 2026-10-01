import numpy as np
import pandas as pd


#Series
ser = pd.Series(np.random.rand(34))
print(ser)
print(type(ser))

#DataFrame
newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
print(newdf)
print(type(newdf))

print(newdf.describe())

newdf[0] = newdf[0].astype(object)

newdf.loc[0, 0] = "Ram"
print(newdf.head())


print(newdf.index)
print(newdf.columns)

#Sorting
print(newdf.sort_index(axis=0))
print(newdf.sort_index(axis=1))

print(newdf.sort_index(axis=0,ascending=False)) #By default ascending is True
print(newdf.sort_index(axis=1,ascending=False)) #By default ascending is True


print(newdf[0]) #It is Series
print(type(newdf[0]))

newdf2=newdf.copy()
print(newdf2.head()) 

#loc
newdf.loc[0,0]=783
print(newdf.head())

newdf.columns=list("ABCDE")
print(newdf.head())

newdf.loc[0,0]=789 #It create a new columns 
print(newdf.head())

newdf.loc[0,'A']=789 
print(newdf.head())

newdf=newdf.drop(0,axis=1)  #Drop the columns
print(newdf.head())


newdf3=newdf.loc[[1,2],['C','D']]
print(newdf3)

print(newdf.loc[:,['C','D']]) #For specific coolumns
print(newdf.loc[[1,2],:]) #For specific rows

print(newdf.loc[newdf['A']<0.3])

print(newdf.loc[(newdf['A'] < 0.3) & (newdf['C'] > 0.1)])


#iloc
print(newdf.head(2))
print(newdf.iloc[0,4])


print(newdf.iloc[[0,5],[1,2]]) 


newdf.reset_index(drop=True,inplace=True)
print(newdf.head())


print(newdf['B'].isnull()) #Check Null value in B


df = pd.DataFrame(
    {
        "name": ["Alfred", "Batman", "Catwoman"],
        "toy": [np.nan, "Batmobile", "Bullwhip"],
        "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
    }
)
print(df.dropna())

print(df.dropna(how='all'))

print(df.dropna(how='all',axis=1)) 
print(" ")
print(df.dropna(subset=['name','toy']))


print(df.shape)

print(df.info())



