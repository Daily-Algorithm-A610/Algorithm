# https://school.programmers.co.kr/learn/courses/30/lessons/154540?language=python3

from collections import deque


def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = []

    y = len(maps)
    x = len(maps[0])
    visited = [[False for _ in range(x)] for _ in range(y)]

    for i in range(y):
        for j in range(x):
            if maps[i][j] != 'X' and visited[i][j] == False:
                # 여기서부터 돌기 시작합니다.
                q = deque([(i, j)]);
                visited[i][j] = True
                cnt = int(maps[i][j]);

                while q:
                    now = q.popleft()
                    for k in range(4):
                        ny = dy[k] + now[0]
                        nx = dx[k] + now[1]

                        if 0 <= ny < y and 0 <= nx < x and maps[ny][nx] != 'X' and visited[ny][nx] == False:
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            cnt += int(maps[ny][nx])
                answer.append(cnt)

    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer
