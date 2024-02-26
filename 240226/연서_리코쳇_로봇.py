# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 리코쳇 로봇 https://school.programmers.co.kr/learn/courses/30/lessons/169199?language=python3
#
# 문제를 잘 읽어야 삽질을 덜 한다...
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import deque

def solution(board):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    answer = 0
    N = len(board)  # 세로
    M = len(board[0])  # 가로
    startpoint = []
    endpoint = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                startpoint.append(i)
                startpoint.append(j)
            elif board[i][j] == 'G':
                endpoint.append(i)
                endpoint.append(j)

    q = deque([])
    q.append(startpoint)
    visited = [[99999999 for i in range(M)] for j in range(N)]
    flag = False

    while q:
        if flag: break
        l = len(q)
        answer += 1
        for i in range(l):
            now = q.popleft()
            nowy, nowx = now[0], now[1]

            if nowy == endpoint[0] and nowx == endpoint[1]:
                flag = True
                break

            for i in range(4):
                nx = nowx
                ny = nowy
                while 0 <= nx + dx[i] < M and 0 <= ny + dy[i] < N and board[ny + dy[i]][nx + dx[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                if visited[ny][nx] > answer:
                    visited[ny][nx] = answer
                    q.append([ny,nx])

    if flag:
        return answer-1
    else: return -1
