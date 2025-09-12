# 조건 1 : 연속해서 커지거나(같은 것 포함)
# 조건 2 : 연속해서 작아지는(같은 것 포함)
# 조건 3 : 그 수열 중 가장 길이가 긴 것 max_len

N = int(input())
number = list(map(int, input().split()))

max_val = -1
up_cnt = 0
down_cnt = 0

for idx in range(N-1):
    # 연속해서 커지는 경우
    if number[idx] <= number[idx+1]:
        up_cnt += 1
    elif number[idx] > number[idx+1]:
        max_val = max(max_val, up_cnt)
        up_cnt = 0

    # 연속해서 작아지는 경우
    if number[idx] >= number[idx+1]:
        down_cnt += 1
    elif number[idx] < number[idx+1]:
        max_val = max(max_val, down_cnt)
        down_cnt = 0
    
max_val = max(max_val, up_cnt, down_cnt)

print(max_val+1)



