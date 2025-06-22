# 입력과 출력
# 입력 - Entry(), 출력 - Text()
import tkinter as tk

root = tk.Tk()
root.title("입력과 출력")
root.geometry("250x200+200+300")

# 이름 입력받기
tk.Label(root, text="이름: ", height=3, font=("System", 12)).grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

# 버튼을 눌러 출력하기 - columnspan=2(병합)
tk.Button(root, text="확인", width=10, height=2).grid(row=1, columnspan=2)
tk.Label(root, text="").grid(row=2, column=0)  #빈 레이블 추가
tk.Text(root, width=20, height=3).grid(row=3, columnspan=2)

root.mainloop()


