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
from src.ma_strategy_template import moving_average_code


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
        ma_code = moving_average_code % (
            start,
            end,
            symbols,
            long_ma,
            str_portfolio,
            long_ma,
            short_ma
        )
        return ma_code

    def generate(self, strategy, args):
        """
        :params:
        strategy: str, "ma", ...
        """
        if strategy == "ma":
            return self._ma_code_fill_in(**args)
        elif strategy == "b":
            return "Strategy B is unavailable yet."
        elif strategy == "c":
            return "Strategy C is unavailable yet."