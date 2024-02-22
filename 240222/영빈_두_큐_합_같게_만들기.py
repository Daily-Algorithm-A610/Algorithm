from collections import deque

def solution(queue1, queue2):
    currentSum = sum(queue1)
    objectSum = (currentSum + sum(queue2))
    
    # 모든 원소의 합을 반으로 나눈 값이 정수 값이 아닌 경우. 즉, 큐 연산을 아무리 해도 정답을 구할 수 없는 경우.
    if not objectSum % 2 == 0:
        return -1
    
    objectSum //= 2
    # queue1의 합 == queue2의 합 == objectSum이므로 문제를 두 개의 큐가 연속으로 이어지는 전체 큐와 내가 살펴볼 큐인 부분 큐가 있다고 생각하자.
    # 부분 큐에서 원소의 갯수가 1 ~ Max 개인 경우를 모두 구하기 위한 반복문 횟수.
    # 전체 큐의 원소 갯수가 총 6개일 때 초기에 부분 큐에 들어가 있는 원소의 수는 3개 이므로, 삽입 3회 + 삭제 5회 = 8회
    maxLoop = len(queue1) * 3 - 1
    
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    answer = 0
    while answer < maxLoop:
        if currentSum == objectSum:
            return answer
        else:
            if currentSum < objectSum:
                temp = dq2.popleft()
                currentSum += temp
                dq1.append(temp)
            else:
                temp = dq1.popleft()
                currentSum -= temp
                dq2.append(temp)
                
            answer += 1
    
    return -1
