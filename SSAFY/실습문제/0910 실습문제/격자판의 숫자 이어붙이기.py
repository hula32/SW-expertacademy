# 조건 1 : 4 * 4 격자판에 0~9 숫자 작성
# 조건 2 : 동서남북으로 총 6번 이동하면서 각 칸의 숫자를 이어 붙이기 -> 7자리 수 완성
# 조건 3 : 중복된 칸 허용, 임의의 위치에서 시작
# 조건 4 : 격자판 안 벗어나기
# 조건 5 : 서로 다른 7자리 수의 개수 구하기 -> set(), count = 0

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def recur(r, c, num):
    global result
    if len(num) == 7:
        result.add(num)
        return
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 > nr or nr >= 4 or 0 > nc or nc >= 4:
            continue

        recur(nr, nc, num + arr[nr][nc])

for t in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for sr in range(4):
        for sc in range(4):
            recur(sr, sc, arr[sr][sc])
    
    print(f'#{t} {len(result)}')

