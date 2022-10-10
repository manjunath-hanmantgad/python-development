from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/test')
def test():
    return "this is a test output"

if __name__ == '__main__':
    app.run()