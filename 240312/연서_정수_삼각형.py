def solution(arr):

    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if arr[i+1][j] >= arr[i+1][j+1]:
                arr[i][j] += arr[i+1][j]
            else :
                arr[i][j]+=arr[i+1][j+1]

    return arr[0][0]
