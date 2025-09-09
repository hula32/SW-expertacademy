# 문제읽기
# - N개의 컨테이너를 M개의 트럭으로 A도시에서 B도시로 운반
# - 트럭당 1개의 컨테이너 운반 가능, 트럭 적재용량을 초과하는 컨테이너는 운반 X
# - 화물의 총 중량이 최대값
# - 컨테이너를 한 개도 옮길 수 없는 경우 '0' 출력

# 설계
# - 1. 정렬
# - 2. 트럭의 적재용량과 컨테이너의 무게를 비교
# -    트럭의 적재용량 < 컨테이너 무게 => 컨테이너 X
# -    트럭의 적재용량 > 컨테이너 무게 => 컨테이너 O
# - 3. 컨테이너 무게 합계 도출

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    car = list(map(int, input().split()))

    # 정렬
    container = sorted(container, reverse=True)
    car = sorted(car, reverse=True)

    '''
    [20, 19, 14, 14, 13, 11, 11, 10, 6, 5]
    [18, 18, 17, 17, 16, 15, 13, 9, 8, 5, 4, 1]
    '''
    
    result = 0
    idx = 0

    for car_num in car:
        while idx < N and container[idx] > car_num:
            idx += 1

        if idx < N:
            result += container[idx]
            idx += 1


    print(f'#{t} {result}')

