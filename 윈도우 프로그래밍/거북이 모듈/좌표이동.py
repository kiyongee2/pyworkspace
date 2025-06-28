import turtle as t
import time  #sleep()

# 좌표 이동 - turtle.goto(x, y)

t.shape("turtle")
# t.up()  #펜 올리기
# t.speed(0) #가장 빠른 속도(0 ~ 10)
# t.goto(200, 0) #x좌표: 200, y좌표 0
# t.goto(0, 200)

import turtle as t
import time  #sleep()
import random

# 직선 그리기
"""
t.down() #펜 내리기
t.goto(-200, 0) #200픽셀
t.goto(200, 0)  #200픽셀
"""

# 사각형 그리기
'''
t.goto(0, 0)
time.sleep(1)  #대기 시간 1초
t.goto(-100, 0)
time.sleep(1)
t.goto(-100, -100)
time.sleep(1)
t.goto(0, -100)
time.sleep(1)
t.goto(0, 0)
'''

# 랜덤 위치 지정
x = random.randint(-250, 250)
y = random.randint(-250, 250)

# t.up()
# t.goto(x, y)

# 마음대로 걷는 거북이
# 거북이의 머리 방향(각도) - 랜덤
t.speed(0) #10보다 빠름 - 0
n = 200  #반복 횟수
for i in range(n):
  ang = random.randint(1, 360)
  t.setheading(ang) #머리 방향
  t.forward(20)


t.mainloop()

