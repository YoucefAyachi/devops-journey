if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)  # service name 'redis'

@app.route('/')
def home():
    count = cache.incr('hits')
    return f"Hello Youcef! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
