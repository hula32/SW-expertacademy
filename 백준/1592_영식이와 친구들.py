# 한 사람이 공을 M번 받으면 게임 끝(지금 받은 공도 포함)
# 1번부터 시작
# 현재 공을 받은 횟수가 홀수 : 시계방향으로 L번째에게
# 짝수 : 반시계 방향으로 L번째
# 공을 주고 받은 횟수

N, M, L = map(int, input().split()) # 5, 3, 2

cnt = [0] * N

cnt_total = 0
i = 0
result = True

while result:
    cnt[i] += 1
    
    if cnt[i] == M:
        result = False
        break

    cnt_total += 1

    if cnt[i] % 2 == 0:
        i = (i - L) % N
        
    elif cnt[i] % 2 == 1:
        i = (i + L) % N
        
print(cnt_total)

