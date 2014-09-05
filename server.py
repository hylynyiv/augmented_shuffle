from flask import Flask, url_for, redirect, request
import sys
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    env = "dev"
    if len(sys.argv) > 1:
        env = sys.argv[1]
    if env == "dev":
        app.run(host='0.0.0.0', port=3000, debug = True)
    else:
        app.run(host='0.0.0.0', port=80)
