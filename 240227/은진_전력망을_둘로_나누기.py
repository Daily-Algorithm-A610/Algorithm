from collections import deque

def solution(n, wires):
    res = 100
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    for x, y in wires:  # 인접행렬
        graph[x][y] = 1
        graph[y][x] = 1
    
    for x, y in wires:
        graph[x][y] = 0
        graph[y][x] = 0
        
        visited = [0]*(n+1)
        bfs(1, n, graph, visited)
        res = min(res, abs(n - sum(visited) * 2))  # sum(visited)와 n - sum(visited)
        
        graph[x][y] = 1
        graph[y][x] = 1
    
    return res


def bfs(vertex, n, graph, visited):
    visited[vertex] = 1
    queue = deque([vertex])
    
    while queue:
        x = queue.popleft()
        for i in range(n+1):
            if graph[x][i] and not visited[i]:
                visited[i] = 1
                queue.append(i)


      
