# 원재는 연속된 N일 동안의 물건의 매매가 예측
# 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입
# 판매 자유

T = int(input())

for t in range(1, T+1):
    N = int(input()) # 3
    number = list(map(int, input().split())) # 3 5 9

    max_val = -1
    buy = 0

    for i in range(N-1, -1, -1): # 2, 1, 0
        if max_val < number[i]:
            max_val = number[i]
        else:
            buy += max_val - number[i]

    print(f'#{t} {buy}')

