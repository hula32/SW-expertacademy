T = int(input())

def recur(total):
    global result

    if total > N:
        return

    if total == N:
        result += 1
        return
    
    for i in range(1, 4):
        recur(total + i)

for t in range(1, T+1):
    N = int(input())

    result = 0

    recur(0)
    print(result)