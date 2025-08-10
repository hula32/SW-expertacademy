# 버블 정렬

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{t}', *arr)


# 카운팅 정렬

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = -1

    for i in arr:
        if max_val < i:
            max_val = i

    counts = [0] * (max_val+1)
    temp = [0] * N

    for i in range(N):
        counts[arr[i]] += 1

    for i in range(1, max_val+1):
        counts[i] += counts[i-1]

    for i in range(N-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]

    print(f'#{t}', *temp)

# 선택정렬

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_val = i
        for j in range(i+1, N):
            if arr[min_val] > arr[j]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]
    
    print(f'#{t}', *arr)

