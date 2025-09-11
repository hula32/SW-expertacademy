N = input().strip()

path = []
visited = [False] * len(N)
result = []


def palin(N):
    mid = len(N) // 2
    lft = 0
    rgt = len(N)-1

    is_pal = True
    for i in range(mid):
        if path[lft + i] != path[rgt - i]:
            is_pal = False

    return is_pal

def recur(cnt):
    global path, result

    if cnt == len(N):
        if palin(path):
            result.append(path[:])
            # 만약 값이 여러개일 경우, 사전순으로 출력
            
            
    for i in range(len(N)):
        if not visited[i]:
            visited[i] = True
            path.append(N[i])
            recur(cnt + 1)
            path.pop()
            visited[i] = False

    

recur(0)
print(result)

