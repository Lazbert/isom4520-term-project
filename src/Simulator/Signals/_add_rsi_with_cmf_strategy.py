import pandas_ta as ta
from pandas import DataFrame


def add_rsi_with_cmf_strategy(df_in: DataFrame, **params) -> DataFrame:
    OVERBOUGHT_THRES = params.get("rsi_overbought_thres", 70)  # 70
    OVERSOLD_THRES = params.get("rsi_oversold_thres", 30)  # 30
    CMF_BULLISH = params.get("cmf_bullish_thres", 0.05)  # 0.05
    CMF_BEARISH = params.get("cmf_bearish_thres", -0.05)  # -0.05

    df = df_in.copy()

    df["rsi"] = ta.rsi(df["Close"], length=14)
    df["cmf"] = ta.cmf(df["High"], df["Low"], df["Close"], df["Volume"], length=20)
    df["trade_opening_price"] = df["Open"]

    df["signal"] = 0
    long_mask = (df["rsi"] < OVERSOLD_THRES) & (df["cmf"] > CMF_BULLISH)
    short_mask = (df["rsi"] > OVERBOUGHT_THRES) & (df["cmf"] < CMF_BEARISH)

    df.loc[long_mask, "signal"] = 1
    df.loc[short_mask, "signal"] = -1

    df["signal"] = df["signal"].shift()
    return df
