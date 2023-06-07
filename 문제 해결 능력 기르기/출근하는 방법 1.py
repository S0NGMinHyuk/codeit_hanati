def staircase(n):
    # 여기에 코드를 작성하세요
    pibo = [1, 1, 2]    # 피보나치 수열 문제
    while n > len(pibo) - 1:
        pibo.append(pibo[-1] + pibo[-2])
    return pibo[n]


# 테스트 코드
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
