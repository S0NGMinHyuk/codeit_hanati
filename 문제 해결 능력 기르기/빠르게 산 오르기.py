def select_stops(water_stops, capacity):
    # 여기에 코드를 작성하세요
    lst = [0]

    for i in range(1, len(water_stops)):    # 마지막으로 간 지점에서 capacity 이내 가장 먼 지역 방문
        if water_stops[i] - lst[-1] > capacity:
            lst.append(water_stops[i-1])
    else:
        if lst[-1] != water_stops[-1]:      # 도착 지점을 지나친 경우 도착 지점 추가
            lst.append(water_stops[-1])

    return lst[1:]
