import random


def check(studentid):
    print("ENTERED ANNOYANCE CHECKER")
    chance= random.randint(1, 10)
    if studentid== 'Beginner':
        if chance <= 7:
            return 1
        elif chance >7:
            return 0
    elif studentid== 'Intermediate':
        half=random.randint(0,1)
        return half
    elif studentid=='Expert':
        if chance <=3:
            return 1
        elif chance >3:
            return 0


