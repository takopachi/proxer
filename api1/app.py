from flask import Flask
app = Flask(__name__)

@app.route('/api1')
def pong():
    return 'PONG from API1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
