# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:10:45 2023

@author: Nishi
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info() 

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6


#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem


#CostPerTransaction column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchases
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberofItemsPurchased*CostPerItem

#adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased'] 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased'] 

#Profit Calculation = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

#Markup = {sales - cost}/ cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction'] 

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction'] 


#Rounding Marking

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2) 

#combining data fields
my_date = 'Day' +'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'
print(data['Day'].dtype) 

#change column type 

day = data['Day'].astype(str)
year = data['Year'].astype(str)  
print(day.dtype)
print(year.dtype)
my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date


#using iloc to view specific column
data.iloc[0]
data.iloc[0:3]
data.iloc[-5:]  #last 5 rows
data.head(5) # brings in first 5 rows
data.iloc[:,2] #brings in all the rows on the 2 column

#using split to split the client_keywords fields
#new_var = column.str.split('sep' ,expand = True) 

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new column for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtofContract'] = split_col[2]

#using the replace function to remove  [] 

data['ClientAge'] = data['ClientAge'].str.replace('[' , '') 
data['LenghtofContract'] = data['LenghtofContract'].str.replace(']' , '') 

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#drop columns 

#df = df.drop('columname' , axis = 1)

data = data.drop('ClientKeywords' , axis =1)
data = data.drop('Day' , axis =1)
data = data.drop(['Month', 'Year'] , axis =1)

#export into a csv

data.to_csv('valueInc_Cleaned.csv', index = False)
 