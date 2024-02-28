"""
문제에서 층 수는 10의 양의 거듭제곱수로만 조작할 수 있다.
결국 특정 숫자를 0으로 만들기 위해서는 각 자리 수를 적절히 증가 혹은 감소하여 모든 자리의 수를 0으로 만들어야 한다.
높은 자리의 숫자의 경우 낮은 자리의 수가 어떻게 처리되느냐(올려지거나 내려지거나)에 영향을 받는다.
따라서, 높은 자리의 숫자를 처리하기 위해서는 낮은 자리 숫자를 처리하는 부문제를 해결해야 한다. => dp
"""
def solution(storey):
    numList = list(map(int, str(storey)))

    # 낮은 처리 숫자부터 접근하기 편하게 하기 위해 역정렬.
    numList.reverse()
    # 가장 상위 자리를 0으로 추가할 필요가 있다. 가장 높은 자리의 수가 올려지는 경우와 내려지는 경우를 확인해야 하기 때문.
    numList.append(0)
    
    # dp[x][0]은 위로 올리는 경우, dp[x][1]은 아래로 내리는 경우.
    dp = [[0 for _ in range(2)] for _ in range(len(numList))]
    # 편의를 위해 가장 낮은 자리 수의 dp 값을 미리 구함.
    dp[0][0] = 10 - numList[0]
    dp[0][1] = numList[0]
    
    # 두 번째로 낮은 자리 수부터 dp 시작.
    for i in range(1, len(numList)):

        # 해당 자리의 수가 높여지기 위해 필요한 이동 횟수.
        upCount = 10 - numList[i]
        # 해당 자리의 수가 낮아지기 위해 필요한 이동 횟수.
        downCount = numList[i]

        dp[i][0] = min(upCount - 1 + dp[i-1][0], upCount + dp[i-1][1])
        dp[i][1] = min(downCount + 1 + dp[i-1][0], downCount + dp[i-1][1])
    
    # 0이 되기 위해서는 가장 높은 자리 수가 어쨌든 내려져야 한다.
    answer = dp[len(numList)-1][1]
    
    return answer
