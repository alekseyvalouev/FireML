import pandas as pd
data= pd.read_csv("/Users/alekseyvalouev/Desktop/FireData/CSV/table2.csv")

data = data.dropna(axis=0, subset=['popdensity'])

out_data = pd.DataFrame(data)

out_data.to_csv('/Users/alekseyvalouev/Desktop/FireData/CSV/popdensitycleanedtable2.csv', index=False)
