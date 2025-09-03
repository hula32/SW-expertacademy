# 첫번째 상자 A개 < 두번째 상자 B개 < 세번째 상자 C개
# 모든 상자 1개 이상 사탕이 들어있음
# 위 조건을 만족하기 위해 0개 이상 사탕 먹기
# 최소 몇 개의 사탕을 먹어야 할까?
# 먹어서 조건 만족이 어려우면 -1 / 이미 조건 만족이면 0

T = int(input())

for t in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0
    if A >= 1 and B >= 2 and C >= 3:
        while not (A < B < C) : # A < B < C 가 되면 종료
            if B >= C:
                num = B - C + 1
                cnt += num
                B -= num
            if A >= B:
                num = A - B + 1
                cnt += num
                A -= num
    
    else:
        cnt = -1

    print(f'#{t} {cnt}')


