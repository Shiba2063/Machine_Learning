# # Univariate -Numerical


import matplotlib.pyplot as plt
import pandas as pd

data={
    "salary":[25000,19000,38000,29000,30000,31000,26000,20300]
}

df=pd.DataFrame(data)
# # print(df)
# print(df.head())

# print(df.shape)

# #line plot

# plt.plot(df["salary"],color="red",marker="o", linestyle="--")
# plt.grid()
# plt.show()

# #Histogram 
# plt.hist(df["salary"],bins=5,color="green")
# plt.show()


# #Boxplot
# plt.boxplot(df["salary"])
# plt.show()

#Univariate categories
df["dept"]=['HR','IT','Finance','IT','HR','IT','Finance','HR']
# print(df.head())

# print(df.info())

#Pie chart
# count=df["dept"].value_counts()
# print(count)

# plt.pie(count,labels=count.index,autopct="%1.1f",explode=[0.1,0.1,0.2])
# plt.axis("equal")
# plt.show()

#countplot
# plt.bar(count.index,count)
# plt.bar(count.index,count,color=["green","black","red"])
# plt.show()


#Bivariate 

#numerical - numerical
df["Age"]=[22,20,25,23,40,45,54,30]
# print(df.head())


# scatter plot
# plt.scatter(df["Age"],df["salary"],color="orange")
# print(plt.show())

#line plot:
# plt.plot(df["Age"],df["salary"],color="red",marker="*",linewidth="2")
# plt.grid()
# print(plt.show())

#for better visualization
sort_age=df.sort_values("Age")
# plt.plot(sort_age["Age"],df["salary"],color="red",marker="*",linewidth="2")
# plt.grid()
# print(plt.show())


#Bar chart:
# plt.bar(sort_age["Age"],df["salary"],color="green")
# print(plt.show())

#Bivariate:Numerical-categorical
hr_sal=df[df["dept"]=="HR"]["salary"]
it_sal=df[df["dept"]=="IT"]["salary"]
fin_sal=df[df["dept"]=="Finance"]["salary"]
# print(hr_sal)

#Boxplot

# plt.boxplot([hr_sal,it_sal,fin_sal],label=["HR","IT","Finance"])
# print(plt.show())


#pie chart

salary_by_dept = df.groupby("dept")["salary"].sum()
# print(salary_by_dept)

# plt.pie(salary_by_dept,labels=salary_by_dept.index,autopct="%1.2f%%")
# plt.axis("equal")
# plt.show()



# Bar Chart
hr_mean=sum(hr_sal)/len(hr_sal)
it_mean=sum(it_sal)/len(it_sal)
fin_mean=sum(fin_sal)/len(fin_sal)

# plt.bar(["HR","IT","Finance"],[hr_mean,it_mean,fin_mean],color=["green","red","black"])
# plt.show()




#multivariate Analysis : 3 numerical columns

# df.head()
df["experience"]=[1,2,3,4,5,6,7,8]
# print(df.head())

#Bubble plot:
# plt.scatter(df["Age"],df["salary"],s=df['experience']*30,color="blue", edgecolors="black")
# plt.title("Age vs salary")
# plt.xlabel("Age")
# plt.ylabel("salary")
# plt.grid()
# plt.show()


#2 numerical and 1 categorical column:
# plt.scatter(
#     df["Age"],
#     df["salary"],
#     c=df["dept"].map({
#         "HR": "yellow",
#         "IT": "blue",
#         "Finance": "orange"
#     })
# )

# plt.xlabel("Age")
# plt.ylabel("salary")
# plt.title("Age vs salary vs dept")
# plt.legend()
# plt.show()


# color={"HR": "yellow",
#         "IT": "blue",
#         "Finance": "orange"}

# for dept,color in color.items():
#     df_dept=df[df['dept']==dept]
#     plt.scatter(df_dept['Age'],df_dept["salary"],c=color,label=dept)

# print(plt.legend())



#object oriented API
# fig,axs=plt.subplots(1,3,figsize=(15,5))
# # print(plt.show())
# #line plot
# axs[0].plot(sort_age['Age'],df["salary"], color="red",marker="*",linewidth=2,markersize=2)
# axs[0].grid()
# axs[0].set_title("Line Plot")
# axs[0].set_xlabel("Age")
# axs[0].set_ylabel("salary")

# #histogram

# axs[1].hist(df["salary"],bins=5,color="skyblue")
# axs[1].set_title("Histogram")
# axs[1].set_xlabel("salary")
# axs[1].set_ylabel("Frequency")


# #Box plot
# axs[2].boxplot(df["salary"])
# axs[2].set_title("Boxplot")
# axs[2].set_xlabel("salary")
# # print(plt.show())

# plt.savefig("Multiplots.png")
# print(plt.show())





# data={
#     "Year":[2000,2001,2002,2003],
#     "Sales":[100,150,200,25],
#     "Profit":[20,30,40,50],
#     "Expenses":[80,120,160,200]
# }

# df=pd.DataFrame(data)

# plt.plot(df["Year"],df["Sales"],label="Sales")
# plt.plot(df["Year"],df["Profit"],label="Profit")
# plt.plot(df["Year"],df["Expenses"],label="Expenses")


# plt.title("Financial Analysis")
# plt.xlabel("Year")
# plt.ylabel("Amount")
# plt.legend()
# print(plt.show())



# 3D plot

ax=plt.axes(projection='3d')
ax.scatter(df["Age"],df["salary"],df["experience"])
ax.set_xlabel("Age")
ax.set_ylabel("salary")
ax.set_zlabel("Experience")
print(plt.show())




