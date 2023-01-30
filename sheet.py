import csv
import pandas as pd

column_name = ["Catagory","Product_Name", "Price", "Quanty"] #The name of the columns
data = ['1',"2", "3","4"] #the data

with open('D:\Data.csv', 'w') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
    writer.writerow(data) #this is the data

df = pd.read_csv('D:\Data.csv')
print(df)