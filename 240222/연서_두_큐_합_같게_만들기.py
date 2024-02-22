# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3
#
# 
# 큐가 무한으로 도는 경우 주의
# 계속 돌게 되면, 이전에 이미 계산했던 케이스가 생긴다는 걸 누군가의 풀이를 보고 알았음...
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from collections import deque

def solution(queue1, queue2):
    answer = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)

    dq1sum = sum(dq1)
    dq2sum = sum(dq2)
    
    n = len(dq1)

    if (dq1sum+dq2sum)%2==1:
        return -1
    
    target = (dq1sum+dq2sum)//2
    #print("The target: {}".format(target))

    while True:
        
        dq1head = dq1[0]
        dq2head = dq2[0]
        
        if answer >= 3*n:
            return -1

        #print("dq1head: {} dq2head: {}".format(dq1head, dq2head))
        #print("dq1sum: {} dq2sum: {}".format(dq1sum, dq2sum))
        
        if dq1head > target or dq2head > target:
            answer = -1
            break
            
        if dq1sum == dq2sum:
            break
        
        elif dq1sum > dq2sum:
            dq1sum -= dq1head
            dq2sum += dq1head
            dq2.append(dq1.popleft())
            answer+=1
        elif dq1sum < dq2sum:
            dq2sum -= dq2head
            dq1sum += dq2head
            dq1.append(dq2.popleft())
            answer+=1

        
    return answer
