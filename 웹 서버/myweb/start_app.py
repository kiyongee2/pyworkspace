# 플라스크 웹 서버

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')


app.run()

