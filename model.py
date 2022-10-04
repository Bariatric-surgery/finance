import joblib

import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingRegressor

reg = GradientBoostingRegressor(random_state=0)
reg2 = GradientBoostingRegressor(random_state=0)

df = pd.read_excel('Cabs_Finanz_Osas.xlsx')

df = df.dropna()


# Get the list of all column names from headers
column_names = list(df.columns.values)

feature = df.drop(['Final Cost','Final Revenue','Patient Nr code','Fall Nr code'], axis=1)

final_cost =  df['Final Cost']
Final_Revenue = df['Final Revenue']

reg.fit(feature, final_cost)
reg2.fit(feature, Final_Revenue)


# save the model to disk
joblib.dump(reg, "reg_model.sav")
joblib.dump(reg2, "reg2_model.sav")


