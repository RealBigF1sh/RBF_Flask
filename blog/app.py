from flask import Flask

app = Flask(__name__)

@app.route("/<name_1>/<name_2>")
def index(name_1:str, name_2:str):
    return f'Hello, {name_1+name_2}'