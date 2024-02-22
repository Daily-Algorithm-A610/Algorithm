#########################################
#
# https://school.programmers.co.kr/learn/courses/30/lessons/152996?language=python3
# 
#
#########################################



def solution(weights):
    answer = 0
    
    for w in set(weights):
        count = weights.count(w) 
        if(count > 1):
            answer += count*(count-1)/2
    wSet = list(set(weights)) # 중복 제거
    wSet.sort()
    for i in range(len(wSet)-1): # 비교할 왼쪽
        for d in range(i+1, len(wSet)): # 오른쪽
            s = wSet[i] #작은거
            l = wSet[d] #큰거
            if(4*s == 3*l or 4*s == 2*l or 3*s == 2*l): #경우의 수 3가지 ( 44 33 22 는 같지 않으면 없음)
                print(s, l)
                #print(weights.count(s), weights.count(l))
                answer += weights.count(s) * weights.count(l)
                
    return answer

solution([100,180,360,100,270])