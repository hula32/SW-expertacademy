arr = [2, 2, 2]

N = 3
R = 3

path = []
visited = [False] * N

run = False
triplet = False

def is_run(a):
    return a[0] == a[1] - 1 == a[2] - 2

def is_triplet(a):
    return a[0] == a[1] == a[2]

def recur(cnt):
    global run, triplet
    if cnt == R:
        # print(*path)
        if is_run(path):
            run = True
        if is_triplet(path):
            triplet = True
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            recur(cnt + 1)
            path.pop()
            visited[i] = False

recur(0)

print(run, triplet)