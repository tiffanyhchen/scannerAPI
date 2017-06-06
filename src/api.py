#Mock Malware Scanner API

from flask import Flask, request

# Instantiate the app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)