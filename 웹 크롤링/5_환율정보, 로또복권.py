# 환율 정보 크롤링하기
import requests
from bs4 import BeautifulSoup

# 환율정보
"""
url = "https://finance.naver.com/marketindex/"
resp = requests.get(url)
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")
# select() 함수 사용
all_li = soup.select("div.market1 ul li")
# print(all_li)

# 환율 종류 - select_one() : 1개 선택
exchange = soup.select_one("span.blind")
# print(exchange.text)

# 환율 지수
value = soup.select_one("span.value")
# print(value.text)

# 환율 전체 출력
for li in all_li:
  exchange = li.select_one("span.blind")
  value = li.select_one("span.value")
  # 공백문자로 텍스트 분리 - 리스트 반환
  # text 대신 string 가능
  print(exchange.string.split(' ')[-1], value.string)

"""

# 로또 복권 당첨 번호 확인
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

# 최신 회차
"""
latest_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
resp = requests.get(latest_url)

soup = BeautifulSoup(resp.text, "html.parser")
# select() : 2개 이상 - 리스트 반환
win_nums = soup.select('div.nums span')
# print(win_nums)

# for num in win_nums:
#   print(num.text)

# 당첨 번호, 보너스 번호
# win_num_list = []
# for num in win_nums:
#   win_num_list.append(num.text)

# 리스트 내포
win_num_list = [num.text for num in win_nums]
print(win_num_list) # ['3', '16', '18', '24', '40', '44', '21']

print("당첨 번호")
print(win_num_list[:-1]) #실제 0 ~ -2 인덱스

print("보너스 번호")
print(win_num_list[-1]) 
"""

# 회차 선택
'''
num = 1178
url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html.parser")
win_nums = soup.select('div.nums span')

# 당첨 번호, 보너스 번호
win_num_list = [num.text for num in win_nums]

print("당첨 번호")
print(win_num_list[:-1]) #실제 0 ~ -2 인덱스

print("보너스 번호")
print(win_num_list[-1]) 
'''
# 윈도우 앱 만들기

def lotto_win():
  try:
    num = int(entry.get()) #입력된 회차 번호 가져옴
    if num <= 0 or num > 1180:
      messagebox.showerror("오류", "회차가 없습니다.")
      entry.delete(0, END)  # 입력 초기화 
      output.delete(0.0, END) # 출력 초기화 
      return #즉시 종료(실행 중단)

    # 웹 크롤링
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, "html.parser")
    win_nums = soup.select('div.nums span')

    # 당첨 번호, 보너스 번호
    win_num_list = [num.text for num in win_nums]

    # 출력
    output.delete(0.0, END)
    output.insert(END, f"당첨 번호: {win_num_list[:-1]} \
                    \n\n보너스 번호: {win_num_list[-1]}")
  except ValueError:
    messagebox.showerror("오류", "유효한 숫자를 입력하세요.")
    entry.delete(0, END)  # 입력 초기화 
    output.delete(0.0, END) # 출력 초기화 

window = Tk()
window.title("로또복권 당첨확인")

Label(window, text="당첨 회차 입력: ") \
  .grid(row=0, column=0, sticky=W)
# 입력 상자
entry = Entry(window, bg="yellow")
entry.grid(row=1, column=0, sticky=W)

Button(window, text="당첨번호 확인", command=lotto_win) \
  .grid(row=2, column=0, sticky=W)
# 출력상자
output = Text(window, bg="lightgreen", width=50, height=6)
output.grid(row=3, column=0, sticky=W)

window.mainloop()








