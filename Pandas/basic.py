import numpy as np
import pandas as pd


dict1={
    "name":['ram', 'rohan','laxman','hari'],
    "marks":[92,34,23,54],
    "subject":['physics','chemistry','programming in c','calculus']
}

df=pd.DataFrame(dict1)  #DataFrames
print(df)

df.to_csv('project.csv') #for save in .csv file and can access from Excel
df.to_csv('NoIndexProject.csv',index=False) #For No Index

print(df.head(2)) #For access top 2 rows
print(df.tail(2)) #For access last 2 rows

print(df.describe()) #describe Numerical column and calculate like mean,std


project1=pd.read_csv('project1.csv') #read data from file
print(project1)


# For accessing any target value
print(project1['score'][0])
print(project1['course'][6])

# For changing/modifying a value
project1['score'][6] = 90

print(project1)

print(project1['score'][6])
project1.to_csv('project1.csv')

#How to change Index
project1.index = ['first', 'second', 'third', 'fourth', 'fifth','sixth', 'seventh', 'eighth', 'ninth', 'tenth']
print(project1)

