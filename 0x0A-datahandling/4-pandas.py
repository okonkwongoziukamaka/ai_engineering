# a program that loads data using pandas

import pandas as pd
# df means dataframe
df = pd.read_excel("0x0A-datahandling/PRACTICE.xlsx")


print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)
