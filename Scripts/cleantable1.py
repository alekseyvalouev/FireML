import pandas as pd

data= pd.read_csv('/Users/alekseyvalouev/Desktop/FireData/CSV/table1.csv')

out_data = data.drop_duplicates(subset=['OBJECTID'], keep='first')

out_data.dropna(axis = 0, subset=["ALARM_DATE", "CONT_DATE"], how='all')

out_data.to_csv('/Users/alekseyvalouev/Desktop/FireData/CSV/finaltable1.csv', index=False)
