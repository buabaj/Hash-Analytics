import pandas as pd #importing the pandas library

workbook = pd.read_excel('data.xlsx', sheet_name= None)  #reading the workbook
for sheet in workbook: # using a loop to get individual sheets
   workbook[sheet].to_csv('%s.csv' %sheet) #converting all sheets to csv format