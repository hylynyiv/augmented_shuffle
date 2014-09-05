from flask import Flask, url_for, redirect, request
import sys
import os
from json import JSONEncoder
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/playlist/<username>', methods=['GET'])
def playlist(username):
    fake_data= open('fake.json')
    return json.dumps(json.loads(fake_data.read()))

@app.route('/credentials/<username>', methods=['GET'])
def credentials(username):
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    return JSONEncoder().encode({ "client_id": client_id, "client_secret": client_secret})

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

if __name__ == '__main__':
    env = "dev"
    if len(sys.argv) > 1:
        env = sys.argv[1]
    if env == "dev":
        app.run(host='0.0.0.0', port=3000, debug = True)
    else:
        app.run(host='0.0.0.0', port=80)
