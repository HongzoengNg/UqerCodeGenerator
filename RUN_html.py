# -*- coding:utf-8 -*-
'''
File: api.py
File Created: Friday, 25th January 2019
Author: Hongzoeng Ng (kenecho@hku.hk)
-----
Last Modified: Friday, 25th January 2019
Modified By: Hongzoeng Ng (kenecho@hku.hk>)
-----
Copyright @ 2018 KenEcho
'''
import json
from src.template_generator import Template_Generator
from argparse import ArgumentParser
from flask import (
    Flask,
    jsonify,
    request,
    redirect,
    url_for,
    abort,
    render_template
)
from utils.validation import (
    validate_date,
    validate_portfolio
)
ADDRESS = "127.0.0.1"
DEFAULT_PORT = 5000


parser = ArgumentParser()
parser.add_argument(
    '-p', '--port', default=DEFAULT_PORT, type=int, help='port to listen on'
)


# initialization
app = Flask(__name__)


# generating codes
@app.route('/generate', methods=['POST'])
def generate_code():
    params = request.get_json()
    start_date = params['start'][:-6]
    params.pop('start')
    end_date = params['end'][:-6]
    params.pop('end')
    strategy = params["strategy"]
    params.pop("strategy")
    for key in params:
        params[key] = float(params[key])
    valid_port_msg, valid_port_boolen = validate_portfolio(params)
    valid_date_msg, valid_date_boolen = validate_date(start_date, end_date)
    str_portfolio = json.dumps(params)
    if valid_port_boolen and valid_date_boolen and str_portfolio != "{}":
        args = {
            "start": start_date,
            "end": end_date,
            "str_portfolio": str_portfolio
        }
        tg = Template_Generator()
        code = tg.generate(strategy, args)
    else:
        code = valid_date_msg + valid_port_msg
        if str_portfolio == "{}":
            code += "At least 1 symbol should be input\n"
    response = {
        'code': code
    }
    return jsonify(response), 200


@app.route("/")
def index():
    return redirect(url_for("display"))


@app.route("/ucg")
def display():
    return render_template("index.html")


if __name__ == "__main__": 
    args = parser.parse_args()
    port = args.port
    app.run(host=ADDRESS, port=port)
