# 조건 1 : 탑의 높이가 B 이상인 경우 그 중 높이가 가장 낮은 탑 찾기
# 조건 2 : 가장 낮은 탑의 높이와 탑의 높이의 차
T = int(input())

def recur(cnt, total):
    global min_val

    if total >= B:
        min_val = min(min_val, total)
        return

    if cnt == N:
        return
        
    recur(cnt + 1, total + S[cnt])
    recur(cnt + 1, total)

for t in range(1, T+1):
    N, B = map(int, input().split())     # 점원 인원, 탑의 높이
    S  = list(map(int, input().split())) # 점원들 키의 합

    min_val = 1e9
    
    recur(0, 0)
    print(f'#{t} {min_val - B}')
