import csv
import pandas as pd

getData = pd.read_csv("dwarf_stars.csv")
# getData.columns()

getData = getData.dropna()
getData.dtypes

getData['Radius'] = getData['Radius'] * 0.102763
getData['Mass'] = getData['Mass'].apply(lambda x: x.replace("$", "").replace(",", "")).astype("float")
getData['Mass'] = getData['Mass'] * 0.000954588

getData.to_csv('final.csv')