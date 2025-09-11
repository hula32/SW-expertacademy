arr = [list(input().strip()) for _ in range(8)]

# r이 짝수이고, c가 홀수일 때 검정 칸
# 반대로 r이 홀수, c가 짝수일 때 하얀 칸
# 하얀칸일 때, F면 cnt += 1

cnt = 0
for r in range(8):
    for c in range(8):
        if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
            # print(r, c)
            if arr[r][c] == 'F':
                cnt += 1

print(cnt)

# 완료




