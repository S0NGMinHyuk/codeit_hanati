def sublist_max(profits):   # 완전탐색
    # 여기에 코드를 작성하세요
    total = min(profits)    

    for i in range(len(profits)):   # 인덱스 i ~ j 까지의 총합이 가장 큰 경우 total 값 갱신
        for j in range(i+1, len(profits)+1):
            if sum(profits[i:j]) >= total:
                total = sum(profits[i:j])
    
    return total
