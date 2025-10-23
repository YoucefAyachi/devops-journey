from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Youcef, your first Docker app works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
