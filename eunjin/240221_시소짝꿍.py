'''
1. 정렬
2. 중복의 개수를 구하기. 중복이 x개일 경우
-> res += x * x-1 / 2 연산하기 (중복인 수끼리 쌍)
-> dic[num * 2] = y + x개
-> dic[num * 3] = y + x개
-> dic[num * 4] = y + x개
res += y * x

ex) res += y * x인 이유
dic[24] = 2개
6, 8 (old)
12 12 12 (new) -> 2개*3 = 6쌍

문제ex)
100 100 180 270 360
100, 100 -> 2 * 1 / 2 = 1쌍

200 : 2
300 : 2
360 : 1
400 : 2
540 : 2
720 : 2
810 : 1
1080 : 2
1440 : 1
'''

from collections import defaultdict

def solution(weights):
    dic = defaultdict(int)
    weights = sorted(weights)
    weights.append(-1)
    
    res = 0
    cnt = 1
    prev = -1
    
    for weight in weights:
        if prev == weight:
            cnt += 1
            continue
            
        else:
            res += cnt * (cnt-1) / 2 
            res += dic[prev*2] * cnt + dic[prev*3] * cnt + dic[prev*4] * cnt
            
            dic[prev*2] += cnt
            dic[prev*3] += cnt
            dic[prev*4] += cnt
            
            cnt = 1
            prev = weight
        
    return res

