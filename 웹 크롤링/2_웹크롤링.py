# bs4 라이브러리 설치
# BeautifulSoup 클래스 
from bs4 import BeautifulSoup

html_str = """
<html>
  <body>
    <ul class="item">
      <li>인공지능</li>
      <li>빅데이터</li>
      <li>로봇공학</li>
    </ul>
    <ul class="lang">
      <li>Python</li>
      <li>C/C++</li>
      <li>Java</li>
    </ul>
  </body>
</html>
"""
# html 파싱
soup = BeautifulSoup(html_str, "html.parser")

#처음 나오는 ul태그 찾음
first_ul = soup.find('ul') 
# print(first_ul) #html 찾음
print(first_ul.text) #html을 제외한 문자 출력

# <li>태그 - 리스트 형태로 찾음 - find_all()
all_li = first_ul.find_all('li')
print(all_li) #[<li>인공지능</li>, <li>빅데이터</li>, <li>로봇공학</li>]
print(all_li[1].text) #빅데이터

# 모든 텍스트 출력
for li in all_li:
  print(li.text)

# 두번째 <ul> 태그 찾음
second_ul = soup.find('ul', attrs={'class': 'lang'})
# print(second_ul)
print(second_ul.text)