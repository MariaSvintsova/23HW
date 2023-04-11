import os

from flask import Flask, request, abort, jsonify

from utils import commands

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    answer = ""
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')
        value2 = request.args.get('value2')
        file_name = request.args.get('file_name')
        with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as file:
            data = file.readlines()
        result = commands(cmd1, value1, data)
        answer = commands(cmd2, value2, result)
    except Exception:
        abort(400)
    return jsonify(answer)
