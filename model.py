import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv("house_price_dataset_clean (1).csv")
print(df.head(2))

X=df[["Size (sq. ft.)","Bedrooms", "Bathrooms","Age of House (Years)","Distance to City Center (Miles)"]]
y=df["Price"]

ml_model=LinearRegression()
ml_model.fit(X,y)

pickle.dump(ml_model, open('model.pkl', 'wb'))
print("model trained and dumped into pikl file")