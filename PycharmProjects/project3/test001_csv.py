import pandas as pd

df=pd.read_csv('In_Active_History.csv')


df=df.drop_duplicates(subset=['セル番号'])
df_sorted=df.sort_values(by='セル番号')
df_inactive=df_sorted[['セル番号','大工程','中工程']]
print(df_inactive)


#CSVからセル名とパスをリストで取得
df2=pd.read_csv('cellname_path.csv')
df2=df2.rename(columns={'セル名':'セル番号'})
df_sorted_path=df2.sort_values(by='セル番号')


print(df_sorted_path)

print(len(df_inactive))
print(len(df_sorted_path))
#cell_name_list=df['セル名'].tolist()
#print(cell_name_list)

merged_df=pd.merge(df_inactive,df_sorted_path,on='セル番号')

merged_df.to_csv('output.csv',index=False)
