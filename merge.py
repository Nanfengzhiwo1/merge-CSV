import pandas as pd

# folder path
path = 'your path'

# read csv files
df1 = pd.read_csv(path+'1.csv',encoding='ANSI')
df2 = pd.read_csv(path+'2.csv',encoding='ANSI')

# merge files,keep the header
df3 = pd.concat([df1, df2], ignore_index=True)

# drop duplicates
df3.drop_duplicates(subset='your key',keep='last',inplace=True)

# output
df3.to_csv(path+'3.csv', index=False,encoding='ANSI')
