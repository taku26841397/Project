import pandas as pd
import json

ex_file="sample_CT_table (1).xlsx"

df=pd.read_excel(ex_file,sheet_name="Sheet1")
print(df.shape)
print(df.head())

json_data=df.to_json("output2.json",orient="records",force_ascii=False)





