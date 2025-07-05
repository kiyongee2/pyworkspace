# 서울 시청 사이트 스크래핑

import requests
from bs4 import BeautifulSoup

url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
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
