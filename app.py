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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_json = request.get_json()
        query = input_json['query']
        context_list = input_json['context_list']
        for val in context_list:
            context = val['context']
            context = context.replace('\n', '')
            prediction = get_answer_using_bert(context, query)
            json = {
                'results': [
                    {
                        'answers': prediction,
                        'id': val['id'],
                        'question': query,
                    }
                ]
            }
        return jsonify(json)
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run()