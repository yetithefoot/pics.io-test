# flask_web/app.py

from flask import Flask
from flask import render_template, request, jsonify
import os
app = Flask(__name__)

@app.route('/logs')
def get_logs():
    accessLogs = open("/var/log/nginx/access.log", "r").read()
    return accessLogs

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def hello_world(path):
    contents = dict(request.headers)
    contents.update(path=path)
    reqMethod = request.method
    return render_template('index.html',
                            title="HTTP request params",
                            contents=contents,
                            method=reqMethod)


if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)
