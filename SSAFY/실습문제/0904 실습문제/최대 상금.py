T = int(input())

for t in range(1, T+1):
    num, ch = map(int, input().split())

    path = []
    number = [] # ['1', '2', '3']
    change = 0

    for n in str(num):
        number.append(n)

    visited = [False] * len(number)

    def recur(cnt):
        global change

        if cnt == len(number):
            change += 1
            print(*path)
            return
        
        for idx in range(len(number)):
            if visited[idx]:
                continue
    
            visited[idx] = True
            path.append(int(number[idx]))
            recur(cnt + 1)
            path.pop()
            visited[idx] = False

    recur(0)