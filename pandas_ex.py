import pandas as pd
#print(pd.__version__) # pandas able to clean the data

#pandas is a library used for data manipulation and analysis in Python. It provides data structures like Series and DataFrame, which are used to store and manipulate data in a tabular format. Pandas is built on top of NumPy and is widely used in data science and machine learning for data cleaning, transformation, and analysis.
# data analysis
#data cleaning
#data transformation   
#data visualization preparation
#csv/excel file handling
#frequently we will use in machine learning

# > pip install pandas

#import
#import pandas as pd

#print(pd.__version__)

# 1.switch to python_basics
   #cd python_basics or cd basics
#2.create requirements.txt
   # pandas

#3.create virtual environment
   # python -m venv venv 
   #or
   # python3 -m venv venv
#4.activate virtual environment
   #venv\Scripts\activate (windows)
   #source venv/bin/activate (linux/mac)

#5.install requirements.txt file
    # pip install -r requirements.txt

#example -2
#nums = [10,20,30,40,50]
#res = pd.Series(nums)
#print(res)

#example -3
#data = ["python","Ml","DL","GenAI","AgenticAI"]
#res = pd.Series(data,index=["a","b","c","d","e",])
#print(res)

#example -4
#marks =[80,90,95]
#res = pd.Series(marks,index=["std1","std2","std3"])
#print(res)
#print(res["std2"])

#example -5
#employees = {
 #   "EmpId":[101,102,103],
#    "Department":["IT","HR","Finance"],
 #   "Salary":[50000,60000,70000]
#}
#df = pd.DataFrame(employees,index=["a","b","c"])
#print(df)

#example -6
#df = pd.read_csv("employees.csv")
#print(df)
#print(df.head()) #read first 5 rows(default)
#print(df.head(3)) #read first 3 rows
#print(df.head(10))#read first 10 rows

#print(df.tail()) #read last 5 rows(default)
#print(df.tail(10)) #read last 10 rows

#print(df.shape) #read number of rows and columns
#print(df.columns) #read column names

#print(df.info()) #read data types and non-null values
#print(df.describe()) #read statistical summary of numerical columns
#print(df["Salary"].describe()) #read statistical summary of salary column)
#print(df[["Salary","Bonus"]].describe()) #read statistical summary of salary and bonus columns/mathematical calculations
#print(df["Name"]) #read statistical summary of name column
#print(df[["Name","Age"]].head()) #read first 5 rows of name and age columns
#print(df[df["Salary"]>70000]) #read rows where salary is greater than 70000
#print(df[df["Department"]=="IT"]) #read rows where department is IT
#print(df.groupby("Department")["Salary"].mean()) #read average salary by department 
#print(df.sort_values("Salary", ascending=False).head(1)[["Name","Department","Designation"]]) #sort dataframe by salary in descending order   
#print(df[(df["Salary"]>70000) & (df["Department"]=="IT")]) #read rows where salary is greater than 70000 and department is IT



#load the csv file
df = pd.read_csv("employees_null.csv")
#print(df)
#print(df.isnull()) #check for null values
#print(df.notnull()) #check for non-null values

#print(df.isnull().sum()) #count of null values in each column

##null_pct = (df.isnull().sum() / len(df)) * 100
#print(null_pct) #percentage of null values in each column

#print(df.fillna(0)) #fill null values with 0

#print(df.fillna(df["age"].mean())) #fill null values with mean of age column
#print(df.fillna(df["salary"].mean())) #fill null values with mean of salary column

#print(df)
#print(df.ffill()) #forward fill - fill null values with previous non-null value
#print(df.bfill()) #backward fill - fill null values with next non-null value
#df[["age", "salary"]] = df[["age", "salary"]].interpolate() #interpolation - fill null values with linear interpolation
#print(df)

#print(df.dropna()) #drop rows with null values
#print(df.dropna(how="all")) #drop rows where all values are null
#print(df.dropna(subset=["age"])) #drop rows where age is null
#print(df.dropna(thresh=2)) #drop rows with less than 2 non-null values
