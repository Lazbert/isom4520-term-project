import pandas_ta as ta
from pandas import DataFrame


def add_cci_strategy(df_in: DataFrame, **params):
    OVERBOUGHT_THRES = 100
    OVERSOLD_THRES = -100

    df = df_in.copy()

    df["cci"] = ta.cci(df["High"], df["Low"], df["Close"], length=10)  # 10-days MA
    df["trade_opening_price"] = df["Open"]

    df["signal"] = 0
    long_mask = df["cci"] < OVERSOLD_THRES
    short_mask = df["cci"] > OVERBOUGHT_THRES

    df.loc[long_mask, "signal"] = 1
    df.loc[short_mask, "signal"] = -1

    df["signal"] = df["signal"].shift()
    return df
