# 처음 만드는 윈도우
from tkinter import *  #'*'-모든 클래스, 함수

def click():
  print("안녕~ 파이썬!")

root = Tk() #Tk 클래스의 인스턴스 생성
root.title("첫 윈도우")
root.geometry("250x80")  #너비-100pixel, 높이-50p

# 라벨 생성
# pack() - 가운데 배치(한 줄을 차지함)
Label(root, text="Hello~ Python!!").pack()

# 버튼 생성
# command - 함수에 명령을 내림
Button(root, text="확인", command=click).pack()

root.mainloop()



