T = int(input())

for t in range(1, T+1):
    N = int(input())

    time = []
    for _ in range(N):
        start, end = map(int, input().split())
        time.append((start, end))

    time.sort(key=lambda x : (x[1], x[0]))


# time : (start, end) 쌍의 튜플을 원소로 가지고 있는 리스트
# time.sort() : time 리스트를 정렬
# 일반적으로 튜플을 정렬하게 되면, 튜플 안에서 앞의 숫자가 더 우선순위가 큼
# 그러나, 문제의 조건에서는 두번째 값을 기준으로 정렬하고, 그 다음 첫번째 값으로 정렬해야 함
# => 정렬 기준을 직접 만들어서 넣어줘야 함.
# => 정렬 기준을 정하는 함수가 key
# time.sort(key=lambda x : (x[1], x[0]))
# 리스트.sort는 key가 주어지면
# 리스트의 원소를 하나씩 꺼내서 key 함수의 파라미터로 넣어줌
# key 함수의 반환값이 정렬 기준이 됨
# 실제로는 원소가 정렬되는 것이고, 정렬 기준만 key의 반환값을 쓰는 것임

    last_time = 0
    cnt = 0

    for s, e in time:
        if s >= last_time:
            cnt += 1
            last_time = e

    print(f'#{t} {cnt}')
