"""
하나의 트리에 속한 송전탑의 개수를 세기 위해서는 트리의 한 노드에서 dfs 혹은 bfs를 하면 된다.
전선을 오직 하나만 끊으므로 전선을 끊는 케이스는 총 n가지.
직관적으로 생각했을 때 전선을 끊는 모든 케이스에 대해 bfs를 돌리면 모든 작업의 시간 복잡도는
n * n^2 으로 o(n^3)이 된다.
n이 최대 100 이므로 충분히 통과될 것이라고 예상.
"""

from collections import deque

edge = []

def solution(n, wires):
    answer = 101
    edge = [[False for _ in range(n)] for _ in range(n)]
    
    def bfs():
        res = 1
        visited = [False for _ in range(n)]
        queue = deque()
        queue.append(0)
        visited[0] = True
        
        while queue:
            current = queue.popleft()
            
            for i in range(n):
                if edge[current][i] and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    res += 1
                    
        return abs(res - (n - res))
    
    for u, v in wires:
        edge[u-1][v-1] = True
        edge[v-1][u-1] = True
    
    for u, v in wires:
        edge[u-1][v-1] = False
        edge[v-1][u-1] = False
        answer = min(answer, bfs())
        edge[u-1][v-1] = True
        edge[v-1][u-1] = True
    
    return answer
