from ._add_MA5_crosses_MA50_signal import add_MA5_crosses_MA50_signal
from ._add_rsi_strategy import add_rsi_strategy
from ._add_obv_strategy import add_obv_strategy
from ._add_rsi_with_cmf_strategy import add_rsi_with_cmf_strategy
from pandas import DataFrame
from typing import Callable
import numpy as np


def get_alpha_signal_func(**params):
    strategy_name = params["strategy_name"]

    strategy_signal_func_dict: dict[str, Callable[..., DataFrame]] = {
        "MA5_cross_MA50": add_MA5_crosses_MA50_signal,
        "rsi": add_rsi_strategy,
        "obv": add_obv_strategy,
        "rsi_with_cmf": add_rsi_with_cmf_strategy,
    }

    signal_func = strategy_signal_func_dict.get(strategy_name)

    if signal_func is None:
        raise NotImplementedError(f"Signal '{strategy_name}' is not implemented yet.")

    return signal_func
