from extractor import extractor
from loader import loader
import pandas as pd
from IPython.display import display
from sqlalchemy import create_engine
import pymysql
from config import config
pymysql.install_as_MySQLdb()


def driver(inpdir):
    temp = extractor(inpdir)
    ticker = temp[0]
    raw = temp[1]
    data = temp[2]

    mx_price = pd.DataFrame(data.xs(key='Close', axis=1, level='Info').max())
    mx_price = mx_price.reset_index(drop=False)
    mx_price.columns = ['Name', 'Close']
    mx_price = mx_price.sort_values('Close', ascending=False).reset_index(drop=True)

    rates = []
    for t in ticker:
        datatemp = raw[t]
        datatemp['MA60'] = datatemp['Close'].rolling(window=60).mean()
        datatemp['MA60 shift year'] = datatemp['MA60'].shift(250)
        datatemp['Growth Rate'] = (datatemp['MA60'] - datatemp['MA60 shift year']) * 100 / datatemp['MA60 shift year']
        rates += [[t, datatemp['Growth Rate'].tolist()[-1]]]
        datatemp = pd.DataFrame(datatemp.reset_index(drop=False))
        raw[t] = datatemp

    # print(rates[0:5])

    indi_rates = raw
    for t in ticker:
        indi_rates[t] = indi_rates[t][['Date', 'Growth Rate']]
        indi_rates[t] = indi_rates[t].rename(columns={'Date': 'curdate', 'Growth Rate': 'growthrate'})

    growth_rate = pd.DataFrame(columns=['Name', 'Annual Growth Rate %'], data=rates)
    growth_rate_ordered = growth_rate.sort_values('Annual Growth Rate %', ascending=False).reset_index(drop=True)

    mx_price = mx_price.rename(columns={'Name': 'CryptoName', 'Close': 'MaxClose'})
    growth_rate_ordered = growth_rate_ordered.rename(columns={'Name': 'CryptoName', 'Annual Growth Rate %': 'growthRate'})

    print('\nMaximum Closing prices for each of the cryptocurrencies (for the entire time period) is shown below:')
    display(mx_price)

    print('\nMost recent growth rates for each of the cryptocurrencies is shown below:')
    display(growth_rate_ordered)

    print('\nIndividual growth rates for each of the cryptocurrencies over the entire record period can be checked'
          'from the database tables named as - "<crypto>" and can be accessed through MySQL command line.')
    print('Example: for Bitcoin, the data is stored in table named as "bitcoin".')

    engine = create_engine(config)
    loader(engine, 'max_price', mx_price)
    loader(engine, 'growth_rates', growth_rate_ordered)
    for t in ticker:
        loader(engine, t.lower(), indi_rates[t])
