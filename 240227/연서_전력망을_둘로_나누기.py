# 아니 게리멘더링이랑 완전 똑같은줄알앗는데............ 유레카 실패
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

mincount = 999999
def isconnected(area, start, n):

    visited = [False for i in range(n)]
    q = deque([])
    q.append(start)
    cnt = 1
    visited[start - 1] = True

    while q:
        now = q.popleft()
        for i in range(n):
            if area[now - 1][i] is True and visited[i] is False:
                visited[i] = True
                q.append(i + 1)
                cnt += 1

    return cnt


def solution(n, wires):
    global mincount

    m = [[False for col in range(n)] for row in range(n)]

    for i in range(n):
        m[i][i] = True

    for w in wires:
        m[w[0]-1][w[1]-1] = True
        m[w[1]-1][w[0]-1] = True

    for w in wires:
        # 전선을 끊고 양 옆을 루트 노드로 갖음
        m[w[0]-1][w[1]-1] = False
        m[w[1]-1][w[0]-1] = False
        a = isconnected(m,w[0], n)
        b = isconnected(m, w[1], n)
        if a+b == n:
            mincount = min(mincount, abs(a-b))
        m[w[0]-1][w[1]-1] = True
        m[w[1]-1][w[0]-1] = True

    return mincount

