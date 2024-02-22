'''
https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3

popleft 및 append 까지가 1회

1. 모든 원소의 합이 홀수인 경우 -1
2. 짝수인 경우, 본론 시작

ex1)
queue1의 합 14 -> 목표 15
queue2의 합 16 -> 목표 15

3 2 7 2 -> 합 12 -> 목표 15보다 작으므로 queue2에서 가져오기 
3 2 7 2 4 -> 합 16 -> 목표 15보다 크므로 popleft
2 7 2 4 -> 합 15 (총 2회, 끝)
'''

from collections import deque

def solution(queue1, queue2):
    sum_queue1 = sum(queue1)
    sum_queue = sum_queue1 + sum(queue2)
    
    if sum_queue % 2: # 홀수
        return -1
    
    target = sum_queue // 2
    len_queue = len(queue1) + len(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    for cnt in range(len_queue + 5):
        if sum_queue1 == target:
            return cnt
        elif sum_queue1 < target:
            x = queue2.popleft()
            queue1.append(x)
            sum_queue1 += x
        elif sum_queue > target:
            x = queue1.popleft()
            queue2.append(x)
            sum_queue1 -= x
    
    return -1
