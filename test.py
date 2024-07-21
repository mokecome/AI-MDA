from pandasai import SmartDatalake
import pandas as pd
import os
df = pd.read_excel('data/data.xlsx', sheet_name=None)
print(list(df))  # 印出所有sheet名稱
test_b = pd.read_excel("data/data.xlsx",sheet_name=list(df)[0])
test_c = pd.read_excel("data/data.xlsx",sheet_name=list(df)[1])
test_bc = pd.read_excel("data/data.xlsx",sheet_name=list(df)[2])

os.environ["PANDASAI_API_KEY"] ='$2a$10$xVT7B/VJpg2dZuvRvoTm6OUx.t.7Ktub7HKmRMM2DHFewAns.kkEK'
lake = SmartDatalake([test_b, test_c,test_bc])
lake.chat("The total number of newly diagnosed patients with liver diseases of type B, type C, and type B+C in the current month")
