def min_coin_count(value, coin_list):
    # 여기에 코드를 작성하세요
    coin_list.sort(reverse=True)    # 코인 내림차순 정렬
    ans = 0     # 코인 개수

    for coin in coin_list:
        while value >= coin:
            value -= coin
            ans += 1
    
    # for coin in coin_list:
    #     count += value // coin
    #     value %= coin

    return ans



# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
