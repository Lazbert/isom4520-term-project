import numpy as np
import pandas_ta as ta


def add_rsi_strategy(df_in, **params):
    OVERBOUGHT_THRES = 80
    OVERSOLD_THRES = 20

    df = df_in.copy()

    df["rsi"] = ta.rsi(df["Close"], length=14)  # the ta library handles shift within

    df["trade_opening_price"] = df["Open"]

    df["signal"] = 0
    long_mask = (df["rsi"] < OVERSOLD_THRES) & (
        df["stat_market_index_change(t_1)_ratio_1d"].abs() < 0.015
    )
    short_mask = (df["rsi"] > OVERBOUGHT_THRES) & (
        df["stat_market_index_change(t_1)_ratio_1d"].abs() < 0.015
    )

    df.loc[long_mask, "signal"] = 1
    df.loc[short_mask, "signal"] = -1

    df["signal"] = df["signal"].shift(1)

    return df
