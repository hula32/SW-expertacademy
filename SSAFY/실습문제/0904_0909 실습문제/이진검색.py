def binary_search_while(target):
    left = 0                # 검색 시작점   
    right = len(arr) - 1    # 검색 끝점 
    cnt = 0                 # 몇 번 만에 검색했는가?

    while left <= right:    # 교차되면 못찾은 것
        mid = (left + right) // 2
        cnt += 1 # 검색횟수 추가

        if arr[mid] == target:
            return mid, cnt  # mid 위치에 존재한다고 return 
            
        
        # target보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid -  1
        # target보다 정답이 오른쪽에 있는 경우 
        else:
            left = mid + 1 
    
    # 못 찾은 경우
    return -1, cnt


arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()

print(f'  9 = {binary_search_while(9)} 번째에 위치')  # 처음과 끝을 함께 전달