#########################################
#
# https://school.programmers.co.kr/learn/courses/30/lessons/152996?language=python3
# 어차피 최대 N 1000이라 알빠노로 풀었
#
#########################################

from collections import Counter

def plus(num):
    cnt = 0

    for i in range(num):
        cnt = cnt+i
      
    return cnt
    
def solution(weights):
    answer = 0
    counter_wei = Counter(weights)

    keys = list(counter_wei.keys())
    for i in range(len(keys)):
        answer = answer + plus(counter_wei[keys[i]])
        for j in range(i+1, len(keys)):
            a = min(keys[i], keys[j])
            b = max(keys[i], keys[j])

            if a*4 == b*2 or a*4 == b*3 or a*3 == b*2:
                answer = answer + counter_wei[a]*counter_wei[b]
            
    return answer

