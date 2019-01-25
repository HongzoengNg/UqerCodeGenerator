# -*- coding:utf-8 -*-
'''
File: ma_strategy_template.py
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
        capital_base=1000000,
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
        attribute="closePrice", time_range=%s, style="sat"
    )

    for stk in current_universe:
        short_ma = hist[stk][-%s:].mean()
        long_ma = hist[stk][:].mean()

        if (short_ma > long_ma) and (stk not in security_account.get_positions()):
            security_account.order_pct_to(stk, context.asset_allocation[stk])
        elif short_ma <= long_ma and (stk in security_account.get_positions()):
            security_account.order_to(stk, 0)

"""
