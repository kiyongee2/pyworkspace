# 거북이 대포 게임

import turtle as t
import random

# 키보드 작동 함수
def turn_up():
  t.left(2)  #왼쪽으로 2도 이동

# 키보드 작동 함수
def turn_down():
  t.right(2) #오른쪽으로 2도 이동

# 포탄 발사 함수
def fire():
  ang = t.heading()  #거북이가 바라보는 현재 각도
  # 포탄이 땅 위에 있음(땅에 떨어지지 않는 동안)
  while t.ycor() > 0: #ycor()- y좌표, xcor() - x좌표
    t.forward(15) #직진 15픽셀
    t.right(5) #오른쪽 5도 방향

  d = t.distance(target, 0) #포탄과 목표지점과의 거리
  # t.write(d)
  t.sety(random.randint(10, 100))  #y좌표 설정 - 성공, 실패를 표시할 위치 지정
  if d < 25: #목표 지점에 닿으면
    t.color('blue')
    # 문자열 쓰기 - 글꼴 크기 15, False-포탄의 위치를 옮기지 않음
    t.write("Good!", False, 'center', ('', 15))
  else:
    t.color('red')
    t.write("Bad!", False, 'center', ('', 15))
    t.color('black')
    t.goto(-200, 10)
    t.setheading(ang) #처음 기억한 각도로 되돌림

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점(50픽셀) - 랜덤
target = random.randint(50, 150) #50 ~ 150 사이
t.color('green')
t.pensize(3)
t.up() #펜 올리기
t.goto(target-25, 1)
t.down() #펜 내리기
t.goto(target+25, 1)

# 포탄(화살 모양) - 거북이의 위치
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)  #포탄의 머리 각도

# 키보드 작동 
t.onkeypress(turn_up, "Up") #함수 호출시 소괄호 생략
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space") #스페이스 키를 누르면 발사
t.listen() #키보드 작동 실행

t.mainloop()