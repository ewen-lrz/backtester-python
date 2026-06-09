#from matplotlib import pyplot as plt
import yfinance as yf
import pandas as pd

#Initialisation des varibles
data = 0

#Recuperer les données
#MU = yf.Ticker("MU")

#print(MU.history(start="2023-03-14", end="2026-03-14", interval="1wk"))

#data = MU.history(start="2026-02-14", end="2026-03-14", interval="1wk")

#data.to_csv("data/mu_data_1wk.csv")
data = pd.read_csv("data/MU_data_1wk.csv")

print(data.head(100))
