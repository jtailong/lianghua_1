import akshare as ak
import pandas as pd


stock_data = ak.stock_zh_a_spot()
print(stock_data)
file_path = 'output3.xlsx'
stock_data.to_excel(file_path, index=False)

# dict1 = {'name':'tailong','age':19,}
# print(dict1['name'])
#
# print("\n all the values in tuple",tuple(dict1.values()))
# print("\n  all the keys",list(dict1.keys()))
# print("\n all the values and keys :%s"% dict1.items())