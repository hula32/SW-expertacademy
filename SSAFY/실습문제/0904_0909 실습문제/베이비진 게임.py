# 0 ~ 9 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때,
# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet

# player 1, player 2 교대로 한 장 씩 카드를 가져감
# 6장을 채우기 전이라도 먼저 run 또는 triplet 되는 사람이 승자

# 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램 작성
# 무승부인 경우 '0' 출력


T = int(input())

def is_run(a):
    return a[0] == a[1] - 1 == a[2] - 2

def is_triplet(a):
    return a[0] == a[1] == a[2]

def recur(cnt):
    global run, triplet
    if cnt == R:
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

for t in range(1, T+1):
    arr = list(map(int, input().split()))

    N = len(arr)
    R = 3

    path = []
    visited = [False] * N

    run = False
    triplet = False

    for i in range(12):
        if i % 2 == 0: # player1
            recur(0)
            if run or triplet:
                print(f'#{t} 1')

        elif i % 2 != 1:
            recur(0)
            if run or triplet:
                print(f'#{t} 2')

        else:
            print(f'#{t} 0')


            







    


    



