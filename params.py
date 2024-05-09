def get_params(
    years_to_consider=5,
    n_symbols=7,
    market="US-TERM",  # US
    slippage_rate=0.00025,
    # Strategy params
    strategy_name="rsi_with_cmf",  # refer to get_alpha_signal_func.py
    # STOP LOSS
    stop_loss_percentage=5,  # 3
    risk_level_percentage=0.2,
    should_stop_loss=True,
    # TAKE PROFIT
    take_profit_percentage=5,  # 3
    should_take_profit=True,
    # Intraday trading params
    should_close_at_end_of_candle=False,
    should_close_at_signal=False,
    # run_alpha_params
    should_limit_one_position_in_run_alpha=True,
    run_parallel=False,
    # Reporting params
    reporting_period="Year",
    n_executed_trade_for_plotting=1,
    # Data pre-processing params
    should_add_garch=False,
    should_add_arima_forecasting=False,
    should_load_from_cache=True,
    draw_stat_figures=True,
    should_log=True,
    # rsi & cmf hyperparameters
    rsi_length=14,
    rsi_overbought_thres=70,
    rsi_oversold_thres=30,
    cmf_bullish_thres=0,
    cmf_bearish_thres=-0,
):
    """
    Params:

    years_to_consider: int
        Number of years to consider for backtesting

    n_symbols: int
        Number of symbols to consider for backtesting

    market: str
        Market to backtest on [US, HK, Crypto]

    slippage_rate: float
        Slippage rate for backtesting

    strategy_name: str
        Strategy to backtest on [random, buy_and_hold]

    stop_loss_percentage: float
        Stop loss percentage for backtesting

    risk_level_percentage: float
        Risk level percentage for backtesting

    should_stop_loss: bool
        Whether to use stop loss for backtesting

    take_profit_percentage: float
        Take profit percentage for backtesting

    should_take_profit: bool
        Whether to use take profit for backtesting

    should_close_at_end_of_candle: bool
        Whether to close position at end of candle

    should_limit_one_position_in_run_alpha: bool
        Whether to limit one position in run_alpha

    run_parallel: bool
        Whether to run parallel in run_alpha

    reporting_period: str
        Reporting period for backtesting

    n_executed_trade_for_plotting: int
        Number of executed trades for plotting

    should_add_garch: bool
        Whether to add garch

    should_add_arima_forecasting: bool
        Whether to add arima forecasting

    should_load_from_cache: bool
        Whether to load from cache

    Returns:
        dict
    """

    return {
        "trading_interval": "1d",
        "years_to_consider": years_to_consider,
        "n_symbols": n_symbols,
        "market": market,
        "slippage_rate": slippage_rate,
        "strategy_name": strategy_name,
        "strategy_type": "market_neutral",
        "risk_level_percentage": risk_level_percentage,
        "should_stop_loss": should_stop_loss,
        "stop_loss_percentage": stop_loss_percentage,
        "should_take_profit": should_take_profit,
        "take_profit_percentage": take_profit_percentage,
        "should_close_at_end_of_candle": should_close_at_end_of_candle,
        "should_close_at_signal": should_close_at_signal,
        "should_load_from_cache": should_load_from_cache,
        "should_limit_one_position_in_run_alpha": should_limit_one_position_in_run_alpha,
        "reporting_period": reporting_period,
        "run_parallel": run_parallel,
        "n_executed_trade_for_plotting": n_executed_trade_for_plotting,
        "should_add_garch": should_add_garch,
        "should_add_arima_forecasting": should_add_arima_forecasting,
        "take_profit_strategy": "Simple",
        "should_log": should_log,
        "draw_stat_figures": draw_stat_figures,
        "rsi_length": rsi_length,
        "rsi_overbought_thres": rsi_overbought_thres,
        "rsi_oversold_thres": rsi_oversold_thres,
        "cmf_bullish_thres": cmf_bullish_thres,
        "cmf_bearish_thres": cmf_bearish_thres,
    }
