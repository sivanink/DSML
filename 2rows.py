import pandas as pd
name=["Alice","Bob","Charlie"]
age=[25,30,35]
score=[88,76,91]
df=pd.DataFrame({"name":name,"age":age,"score":score})
print(df)
print("First 2 rows:")
first_2_rows=df.head(2)
print(first_2_rows)
