import os.path

import pandas as pd
#
# def output_csv(csv_data):
#
#     df=pd.DataFrame(csv_data,columns=["A","B","C"])
#
#     if not os.path.exists("./test.csv"):
#         df.to_csv("./test.csv",index=False)
#         print("CSVを出力しました。")
#     else:
#         print("既にCSVを出力済みです")
#
# data=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# output_csv(data)



    data = {
        "A":[1,4,7],
        "B":[2,5,8],
        "C":[3,6,9],
    }

    df = pd.DataFrame(data)
    print(df)
    df.to_csv("test2.csv", index=False)
