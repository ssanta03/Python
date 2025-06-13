import pandas as pd
from csv import DictReader
import csv

df = pd.read_csv('shop.csv')
df["Сумма продаж"] = df["Цена"] * df["Количество"]
общая = df['Сумма продаж'].sum()
макс = df['Количество'].max()
кол = df['Товар'].nunique()
сред = df['Цена'].sum() / кол


