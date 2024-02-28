def solution(storey):
    answer = 0
    pointer = storey % 10

    while storey != 0:
        if 0 <= pointer < 5:
            answer += pointer
            storey -= pointer

        elif pointer == 5:
            answer += pointer

            if 0 <= (storey // 10) % 10 < 5:
                storey -= pointer
            else:
                storey += pointer

        else:
            answer += (10 - pointer)
            storey += pointer

        storey //= 10
        pointer = storey % 10

    return answer
