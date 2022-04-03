from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_post_data(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    if not data.get('name') or not isinstance(data['name'], str):
        return False
    if not data.get('age') or not isinstance(data['age'], int):
        return False
    return True

@app.route('/', methods=['GET'])
def hello():
    return "Hello world"

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({'status': 'test'})
    elif request.method == 'POST':
        if validate_post_data(request.json):
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'bad input'}), 400

def main():
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()