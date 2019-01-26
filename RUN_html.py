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
    render_template
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
    params.pop("")
    key_with_empty = []
    strategy = params["strategy"]
    params.pop("strategy")
    for key in params:
        if params[key] == "":
            key_with_empty.append(key)
        else:
            params[key] = float(params[key])
    for key in key_with_empty:
        params.pop(key)
    args = {
        "start": start_date,
        "end": end_date,
        "str_portfolio": json.dumps(params)
    }
    code = ""
    if args['start'] == "":
        code += "Error: The start date cannot be empty!\n"
    if args['end'] == "":
        code += "Error: The end date cannot be empty!\n"
    if args['str_portfolio'] == "{}":
        code += "Error: At least 1 symbol should be input!\n"
    if args['start'] != "" and args['end'] != "" and args['str_portfolio'] != "":
        tg = Template_Generator()
        code = tg.generate(strategy, args)
    response = {
        'code': code
    }
    return jsonify(response), 200


@app.route("/ucg")
def display():
    return render_template("index.html")


if __name__ == "__main__":
    args = parser.parse_args()
    port = args.port
    app.run(host=ADDRESS, port=port)
