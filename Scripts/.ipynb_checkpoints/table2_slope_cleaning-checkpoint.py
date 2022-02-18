import pandas as pd

data= pd.read_csv('/Users/alekseyvalouev/Desktop/FireData/CSV/popdensitycleanedtable2.csv')

data["slope_mean"][data["slope_mean"] < 0] = 0

data.to_csv('/Users/alekseyvalouev/Desktop/FireData/CSV/finaltable2.csv', index=False)