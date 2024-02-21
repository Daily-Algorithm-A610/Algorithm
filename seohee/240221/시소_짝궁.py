#########################################
#
# https://school.programmers.co.kr/learn/courses/30/lessons/152996?language=python3
# 통과 못함 ㅠㅠ 서러움
#
#########################################


def solution(weights):
    answer = 0
    
    for w in set(weights):
        count = weights.count(w) 
        if(count > 1):
            answer += count*(count-1)/2

    weights = list(set(weights)) # 중복 제거
    weights.sort()
    for i in range(len(weights)-1): # 비교할 왼쪽
        for d in range(i+1, len(weights)): # 오른쪽
            s = weights[i] #작은거
            l = weights[d] #큰거
            if(4*s == 3*l or 4*s == 2*l or 3*s == 2*l): #경우의 수 3가지 ( 44 33 22 는 같지 않으면 없음)
                answer += 1 
                
    return answer

