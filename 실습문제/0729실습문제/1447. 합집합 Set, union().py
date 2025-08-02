# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1 | set2
    # return set1.union(set2)
    # result = set()
    # result = update(set1)
    # result = update(set2)
def union_multiple_sets(*sets):
    # Tuple에 포함된 요소들의 개수 => len(sets)
    if len(sets) < 2:
        print("최소 두개의 셋이 필요합니다")
        return set()
    else:
        # 가변인자 sets의 자료형은 tuple이다.
        # tuple은 iterable이다.
        result = set()
        for item in sets:
            result = result | item

        return result

    # 총 합을 구한다.
    lst = [1, 2, 3, 4, 5]
    hap = 0
    for val in lst:
        hap = hap + val # 누적
    print(hap) # 15


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다