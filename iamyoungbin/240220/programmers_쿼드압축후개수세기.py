answer = [0, 0]

def solution(arr):
    
    def checkSquare(sy, ey, sx, ex):
        for i in range(sy, ey):
            for j in range(sx, ex):
                if arr[sy][sx] != arr[i][j]:
                    return False
              
        answer[arr[sy][sx]] += 1
        return True
    
    def divideSquare(sy, ey, sx, ex):
        if checkSquare(sy, ey, sx, ex):
            return   
        
        my = (sy + ey) // 2
        mx = (sx + ex) // 2
        
        divideSquare(sy, my, sx, mx)
        divideSquare(my, ey, sx, mx)
        divideSquare(sy, my, mx, ex)
        divideSquare(my, ey, mx, ex)
        
    size = len(arr)
    divideSquare(0, size, 0, size)
    
    return answer
    