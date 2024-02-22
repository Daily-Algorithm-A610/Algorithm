####################################################################################
#
#  https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=python3
#
####################################################################################

def solution(arr):
    global count
    press(0,0, int(len(arr[0])), arr)
    return count

def press(y, x, size, area):

    global count

    if canRec(y,x,size, area) is False:
        if area[y][x] == 1 : count[1] = count[1]+1
        else: count[0] = count[0]+1
        return

    press(y,x,int(size/2), area)
    press(y,x+int(size/2), int(size/2), area)
    press(y+int(size/2), x, int(size/2), area)
    press(y+int(size/2), x+int(size/2), int(size/2), area)


def canRec(y,x,size, area):

    target = area[y][x]

    for i in range(y, y+size):
        for j in range(x, x+size):
            if area[i][j] != target: return True

    return False

count = [0,0]





