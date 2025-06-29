# 짝수/홀수 판정 프로그램

from tkinter import *

def click():
  # 입력 받은 문자를 숫자형으로 변환
  try:
    num = int(entry.get())
    if num % 2 == 0:
      text.insert(END, "짝수")
    else:
      text.insert(END, "홀수")
  except ValueError: #문자가 입력될 경우 에러처리
    text.delete(0.0, END)
    text.insert(END, "오류")

def reset():
  entry.delete(0, END)  #한 줄(0번 인덱스)
  text.delete(0.0, END) #0-첫째줄, 0-첫번째 문자

root = Tk()
root.title("짝수/홀수 판정")
root.geometry("300x200+300+200")
root.option_add("*font", "System 12")

# 입력, 출력 프레임 
# pady() : y축(위, 아래) 바깥 여백, padx() : x축(왼쪽, 오른쪽) 바깥여백
io_frame = Frame(root)
io_frame.pack(pady=20)

# 입력
Label(io_frame, text="숫자 입력: ").grid(row=0, column=0)
entry = Entry(io_frame, width=15) #한 줄 입력 
entry.grid(row=0, column=1)

# 출력
Label(io_frame, text="결과").grid(row=1, column=0)
text = Text(io_frame, width=15, height=2)
text.grid(row=1, column=1)

# 버튼 프레임
btn_frame = Frame(root)
btn_frame.pack(pady=10)

# pack() - 한 줄 차지, side=LEFT(왼쪽에 배치, 오른쪽 버튼도 왼쪽 배치 속성)
Button(btn_frame, text="판정", command=click).pack(side=LEFT, padx=5)
Button(btn_frame, text="초기화", command=reset).pack(side=LEFT, padx=5)

root.mainloop()






'''
num = int(input("숫자 입력: "))

# 2, 4, 6, 8... -> 2의 배수(2로 나눈 나머지 0) - %연산자
if num % 2 == 0:
  print("짝수")
else:
  print("홀수")

'''