# 도착지점 2를 찾기
# 도착지점에서부터 올라오기
# 좌우를 살펴보고 1이 있으면 들어가서(c-1) 직진 0을 볼 때까지
# 없으면 직진 (r-1)
# 'r = 0이 될때까지'

# for t in range(1, 11):
#     input()
#     arr = [list(map(int, input().split())) for _ in range(100)]

arr = [[0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1],
       [0, 1, 0, 0, 1],
       [0, 0, 0, 0, 2]]

# 도착지점 2 찾기
start_r, start_c = -1, -1 # 4, 4
for r in range(5):
    for c in range(5):
        if arr[r][c] == 2:
            start_r, start_c = r, c # 2의 위치 저장(기준점)

r, c = start_r, start_c

while r != 0:
    if c-1 >= 0 and arr[r][c-1] == 1:
        while c-1 >= 0 and arr[r][c-1] == 1:
            c -= 1
    elif c+1 < 5 and arr[r][c+1] == 1:
        while c+1 < 5 and arr[r][c+1] == 1:
            c += 1
    r -= 1
    
print(c)

                    










            