'''
https://school.programmers.co.kr/learn/courses/30/lessons/43105
dfs로 접근했다가 뒤늦게 메모이제이션 적용하느라 댕삽질한 문제...
'''

def dfs(n, triangle, x, y, sum_num, visited):
    if x == n:
        return sum_num

    if (x, y) in visited:
        return sum_num + visited[(x, y)]

    left = dfs(n, triangle, x + 1, y, sum_num + triangle[x][y], visited)
    right = dfs(n, triangle, x + 1, y + 1, sum_num + triangle[x][y], visited)

    max_sum = max(left, right)
    visited[(x, y)] = max_sum - sum_num
    return max_sum


def solution(triangle):
    n = len(triangle)
    return dfs(n, triangle, 0, 0, 0, {})

