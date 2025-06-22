import turtle as t

# 다각형 그리기
"""
def polygon(n):
  for x in range(n):
    t.forward(50)
    t.left(360/n)

def polygon2(n, d):
  for x in range(n):
    t.forward(d)
    t.left(360/n)

polygon(3)  #다각형 함수 호출
polygon(5)

# 다른 위치에 그리기
t.up()  #펜 올리기
t.forward(100)
t.down() #펜 내리기

polygon2(3, 100)
polygon2(5, 100)
"""

# 키보드 조종하기
# 오른쪽 방향 
def turn_right():
  t.setheading(0)  #거북이 머리 방향
  t.forward(10)

# 위쪽 방향
def turn_up():
  t.setheading(90)
  t.forward(10)

# 왼쪽 방향
def turn_left():
  t.setheading(180)
  t.forward(10)

# 아래 방향
def turn_down():
  t.setheading(270)
  t.forward(10)

t.shape('turtle')
# 화살표 키 동작 - 상수로 지정, 첫글자 대문자임
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen() #실행(작동)

t.mainloop()


