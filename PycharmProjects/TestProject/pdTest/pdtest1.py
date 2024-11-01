from operator import truediv

import pandas as pd


csv_train=pd.read_csv("../pandas_train.csv")
#csv_train.to_csv("../pandas_train2.csv")

# csv_train["Satisfied"]=0
# print(csv_train["Satisfied"])

# csv_train["AgeBin"]=pd.cut(csv_train["Age"],4)
# print(csv_train)
# csv_train.to_csv("../pandas_train3.csv")

csv_train["FareBin"]=pd.qcut(csv_train["Fare"],4)

csv_train.drop(["PassengerId","Ticket"],axis=1,inplace=True)

csv_train["Familysize"]=csv_train["SibSp"]+csv_train["Parch"]+1

csv_train["IsAlone"]=1
# csv_train["IsAlone"].loc[csv_train["Familysize"]>1]=0

# csv_train=pd.get_dummies(csv_train,columns=["Sex","Embarked"])


# csv_train2=csv_train.drop(["Satisfied"],axis=1)
# print(csv_train2)
#
# csv_train3=csv_train[["Satisfied","Name"]]
# print(csv_train3)
# print(csv_train)

csv_train=pd.read_csv("../pandas_train.csv")

# print(csv_train.shape)
# print(csv_train.columns)
#
# csv_train.info()
#
# print(csv_train.isnull().sum())

# print(csv_train.tail())
#
# df2=csv_train.sort_values(by="Pclass",ascending=True)
# df2.set_index("Pclass",inplace=False)
# print(df2)

# csv_train=csv_train.dropna()
print(csv_train)