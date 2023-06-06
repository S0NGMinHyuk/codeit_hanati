def find_same_number(some_list):
    # 여기에 코드를 작성하세요
    dic = {}    # 딕셔너리 자료형을 통해 중복값인지 판별
    for num in some_list:
        if num in dic:
            return num
        else:
            dic[num] = 1
    

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
