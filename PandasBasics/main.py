#calling the libraries but only using Pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
print("successful")

#calling the data
df = pd.read_excel (r'inputing file location')

#getting rid of unnecessary blank columns in the spreadsheet 
df.columns = df.columns.str.replace(' ', '_')

#review
df.head()

#replacing unnecessary NaN Colums in the spreadsheet
df.columns = df.columns.str.replace('NaN', ' ')

#breaking down the coloums to review transaction and spending behavior
df[['Account_Key_', 'Transaction_Date', 'Debit_Amount', 'Credit_Amount']]

#Getting the total sum of the debits and credits that were deposited and spend by the customer
df.iloc[:, 8:10].sum()
