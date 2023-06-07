# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 여기에 코드를 작성하세요
    way = [0]*(stairs+1)
    way[0], way[1] = 1, 1   # 피보나치 수열 응용 문제

    step = [1]  # 한 번에 오를 수 있는 계단 칸 수

    for i in range(2, len(way)):
        if i in possible_steps:
            for s in step:
                way[i] += way[i-s]
            way[i] += 1     # 0칸에서 한 번에 i칸으로 오르는 방법 추가
            step.append(i)  # 한 번에 오를 수 있는 계단 칸 수 추가
        else:
            for s in step:
                way[i] += way[i-s]
    return way[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
