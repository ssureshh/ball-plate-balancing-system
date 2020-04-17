from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
sio = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def index():
    return render_template("index.html")

@sio.on('connect')
def connect():
    print(f'\n\n A Client Connected : {request.sid}\n\n')

@sio.on('coord_event')
def send_coord(data):
    coord_json = json.dumps(data)
    emit('coords', coord_json, broadcast=True)
    print(f'Data sent : {coord_json}')

@sio.on('des_event')
def send_des(data):
    print(f'DES : {data}')
    emit('des_client', data, broadcast=True)
@sio.on('pid_event')
def send_des(data):
    print(f'PID : {data}')
    emit('pid_client', data, broadcast=True)

if __name__ == "__main__":
    sio.run(app, debug=True, port=8000, host="0.0.0.0")


'''
Notes : 
import os
from flask_cors import CORS

template_dir = os.path.abspath('../webfiles')
static_dir = os.path.abspath('./webfiles/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/css/<path:filename>")
def route_css(filename):
    return send_from_directory("/Users/suresh/proj/major/code/python/webfiles/css", filename)
@app.route("/js/<path:filename>")
def route_js(filename):
    return send_from_directory("/Users/suresh/proj/major/code/python/webfiles/js", filename)
@app.route("/pages/<path:filename>")
def route_pages(filename):
    return send_from_directory("/Users/suresh/proj/major/code/python/webfiles/pages", filename)
'''