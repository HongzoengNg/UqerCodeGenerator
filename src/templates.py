# -*- coding:utf-8 -*-
'''
File: templates.py
File Created: Tuesday, 12th February 2019
Author: Hongzoeng Ng (kenecho@hku.hk)
-----
Last Modified: Tuesday, 12th February 2019
Modified By: Hongzoeng Ng (kenecho@hku.hk>)
-----
Copyright @ 2018 KenEcho
'''

moving_average_code = """# Moving average strategy
start = '%s'
end = '%s'
universe = %s
benchmark = "HS300"
freq = "d"
refresh_rate = 1
max_history_window = %s

accounts = {
    "security_account": AccountConfig(
        account_type="security",
        capital_base=10000000,
        commission=Commission(buycost=0.00, sellcost=0.00, unit="perValue"),
        slippage=Slippage(value=0.00, unit="perValue")
    )
}


def initialize(context):
    context.asset_allocation = %s


def handle_data(context):
    security_account = context.get_account("security_account")
    current_universe = context.get_universe("stock", exclude_halt=False)
    hist = context.get_attribute_history(
        attribute="closePrice", time_range=max_history_window, style="sat"
    )

    for stk in current_universe:
        short_ma = hist[stk][-%s:].mean()
        long_ma = hist[stk][:].mean()

        if (short_ma > long_ma) and (stk not in security_account.get_positions()):
            security_account.order_pct_to(stk, context.asset_allocation[stk])
        elif short_ma <= long_ma and (stk in security_account.get_positions()):
            security_account.order_to(stk, 0)

"""

macd_code = """# MACD Strategy
import pandas as pd
import numpy as np
import talib

start = '%s'
end = '%s'
universe = %s
benchmark = 'HS300'
freq = 'd'
refresh_rate = 1
max_history_window = %s


accounts = {
    'security_account': AccountConfig(
        account_type='security',
        capital_base=10000000,
        commission = Commission(buycost=0.00, sellcost=0.00, unit='perValue'),
        slippage = Slippage(value=0.00, unit='perValue')
    )
}

def initialize(context):
    context.asset_allocation = %s
    context.short_win = %s # default to be 12
    context.long_win = %s # default to be 26
    context.macd_win = %s # default to be 9

def handle_data(context):
    security_account = context.get_account('security_account')
    current_universe = context.get_universe('stock', exclude_halt=False)
    hist = context.get_attribute_history(
        attribute='closePrice', time_range=max_history_window, style='sat'
    )

    for stk in current_universe:
        prices = hist[stk].values
        macd, signal, macdhist = talib.MACD(
            prices,
            fastperiod=context.short_win,
            slowperiod=context.long_win,
            signalperiod=context.macd_win
        )
        if (macd[-1] - signal[-1] > 0) and (stk not in security_account.get_positions()):
            security_account.order_pct_to(stk, context.asset_allocation[stk])
        elif (macd[-1] - signal[-1] < 0) and (stk in security_account.get_positions()):
            security_account.order_to(stk, 0)

"""

stochastic_oscillator_code = """# Stochastic oscillator
import pandas as pd
import numpy as np
import talib as ta

start = '%s'                      
end = '%s'                     
universe = %s
benchmark = 'HS300'                       
freq = 'd'                                 
refresh_rate = 1
max_history_window = %s
  

accounts = {
    'security_account': AccountConfig(
        account_type='security',
        capital_base=10000000,
        commission = Commission(buycost=0.00, sellcost=0.00, unit='perValue'),
        slippage = Slippage(value=0.00, unit='perValue')
    )
}
  
def initialize(context):
    context.asset_allocation = %s
    context.fastk = %s # default to be 14
    context.slowk = %s # default to be 3
    context.slowd = %s # default to be 3
    
def handle_data(context):
    security_account = context.get_account('security_account')
    current_universe = context.get_universe('stock', exclude_halt=False)
    hist_close = context.get_attribute_history(
        attribute='closePrice', time_range=max_history_window, style='sat'
    )
    hist_high = context.get_attribute_history(
        attribute='highPrice', time_range=max_history_window, style='sat'
    )
    hist_low = context.get_attribute_history(
        attribute='lowPrice', time_range=max_history_window, style='sat'
    )
    
    for stk in current_universe:
        close = hist_close[stk].values
        high = hist_high[stk].values
        low = hist_low[stk].values
        slowk, slowd = ta.STOCH(
            high, low, close,
            fastk_period=context.fastk,
            slowk_period=context.slowk,
            slowk_matype=0,
            slowd_period=context.slowd,
            slowd_matype=0
        )
        if (slowk[-1] > slowd[-1]) and (stk not in security_account.get_positions()):
            security_account.order_pct_to(stk, context.asset_allocation[stk])
        elif (slowk[-1] < slowd[-1]) and (stk in security_account.get_positions()):
            security_account.order_to(stk, 0)

"""

buy_hold_code = """# Buy & Hold strategy
start = '%s'
end = '%s'
universe = %s
benchmark = "HS300"
freq = "d"
refresh_rate = 1

accounts = {
    "security_account": AccountConfig(
        account_type="security",
        capital_base=10000000,
        commission=Commission(buycost=0.00, sellcost=0.00, unit="perValue"),
        slippage=Slippage(value=0.00, unit="perValue")
    )
}


def initialize(context):
    context.asset_allocation = %s


def handle_data(context):
    security_account = context.get_account("security_account")
    current_universe = context.get_universe("stock", exclude_halt=False)

    for stk in current_universe:
        if stk not in security_account.get_positions():
            security_account.order_pct_to(stk, context.asset_allocation[stk])

"""