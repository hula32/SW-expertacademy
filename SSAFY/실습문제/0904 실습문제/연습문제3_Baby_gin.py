path = []
arr = [0, 1, 6, 2, 7, 8]
visited = [False] * len(arr)

def is_run(N):
    if N[1] == N[0] + 1 and N[2] == N[0] + 2: return True
    return False
    
def is_triplet(N):
    if N[0] == N[1] == N[2]: return True
    return False

def recur(cnt):
    global is_babygin
    if cnt == 6:
        first, second = path[:3], path[3:]
        if (is_run(first) and is_triplet(second)) or (is_run(second) and is_triplet(first)) or \
            (is_run(first) and is_run(second)) or (is_triplet(first) and is_triplet(second)):
            # print(f'{path}: baby-gin')
            is_babygin = True
        return
    
    for idx in range(len(arr)):
        if visited[idx]:
            continue

        visited[idx] = True
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        visited[idx] = False

is_babygin = False
recur(0)
if is_babygin:
    print("babygin")
else:
    print("-1")