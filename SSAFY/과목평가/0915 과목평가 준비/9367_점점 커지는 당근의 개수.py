# 조건 1 : 연속으로 당근의 크기가 커진 경우 커진 개수 cnt
# 조건 2 : 당근의 크기는 수확한 순서대로 주어짐
# 조건 3 : 연속으로 커지는 당근의 갯수는 최대 얼마?
# 조건 4 : 연속으로 커지지 않는 경우 1출력

T = int(input())
for t in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    max_val = -1
    cnt = 0
    for idx in range(N-1):
        if number[idx] < number[idx+1]:
            cnt += 1
        else:
            max_val = max(max_val, cnt)
            cnt = 0

    max_val = max(max_val, cnt)

    if max_val > -1:
        print(f'#{t} {max_val+1}')
    else:
        print(f'#{t} 1')