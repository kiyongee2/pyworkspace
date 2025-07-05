# 플라스크 - 웹 프레임워크 
# Flask 설치 - pip install Flask
from flask import Flask

app = Flask(__name__) #app 인스턴스 생성

@app.route('/') #http://127.0.0.1:5000/
def index():
  return "Hello~ Flask!"

@app.route("/login") #http://127.0.0.1:5000/login
def login():
  return "<h2>로그인 페이지입니다.</h2>"

app.run()
