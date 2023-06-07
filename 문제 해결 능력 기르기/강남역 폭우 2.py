def trapping_rain(buildings):
    # 여기에 코드를 작성하세요
    high = 0
    left = [0]*len(buildings)   # i번째 빌딩 기준 가장 큰 왼쪽 빌딩 높이 리스트
    for i in range(len(buildings)):
        if buildings[i] > high:
            high = buildings[i]
        left[i] = high

    high = 0
    right = [0]*len(buildings)  # i번째 빌딩 기준 가장 큰 오른쪽 빌딩 높이 리스트
    for i in range(len(buildings)-1, -1, -1):
        if buildings[i] > high:
            high = buildings[i]
        right[i] = high

    result = 0
    for i in range(1, len(buildings)-1):
        capacity = min(left[i], right[i])
        result += max(0, capacity - buildings[i])
    return result


# 테스트 코드
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
