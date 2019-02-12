# -*- coding:utf-8 -*-
'''
File: validation.py
File Created: Saturday, 26th January 2019
Author: Hongzoeng Ng (kenecho@hku.hk)
-----
Last Modified: Saturday, 26th January 2019
Modified By: Hongzoeng Ng (kenecho@hku.hk>)
-----
Copyright @ 2018 KenEcho
'''
import datetime


def validate_portfolio(portfolio):
    """
    :params:
    portfolio: e.g. {"000001.XSHG": 0.25}
    """
    symbol_correct = True
    weight_correct = True
    msg = ""
    for symbol in portfolio:
        if (
            len(symbol) == 11 and symbol[:-5].isdigit() and
                (symbol.endswith(".XSHG") or symbol.endswith(".XSHE"))):
            pass
        else:
            msg += "Invalid symbol: {}\n".format(symbol)
            symbol_correct = False
        if portfolio[symbol] >= 0 and portfolio[symbol] <= 1:
            pass
        else:
            weight_correct = False
            msg += "Invalid weight: {}\n".format(portfolio[symbol])
    if symbol_correct and weight_correct:
        return msg, True
    else:
        if not weight_correct:
            msg += "Weight should between 0 and 1 (included 0 and 1)\n"
        return msg, False


def validate_date(start_date, end_date):
    date_correct = True
    msg = ""
    min_date = datetime.datetime.strptime("2010-01-01", "%Y-%m-%d")
    max_date = datetime.datetime.strptime("2019-02-01", "%Y-%m-%d")
    if start_date != "":
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        if start < min_date:
            date_correct = False
            msg += "The start cannot earlier than '2010-01-01'\n"
        if start > max_date:
            date_correct = False
            msg += "The start cannot later than '2019-02-01'\n"
    else:
        date_correct = False
        msg += "Error: The start date cannot be empty!\n"
    if end_date != "":
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if end < min_date:
            date_correct = False
            msg += "The end cannot earlier than '2010-01-01'\n"
        if end > max_date:
            date_correct = False
            msg += "The end cannot later than '2019-02-01'\n"
    else:
        date_correct = False
        msg += "Error: The end date cannot be empty!\n"
    if start_date == "" or end_date == "":
        return msg, date_correct
    else:
        if start > end:
            date_correct = False
            msg += "The start date cannot be later than the end date\n"
        elif start == end:
            date_correct = False
            msg += "The start date cannot be equal to the end date\n"
        return msg, date_correct


def validate_sma_lma(sma, lma):
    msg = ""
    ma_correct = True
    if sma != "":
        if sma < 1:
            ma_correct = False
            msg += "Short-Term value should not be less than 1\n"
        if sma > 100:
            ma_correct = False
            msg += "Short-Term value should not be greater than 100\n"
    else:
        ma_correct = False
        msg += "Error: The Short-Term value cannot be empty!\n"
    if lma != "":
        if lma < 1:
            ma_correct = False
            msg += "Long-Term value should not be less than 1\n"
        if lma > 100:
            ma_correct = False
            msg += "Long-Term value should not be greater than 100\n"
    else:
        ma_correct = False
        msg += "Error: The Long-Term value cannot be empty!\n"
    if sma == "" or lma == "":
        return msg, ma_correct
    else:
        if sma > lma:
            ma_correct = False
            msg += "The Short-Term value cannot be greater than the Long-Term value\n"
        elif sma == lma:
            ma_correct = False
            msg += "The Short-Term value cannot be equal to the Long-Term value\n"
        return msg, ma_correct
