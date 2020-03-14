import yfinance as yf
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

msft = yf.Ticker('MSFT')
hist = msft.history(start='2020-3-1',end='2020-5-3',interval='15m')
print(hist.Open.to_numpy())

plt.plot(hist.Open.to_numpy())
plt.plot(hist.High.to_numpy())
plt.plot(hist.Low.to_numpy())


high_low_delta = np.ndarray(len(hist.Open.to_numpy()))
for i in range(len(hist.Open.to_numpy())):
    high_low_delta[i] = hist.High.to_numpy()[i] - hist.Low.to_numpy()[i]

plt.bar(range(len(high_low_delta)),high_low_delta)

plt.show()
