import pandas as pd

scExcel = pd.read_excel('IEEE.xls')
scExcel.sort_values(by='Year')
scExcel.to_excel('new.xls')