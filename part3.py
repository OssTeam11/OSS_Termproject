criteria = ['pass', 'warning', 'stop']
x = 0
y = 0
w = 0
h = 0
frame = abs(x-w) * abs(y-h)
# 시작점 좌표(x1,y1) , 종료점 좌표(x2,y2) 절댓값으로 거리차이 계산 => 프레임의 각 변의 길이 알 수 있음
# 프레임 길이 -> 넓이구하기 -> 넓이가 커질수록 거리가 가까움 -> 거리에 따른 기준 출력
def frame_if():
    if frame < 50:
        print(criteria[0])
    elif frame < 70:
        print(criteria[1])
    elif frame < 100:
        print(criteria[2])


frame_if()