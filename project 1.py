#supermarket sales data cleaning project
#This project involves cleaning and preprocessing supermarket sales data for analysis.
#and prepare the data for visualization and reporting.

import pandas as pd

# Load data
data=pd.read_excel("C:/Users/HP/OneDrive/Documents/supermarket_sales_with_nulls.xlsx")
df=pd.DataFrame(data)

# Initial exploration
print(df.shape)         
print(df.head())        
print(df.info())        
print(df.describe())    
print(df.isnull().sum()) # how many missing values in each column

# clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# drop unnecessary columns
df.drop(columns=["unitprice"],inplace=True)      

# Handle missing values
df["city"].fillna(df["city"].mode()[0], inplace=True)  
df["payment"].fillna(df["payment"].mode()[0], inplace=True)  
df["quantity"].fillna(df["quantity"].median(), inplace=True)  

# Convert time column to datetime
df["time"]=pd.to_datetime(df["time"], format="%H:%M:%S").dt.date  

# verify cleaning 
print(df.isnull().sum())  
print(df)