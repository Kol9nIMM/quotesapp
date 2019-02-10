from flask import Flask,jsonify
import json

app = Flask(__name__)

json_dict = {'text': 'text', 'author': 'author'}


def write_json(data):
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


@app.route('/')
@app.route('/getquote', methods=['GET', 'POST'])
def getquote():
    write_json(json_dict)
    return jsonify(json_dict)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
