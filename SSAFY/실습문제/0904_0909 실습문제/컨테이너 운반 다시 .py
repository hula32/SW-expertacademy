T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    car = list(map(int, input().split()))

    container.sort(reverse=True)
    car.sort(reverse=True)

    total = 0
    j = 0 # 컨테이너 인덱스

    for car_num in car:
        while j < N and container[j] > car_num:
            j += 1
            
        if j < N:
            total += container[j]
            j += 1

    print(f'#{t} {total}')