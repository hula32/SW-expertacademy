# 재귀함수

arr = [1,2,3,4,5]
N = len(arr)
R = 3

res = [0] * R # 저장소
visited = [False] * N

def perm(idx): # res
    if idx == R:
        print(res)
        return
    for i in range(N): # arr
        if 



perm(0)
