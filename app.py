# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><img src='https://www.insight.com/content/dam/insight-web/logos/global-nav.svg' width='30%' alt='Insight'> <h1>Hello</h1><h2>Version 01<h2></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)