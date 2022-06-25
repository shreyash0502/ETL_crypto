import pandas as pd


def extractor(inpdir):
    coins = {'Aave': 'AAVE', 'BinanceCoin': 'BNB', 'Bitcoin': 'BTC', 'Cardano': 'ADA', 'ChainLink': 'LINK',
             'Cosmos': 'ATOM', 'CryptocomCoin': 'CRO',
             'Dogecoin': 'DOGE', 'EOS': 'EOS', 'Ethereum': 'ETH', 'Iota': 'MIOTA', 'Litecoin': 'LTC', 'Monero': 'XMR',
             'NEM': 'XEM', 'Polkadot': 'DOT',
             'Solana': 'SOL', 'Stellar': 'XLM', 'Tether': 'USDT', 'Tron': 'TRX', 'USDCoin': 'USDC', 'Uniswap': 'UNI',
             'WrappedBitcoin': 'WBTC',
             'XRP': 'XRP'}

    ticker = list(coins.keys())
    raw = {t: pd.read_csv("../{}/coin_{}.csv".format(inpdir, ticker[index]), header=0)
           for index, t in enumerate(ticker)}

    for t in ticker:
        raw[t]['Date'] = pd.to_datetime(raw[t]['Date'])
        # raw[t].drop('Date', axis=1, inplace=True)
        raw[t].set_index('Date', inplace=True)
        # raw[t].reset_index(drop=True, inplace=True)
        raw[t].drop('SNo', axis=1, inplace=True)
        raw[t].drop('Name', axis=1, inplace=True)
        raw[t].drop('Symbol', axis=1, inplace=True)
        raw[t]['Volume'] = pd.to_numeric(raw[t]['Volume'])
        raw[t]['Marketcap'] = pd.to_numeric(raw[t]['Marketcap'])
        # display(raw[t].head())
    data = pd.concat(raw.values(), axis=1, keys=ticker)
    data.columns.names = ['Ticker', 'Info']
    return [ticker, raw, data]
