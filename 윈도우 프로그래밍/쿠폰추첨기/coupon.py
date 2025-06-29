# 쿠폰 추첨기
from tkinter import *
import random

def click():
  namelist = ['강감찬', '고담덕', '이순신', '장영실',
              '이도', '김구', '신사임당', '유관순',
              '서희', '허균']
  winners = [] #당첨자 저장 리스트
  while len(winners) < 3:
    winner = random.choice(namelist)  #choice - 문자열 리스트 추출(1명)
    if winner not in winners:  #이미 저장되지 않은 이름이면(중복 불허)
      winners.append(winner) #3명 저장

  output.delete(0.0, END)
  output.insert(END, winners)

window = Tk()
window.title("쿠폰 추첨기")
window.option_add("*font", "System 12")

# 이미지 파일 넣기 - PhotoImage 클래스 사용
# 라벨 위에 이미지 올리기 
lbl_img = Label(window)
img = PhotoImage(file = "bronx.png") 
lbl_img.config(image = img)
lbl_img.grid(row=0, column=0, sticky=W)

# 추첨 버튼
Button(window, text="추첨", command=click) \
  .grid(row=1, column=0, sticky=W)

# 당첨자 출력
output = Text(window, width=41, height=8, bg='orange')
output.grid(row=2, column=0, sticky=W)

window.mainloop()