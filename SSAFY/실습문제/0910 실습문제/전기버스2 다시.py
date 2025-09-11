T = int(input())

def recur(idx, battery, cnt):
    global min_val

    battery -= 1

    if min_val <= cnt:
        return
    
    if battery < 0:
        return
    
    if idx == N and battery >= 0:
        min_val = min(min_val, cnt)
        return
    
    recur(idx+1, M[idx], cnt+1)
    recur(idx+1, battery, cnt)

for t in range(1, T+1):
    N, *M = map(int, input().split())
    M = [0] + M

    min_val = float("inf")
    recur(2, M[1], 0)

    print(f'#{t} {min_val}')