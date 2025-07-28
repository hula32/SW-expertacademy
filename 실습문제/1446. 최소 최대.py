# 아래 함수를 수정하시오.
def find_min_max(data):
    Max = data[0]
    Min = data[0]
    for num in data:
        if num > Max:
            Max = num
        if num < Min:
            Min = num
    
    return (Min, Max)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
