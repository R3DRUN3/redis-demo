from redis import Redis
from flask import Flask, request, jsonify


FLASK_PORT = 8754
REDIS_PORT = 6379

app = Flask(__name__)

redis = Redis(host='redis', port=REDIS_PORT)

#Root endpoint: implement a counter via redis
@app.route('/')
def home():
    redis.incr('hits') # Increments redis counter
    counter = str(redis.get('hits'),'utf-8') # get current redis counter value
    return f'This webpage has been viewed {counter} time(s)'

#GET Key endpoint: return current value of "my-key" key
@app.route('/key', methods=['GET'])
def get_key():
    key = redis.get("my-key")
    if (key is None):
        return jsonify(
            status=False,
            message='Key not found, you need to save a value first!'
        ), 404
    else:
        return key
    
#POST Key endpoint: set a new value for "my-key" key
@app.route('/key', methods=['POST'])
def create_key():
    try:
        data = request.get_json(force=True)
        key = data['key']
        redis.set("my-key", key)
        return jsonify(
            status=True,
            message='Key saved successfully!'
        ), 201
    except Exception as e:
        return jsonify(
            status=False,
            error=repr(e) 
        ), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8754)