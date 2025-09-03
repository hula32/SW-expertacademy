
N = 5
P = [0,1,1,2,0]

cnt = [0] * (N+1)
# [1,2,3,1,0,0]

min_val = 9999

for idx, num in enumerate(P, 1): # 1,2,3,4,5,6 / 
    for i in range(num, idx+1):
        cnt[i] += 1

if min_val > sum(cnt):
    result = sum(cnt) - 4

        
print(min_val)    



    #print(idx, cnt_num)
    # for i in range()


'''

# 방은 1번부터 N번까지
# 왼쪽 포털, 오른쪽 포털
# 오른쪽은 무조건 바로 옆 한 칸만 갈 수 있는 포털
# 왼쪽 포털은 주어진 번호로 바로 이동
# 처음 그 방에 갔다면 -> 무조건 왼쪽 포털 사용
# 두번째 그 방에 갔다면 -> 오른쪽으로 한 칸

# 1. 정확한 반복 횟수가 안나와 있고, 반복의 조건만 나와있다 => while
# 2. 방문처리(visited)

N = 5 # 방의 개수 5, 1번 ~ 5번 방까지 있음
P = [0] + [0, 1, 1, 2, 0] # N-1 크기의 배열을 만들고, 가장 첫번째는 쓰지 않는다.
visited = [False] * (N+1)

idx = 1 # 1번방부터 시작
visited[idx] = True # 1번은 이미 방문한 상태로 시작, 2~N번방은 아직 방문하지 않음
cnt = 0

# 목표 : idx => N까지 가길 바람(종료조건)
# <=> 반대되는 상황: idx가 아직 N이 아닌 상황 (반복해야 하는 조건)

while idx < N:
    idx += 1 # 오른쪽으로 한 칸 간다
    cnt += 1 # 한번 이동했으니까 카운트 늘리기

    if idx == N: # N번 방에 도달했다면 바로 while문 종료
        break # N번 방(마지막 방의 경우에는 왼쪽 포털 이동 기회를 차단)
    
    if not visited[idx]: # idx번 방을 처음 방문했다면
        visited[idx] = True
        idx = P[idx] # 왼쪽으로 이동
        cnt += 1 # 이동했으므로 카운트 늘려주기

print(cnt)


'''