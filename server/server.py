from flask import Flask, render_template, Response, jsonify, request, json
from flask_cors import CORS
from ner import NER

import re

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'I am your super flask server'


@app.route('/format_text', methods=['POST'])
def format_text():
    req = request.get_data()
    req = json.loads(req)
    text = req['text']
    
    text = re.sub(r'●', '.', text)
    text = re.sub(r'○', '.', text)
    text = re.sub(r'•', '.', text)

    global ner
    ner = NER(text)

    formated_text_output = ner.get_formated_text()
    # ner.get_predictions(formated_text_output['result'])
    return jsonify(compiled_result=formated_text_output, success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True,
            use_reloader=False, debug=True)
