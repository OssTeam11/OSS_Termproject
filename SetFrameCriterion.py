criteria = ['pass', 'warning', 'stop']
frame = 0
status =" "

def frame_if(status):
    if frame < 50:
        print(criteria[0])
    elif frame < 70:
        print(criteria[1])
    elif frame < 100:
        print(criteria[2])

print(hello)
frame_if()