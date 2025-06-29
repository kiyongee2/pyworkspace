# 웹 페이지 요청(request) - 모듈(requests)
import requests

# address(도메인) - https://www.python.org
# url - 도메인의 디렉터리 경로까지 포함 https://www.python.org/downloads/

url = "https://www.python.org"
response = requests.get(url)  #응답
# print(response) #Response [200]> 200 - 페이지 요청 성공, 404 - 페이지 없음
# print(response.text)  #웹 페이지의 html 요소 출력

urls = ["https://www.python.org/", "https://www.google.com/"]
filename = "robots.txt"

# print(urls[0] + filename) #https://www.python.org/robots.txt
for url in urls:
  url_path = url + filename #url 경로
  print(url_path)
  response = requests.get(url_path)
  print(response)



