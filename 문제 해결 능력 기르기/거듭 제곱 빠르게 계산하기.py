def power(x, y):
    # 여기에 코드를 작성하세요
    if y == 0:
        return 1
    
    subresult = power(x, y//2)

    if y%2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# 테스트 코드
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
