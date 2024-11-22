import random
from datetime import datetime,timedelta
import time
import pandas as pd
import datetime




#異常名リスト
trouble_name=["オーバーヒート","異音発生","動作停止","センサーエラー","油圧低下"]
random_trouble=random.choice(trouble_name)
#print(random_trouble)

#設備リスト
facility_name=["設備1","設備2","設備3","設備4"]
random_facility=random.choice(facility_name)
# print(random_facility)


#ランダムな時間の取得
# now_time=datetime.now()
# random_seconds=random.randint(0,86400)
# random_datetime=now+timedelta(seconds=random_seconds)





#CSVからセル名とセルパスをリストで取得
df=pd.read_csv('output.csv')
#print(df)
cell_name_list=df['セル番号'].tolist()
cell_path_list=df['MTTR_path'].tolist()
# print(cell_name_list)
# print(cell_path_list)


#タイムスタンプの計算
time_string="2024-05-30T07:00:00.000Z"
default_time=datetime.datetime.strptime(time_string,"%Y-%m-%dT%H:%M:%S.%fZ")
#print(default_time)


put_we=0
put_pa=0
put_af=0

for i in range(0,13):

    put1=random.randint(10,40)
    put2=random.randint(10,40)
    put3=random.randint(10,40)
    put_we+=put1
    put_pa+=put2
    put_af+=put3

    add_time=default_time+datetime.timedelta(hours=i)

n
print(add_time)
print(put_we)
print(put_pa)
print(put_af)




