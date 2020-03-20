import yfinance as yf
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


def chart(ticker,start,end,interval='15m'):
    msft = yf.Ticker(ticker)
    hist = msft.history(start=start,end=end,interval=interval)
    #print(hist.Open.to_numpy())
    #for i in hist.Open.to_numpy():
    #    print(i)

    plt.plot(hist.Open.to_numpy(),label='Open')
    plt.plot(hist.High.to_numpy(),label='High')
    plt.plot(hist.Low.to_numpy(),label='Low')


    high_low_delta = np.ndarray(len(hist.Open.to_numpy()))
    for i in range(len(hist.Open.to_numpy())):
        high_low_delta[i] = hist.High.to_numpy()[i] - hist.Low.to_numpy()[i]
        high_low_delta[i] *= 5

    plt.bar(range(len(high_low_delta)),high_low_delta,color='purple',label='Volatility')

    if interval == '15m':
        spacing = range(0,len(high_low_delta),26)
    else:
        spacing = range(0,len(high_low_delta),13)
    plt.xticks(spacing,range(len(spacing)))
    plt.grid(b=True,axis='x')
    plt.title(ticker + ' (' + start + ')-(' + end + ')')
    plt.legend()
    plt.show()


def test():
    chart('DIS','2020-2-1','2020-3-4','15m')
