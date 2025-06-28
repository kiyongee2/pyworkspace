# 체크 버튼 만들기
# 목록 버튼 - CheckButton()

# from tkinter import *  # '*' - 모든 클래스와 함수를 지칭
import tkinter as tk  #tk 별칭 사용

# 체크 버튼 동작 구현
"""
def click():
  if ck_val.get() == True:
    print("체크 되었슴")
  else:
    print("해제 되었슴")

window = tk.Tk() # Tk() 클래스의 인스턴스(window) 생성
window.title("목록 버튼")
window.geometry("250x200")

# 체크 버튼 클래스에서 생성,  pack() - 가운데 배치
# variable(변수)
ck_val = tk.BooleanVar() #True or False를 저장함
ck_val.set(False)

tk.Checkbutton(text="체크 버튼", font=("System", 13),
        variable=ck_val, command=click).pack()

window.mainloop()
"""

# 목록 (취미) 만들기
def click():
  result = "* 선택된 취미\n\n"  #취미 저장
  for i in range(n):
    if ck_val[i].get():
      result += f"{hobby[i]} " #체크 목록이 더해짐
  lbl_result.config(text=result)

window = tk.Tk() # Tk() 클래스의 인스턴스(window) 생성
window.title("취미 목록 만들기")
window.geometry("250x300")

hobby = ["독서", "운동", "게임", "등산"]
ck_val = [None, None, None, None] #ck_val 초기화
ck_btn = [None] * 4               #ck_btn 초기화

n = len(hobby)
for i in range(n): #0부터 n-1 까지 반복
  ck_val[i] = tk.BooleanVar() #True or False를 저장함
  ck_val[i].set(False)
  ck_btn[i] = tk.Checkbutton(window, text=hobby[i], font=("System", 13),
          variable=ck_val[i])
  # 좌표로 이동하는 함수 - place(x = ?, y = ?)
  ck_btn[i].place(x = 100, y = 20 + (30 * i)) #y: 20, 50, 80, 110


# 확인 버튼
tk.Button(window, text="확인", command=click).place(x = 110, y = 160)

# 결과 표시 레이블
lbl_result = tk.Label(window, text="", font=("System", 13))
lbl_result.place(x = 50, y = 200)

window.mainloop()

















