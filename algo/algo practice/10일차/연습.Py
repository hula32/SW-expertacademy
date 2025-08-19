# 재귀함수

arr = [1,2,3,4,5]
N = len(arr)
R = 3

visted = [False] * N
res = [0] * R

def perm(idx): # res
    if idx == R: # 기저조건
        print(res)
        return
    
    for i in range(N): # 유도조건
        if not visted[i]:
            visted[i] = True
            res[idx] = arr[i]
            perm(idx+1)
            visted[i] = False
    
perm(0)
