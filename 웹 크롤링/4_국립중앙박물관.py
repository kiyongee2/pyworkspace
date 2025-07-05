# 국립 중앙 박물관 관람 정보
import requests
from bs4 import BeautifulSoup

url = "https://www.museum.go.kr/MUSEUM/contents/M0101000000.do?menuId=tour-guidance"
response = requests.get(url)

html = BeautifulSoup(response.text, "html.parser")

# 관람 시간
first_ul = html.select_one('ul.display-content')
# print(first_ul)
# print(first_ul.text)

# 전체 관람 안내
# '>' - 자식 태그, ' ' - 공백은 후손 태그(범위가 넓다)
contents = html.select('ul.display-content-area > li > ul')
# contents = html.select('ul.display-content-area li ul')
print(contents)

# for content in contents:
#   print(content.text)

# 관람료
# print(contents[2].text)