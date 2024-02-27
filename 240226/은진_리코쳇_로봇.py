'''
https://school.programmers.co.kr/learn/courses/30/lessons/169199

(실수)
1. 입력값이 2차원 배열일 줄 알았는데, 1차원 배열에 문자열로 입력값을 받아옴.
2. nx-dx, ny-dy인데 nx-1, ny-1로 작성
3. break 위치
4. 도착지 G 판별하는 코드 위치

R위치에서 7번만에 G위치 도달. ??왜 7번임??
1. 장애물 or 맨 끝에 도달해야지만 stop할 수 있음
2. 로봇은 G를 통과할 수 있다. 1의 stop 조건을 만족한 후 G인지 판단해야함
도달할 수 없다면 -1 작성

'''

from collections import deque

def bfs(n, m, board, start, end):
    queue = deque([start])
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    
    l = n
    if n < m:
        l = m
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x, y
            
            for _ in range(l):
                nx += dx
                ny += dy
                
                # 'D'에 부딪히거나 경계값에 닿을 때까지 전진
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    # nx-dx, ny-dy
                    if not visited[nx-dx][ny-dy]: 
                        visited[nx-dx][ny-dy] = visited[x][y] + 1
                        queue.append([nx-dx, ny-dy])
                    if board[nx-dx][ny-dy] == 'G':
                        return visited
                    break
                elif board[nx][ny] == 'D':
                    if not visited[nx-dx][ny-dy]:    
                        visited[nx-dx][ny-dy] = visited[x][y] + 1
                        queue.append([nx-dx, ny-dy])
                    if board[nx-dx][ny-dy] == 'G':
                        return visited
                    break
            
    return visited


def solution(board):
    n = len(board)
    m = len(board[0])
    graph = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            graph[i][j] = board[i][j]
            
            if graph[i][j] == 'R':
                start = [i, j]
                continue
            if graph[i][j] == 'G':
                end = [i, j]
                continue
    
    visited = bfs(n, m, graph, start, end)
    return visited[end[0]][end[1]]-1
