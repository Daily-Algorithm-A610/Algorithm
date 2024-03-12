"""
옛날에 풀어놨던 문제~
꿀 냠냠
"""
def solution(triangle):
    answer = 0
    
    for row in range(len(triangle)):
        for col in range(len(triangle[row])):
            if row == 0 :
                continue
            elif col == 0:
                triangle[row][col] =  triangle[row][col] + triangle[row-1][0]
            elif col == len(triangle[row-1]):
                triangle[row][col] = triangle[row][col] + triangle[row-1][col-1]
            else:
                left = triangle[row-1][col-1]
                right = triangle[row-1][col]

                if(left >= right):
                    triangle[row][col] = triangle[row][col] + left
                else:
                    triangle[row][col] = triangle[row][col] + right                
            if(answer < triangle[row][col]):
                answer = triangle[row][col]

    return answer