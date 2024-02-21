# programmers : 시소 짝꿍 

from collections import defaultdict

def solution(weights):
    answer = 0
    
    wd = defaultdict(int)
    for weight in weights:
        wd[weight] += 1
    
    for w, n in wd.items():
        if n > 1:
            answer += n * (n-1) / 2
        if w * 2 in wd:
            # w * 4 / 2
            answer += n * wd[w*2]
        if w * 4 / 3 in wd:
            answer += n * wd[w*4/3]
        if w * 3 / 2 in wd:
            answer += n * wd[w*3/2]
            
    return answer
