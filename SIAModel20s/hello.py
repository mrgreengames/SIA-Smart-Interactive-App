from flask import Flask
from time import sleep
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    return "This is a website!"
