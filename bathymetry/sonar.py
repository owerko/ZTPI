import pandas as pd
data = pd.read_csv('Chart 6_5_16 [0].csv')
print(data.head())
depth = data['Depth'].to_list()
time = data['TimeOffset[ms]'].to_list()
print(depth)
print(time)