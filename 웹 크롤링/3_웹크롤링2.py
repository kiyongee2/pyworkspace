# 서울 시청 사이트 스크래핑

import requests
from bs4 import BeautifulSoup

url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')

# select_one("태그이름.선택자이름") - 처음 요소 찾음
first_li = html.select_one('li.public')
print(first_li.text)

# select('태그이름.선택자이름 > 하위태그 > 하위태그')
all_li = html.select('div.m_service ul li')
# print(all_li)
print(all_li[-2].text) # 평생학습포털

"""
first_li = html.find('li', attrs={'class': 'public'})
# print(first_li)

# 모든 li 찾기
div = html.find('div', attrs={'class': 'm_service'})
all_li = div.find_all('li')
# print(all_li)
print(all_li[2].text)  # 서울일자리
print(all_li[-2].text) # 평생학습포털

# 전체 서비스 출력
# for li in all_li:
#   print(li.text)
"""