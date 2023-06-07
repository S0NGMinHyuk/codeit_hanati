def sum_in_list(search_sum, sorted_list):
    # 여기에 코드를 작성하세요
    left, right = 0, len(sorted_list)-1
    while left <= right:
        if sorted_list[left] + sorted_list[right] < search_sum:
            left += 1
        elif sorted_list[left] + sorted_list[right] > search_sum:
            right -= 1
        else:
            return True
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
