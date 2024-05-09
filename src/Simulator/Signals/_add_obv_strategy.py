from pandas import DataFrame
import pandas_ta as ta


# https://medium.com/@mail.remotetrades/trading-strategy-obv-divergence-trade-6ba567a636a5
def add_obv_strategy(df_in: DataFrame, **params):
    """OBV divergence strategy with lookback period of 10 days"""
    ATR_MULTIPLIER = 4

    df = df_in.copy()
    df["trade_opening_price"] = df["Open"]

    # obv
    df["obv"] = ta.obv(df["Close"], df["Volume"])
    df["obv_10d_highest"] = df["obv"].rolling(window=10).max()
    df["obv_10d_lowest"] = df["obv"].rolling(window=10).min()

    # price movements
    df["Close_10d_highest"] = df["Close"].rolling(window=10).max()
    df["Close_10d_lowest"] = df["Close"].rolling(window=10).min()
    df["ma_100"] = df["Close"].rolling(window=100).mean()

    # confirm divergence with ATR
    df["atr_14"] = ta.atr(df["High"], df["Low"], df["Close"], length=14)

    df["signal"] = 0
    long_mask = (
        (df["obv"] == df["obv_10d_highest"])
        & (df["Close"] < df["Close_10d_highest"])
        & (df["Close"] <= df["ma_100"] - ATR_MULTIPLIER * df["atr_14"])
    )
    short_mask = (
        (df["obv"] == df["obv_10d_lowest"])
        & (df["Close"] > df["Close_10d_lowest"])
        & (df["Close"] >= df["ma_100"] + ATR_MULTIPLIER * df["atr_14"])
    )

    df.loc[long_mask, "signal"] = 1
    df.loc[short_mask, "signal"] = -1
    df["signal"] = df["signal"].shift()
    return df
