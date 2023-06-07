def max_profit(stock_list):
    # 여기에 코드를 작성하세요
    best = None

    for i in range(len(stock_list)-1):  # (현재 이후 값 중 최대값) - 현재값 이 가장 큰 경우를 찾는다
        now = stock_list[i]
        if best == None or best < max(stock_list[i+1:]) - now:
            best = max(stock_list[i+1:]) - now

    return best


# 테스트 코드
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
