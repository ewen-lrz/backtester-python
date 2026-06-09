#from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd

#Variable init
data = 0

#Define MU w/ MU stocks
#MU = yf.Ticker("MU")

#Get data on a period of time w/ a time frame
#data = MU.history(start="2022-03-14", end="2026-03-14", interval="1wk")

#data.to_csv("data/mu_data_1wk.csv")

#Def data w/ value in the csv, use index to define which column is the "main one" (index one)
data = pd.read_csv("data/MU_data_1wk.csv", index_col=0)

print(data.head(2))
