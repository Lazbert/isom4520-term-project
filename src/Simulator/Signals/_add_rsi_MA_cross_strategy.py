from pandas import DataFrame
import numpy as np
from ._add_rsi_strategy import add_rsi_strategy
from ._add_MA5_crosses_MA50_signal import add_MA5_crosses_MA50_signal


def add_rsi_MA_cross_strategy(df_in, **params) -> DataFrame:

    df = df_in.copy()
    df["trade_opening_price"] = df["Open"]

    df_rsi = add_rsi_strategy(df, **params)
    df_ma_cross = add_MA5_crosses_MA50_signal(df, **params)

    df["signal"] = np.where(
        (df_rsi["signal"] == 1) & (df_ma_cross["signal"] == 1),
        1,
        np.where((df_rsi["signal"] == -1) & (df_ma_cross["signal"] == -1), -1, 0),
    )
    print(df["signal"].value_counts())

    return df
