def counting_sort(data, temp, k):
# data [] = 입력 배열(0 <= 정수, k>= 정수)
# temp [] = 정렬된 배열
# counts [] = 카운트 배열 -> k 배열 개수

    counts = [0] * (k+1)
    # k: 주어진 입력 배열에서 최대값

    for i in range (len(data)): # 데이터 길이 8, range (0 ~ 7)
        counts[data[i]] += 1 
        '''
        data[0] -> counts[0] += 1
        data[1] -> counts[4] += 1
        data[2] -> counts[1] += 1

        [1, 0, 0, 0, 0, 0, 0, 0, 0]
        [1, 0, 0, 0, 1, 0, 0, 0, 0]
        [1, 1, 0, 0, 1, 0, 0, 0, 0]
        [1, 1, 0, 1, 1, 0, 0, 0, 0]
        [1, 2, 0, 1, 1, 0, 0, 0, 0]
        [1, 2, 1, 1, 1, 0, 0, 0, 0]
        [1, 2, 1, 1, 2, 0, 0, 0, 0]
        [1, 3, 1, 1, 2, 0, 0, 0, 0]
        ...
        '''
    for i in range(1, k+1): # range 1 ~ 8 , 해당 숫자의 상대적 위치 / 누적합
        counts[i] += counts[i-1] 
        '''
        counts[1] = counts[1] 3 + counts[0] 1 => 4
        counts[2] = counts[2] 1 + counts[1] 4 => 5
        counts[3] = counts[3] 1 + counts[2] 5 => 6
        counts[4] = counts[4] 2 + counts[3] 6 => 7

        '''

    for i in range(len(data)-1, -1, -1): # range (7 ~ 0)
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]     
      
    return temp
    
        


data = [0, 4, 1, 3, 1, 2, 4, 1]
temp = [0] * len(data)
print(counting_sort(data, temp, max(data)))