from crypt import methods
from flask import Flask, request, jsonify
import json
from QuestionAnswering import get_answer_using_bert

app = Flask(__name__)

@app.route('/')
def index():
    json = {
        'data': [],
        'message': 'Success testing the API!',
        'status_code': 200,
    }
    return jsonify(json)

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()