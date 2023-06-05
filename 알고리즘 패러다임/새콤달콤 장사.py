def max_profit_memo(price_list, count, cache):
    # 여기에 코드를 작성하세요
    for i in range(count+1):    # count 개수 전까지 실행
        if i < len(price_list): # i개를 한 번에 팔 수 있을 경우
            cache[i] = price_list[i]    # 초기값을 price[i]로 설정
            for j in range(i-1, 0, -1): # i개를 나눠서 파는 경우가 최대수익이라면 해당 값으로 변경
                if cache[i] < cache[j] + price_list[i-j]:
                    cache[i] = cache[j] + price_list[i-j]
        else:
            cache[i] = 0    # i개를 무조건 나눠서 팔아야 하는 경우 초기값을 0으로 설정
            for j in range(len(price_list)-1, 0, -1):
                if cache[i] < cache[i-j] + price_list[j]:
                    cache[i] = cache[i-j] + price_list[j]
    
    return cache[count]

    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트 코드
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))


#---------------------------------------------------------------------------------------------------------------
def max_profit(price_list, count):
    # 여기에 코드를 작성하세요
    cache = {}
    for i in range(count+1):    # count 개수 전까지 실행
        if i < len(price_list): # i개를 한 번에 팔 수 있을 경우
            cache[i] = price_list[i]    # 초기값을 price[i]로 설정
            for j in range(i-1, 0, -1): # i개를 나눠서 파는 경우가 최대수익이라면 해당 값으로 변경
                if cache[i] < cache[j] + price_list[i-j]:
                    cache[i] = cache[j] + price_list[i-j]
        else:
            cache[i] = 0    # i개를 무조건 나눠서 팔아야 하는 경우 초기값을 0으로 설정
            for j in range(len(price_list)-1, 0, -1):
                if cache[i] < cache[i-j] + price_list[j]:
                    cache[i] = cache[i-j] + price_list[j]
    
    return cache[count]


# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
