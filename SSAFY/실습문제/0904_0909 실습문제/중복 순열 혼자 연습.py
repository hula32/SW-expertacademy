# 중복순열
# [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.

path = []

def recur(cnt):
    if cnt == 2:
        print(*path)
        return
    
    for i in range(3):
        path.append(i)
        recur(cnt + 1)
        path.pop()


recur(0)