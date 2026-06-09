#from matplotlib import pyplot as plt
import yfinance as yf
#import pandas as pd

#Initialisation des varibles
data = 0

MU = yf.Ticker("MU")

#print(MU.history(start="2023-03-14", end="2026-03-14", interval="1wk"))

data = MU.history(start="2023-03-14", end="2026-03-14", interval="1wk")

print(data.head(2))
