# -*- coding:utf-8 -*-
'''
File: template_generator.py
File Created: Wednesday, 23rd January 2019
Author: Hongzoeng Ng (kenecho@hku.hk)
-----
Last Modified: Wednesday, 23rd January 2019
Modified By: Hongzoeng Ng (kenecho@hku.hk>)
-----
Copyright @ 2018 KenEcho
'''
import json
from src.templates import *
from utils.validation import validate_sma_lma


class Template_Generator(object):
    def __init__(self):
        pass

    def _ma_code_fill_in(self, start, end, str_portfolio, short_ma=5, long_ma=20):
        """
        start: str, "2018-01-01"
        end: str, "2019-01-01"
        str_portfolio: str, '{"00001.XSHE": 0.5, "000002.XSHE": 0.5}'
        """
        portfolio_dict = json.loads(str_portfolio)
        symbols = str(list(portfolio_dict.keys()))
        get_ma_code = moving_average_code % (
            start,
            end,
            symbols,
            long_ma,
            str_portfolio,
            short_ma
        )
        return get_ma_code

    def _macd_code_fill_in(self, start, end, str_portfolio, short_win=12, long_win=26, macd_win=9):
        portfolio_dict = json.loads(str_portfolio)
        symbols = str(list(portfolio_dict.keys()))
        get_macd_code = macd_code % (
            start,
            end,
            symbols,
            90,
            str_portfolio,
            short_win,
            long_win,
            macd_win
        )
        return get_macd_code

    def _stoch_code_fill_in(self, start, end, str_portfolio, fast_k=14, slow_k=3, slow_d=3):
        portfolio_dict = json.loads(str_portfolio)
        symbols = str(list(portfolio_dict.keys()))
        get_stoch_code = stochastic_oscillator_code % (
            start,
            end,
            symbols,
            90,
            str_portfolio,
            fast_k,
            slow_k,
            slow_d
        )
        return get_stoch_code
    
    def _buyhold_code_fill_in(self, start, end, str_portfolio):
        portfolio_dict = json.loads(str_portfolio)
        symbols = str(list(portfolio_dict.keys()))
        get_buyhold_code = buy_hold_code % (
            start,
            end,
            symbols,
            str_portfolio
        )
        return get_buyhold_code

    def generate(self, strategy, args):
        """
        :params:
        strategy: str, "ma_5_10", ...
        """
        if strategy.startswith("ma_"):
            params = strategy.split("_")
            sma = int(params[1])
            lma = int(params[2])
            msg, valid = validate_sma_lma(sma, lma)
            if valid:
                args["short_ma"] = str(sma)
                args["long_ma"] = str(lma)
                return self._ma_code_fill_in(**args)
            else:
                return msg
        elif strategy.startswith("macd_"):
            params = strategy.split("_")
            short_win = int(params[1])
            long_win = int(params[2])
            macd_win = int(params[3])
            msg, valid = validate_sma_lma(short_win, long_win)
            if valid:
                args["short_win"] = str(short_win)
                args["long_win"] = str(long_win)
                args["macd_win"] = str(macd_win)
                return self._macd_code_fill_in(**args)
            else:
                return msg
        elif strategy.startswith("stoch_"):
            params = strategy.split("_")
            fast_k = int(params[1])
            slow_k = int(params[2])
            slow_d = int(params[3])
            msg, valid = validate_sma_lma(slow_d, fast_k)
            if valid:
                args["fast_k"] = str(fast_k)
                args["slow_k"] = str(slow_k)
                args["slow_d"] = str(slow_d)
                return self._stoch_code_fill_in(**args)
            else:
                return msg
        elif strategy == "buyhold":
            return self._buyhold_code_fill_in(**args)
