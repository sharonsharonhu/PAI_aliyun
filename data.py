import pandas as pd

df=pd.read_csv('Test/TestDataset/Data/credit_default.csv')
df1=df.iloc[:40000,:30]
df2=df.iloc[40000:50000,:30]

df3=df.iloc[:40000,30:72]
df4=df.iloc[40000:50000,30:72]

df5=df.iloc[:40000,72:73]
df6=df.iloc[40000:50000,72:73]


df3.to_csv('Test/TestDataset/GeneratedData/Data/SecureXgb_test_data/party2/train.csv')
df4.to_csv('Test/TestDataset/GeneratedData/Data/SecureXgb_test_data/party2/test.csv')