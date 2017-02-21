def fact(n = 0):
    answer = 1
    for num in range(1, n+1):
        answer = answer*num
    return answer
