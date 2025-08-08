# 카운트 정렬
def count_sort(data, temp, k):
    # 카운트 배열 만들기
    counts = [0] * (k+1)
    # 카운트 배열에 해당 숫자에 해당하는 인덱스에 + 1
    for i in range(len(data)-1, -1, -1): # 5,4,3,2,1,0
        counts[data[i]] += 1
    # 카운트 배열에서 이전 인덱스의 카운트 값과 더하기
    for i in range(1, k+1):
        counts[i] += counts[i-1]
    # temp 새로운 배열에 데이터 값 정렬해서 넣기
    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

#  선택정렬
def sort(a, N):
    for i in range(N-1): # 0,1,2,3,4,5
        min_idx = i # 0 / 1 / 2 ...
        for j in range(i+1, N): # 1,2,3,4,5,6 / 2, 3, 4, 5, 6 / 3, 4, 5, 6...
            if a[min_idx] > a[j]:
                min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]

# 버블정렬
def bubble(a, n):
    for i in range(n-1, 0, -1): 
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]












    



