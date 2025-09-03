from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # 3, 5
    cheese = list(map(int, input().split())) # 7 2 6 5 3
    # N = 화덕크기 
    # M = 피자개수
    # cheese = 치즈 양


    cq = [0] * N
    front = rear = 0


    def pizza(N, M, cheese):
        q = deque()

        # 처음에 N개까지 화덕에 넣기
        for i in range(N): # 0,1,2
            q.append((i+1, cheese[i])) # (피자 번호, 치즈 양)

        next_pizza = N # 다음에 넣을 피자 번호

        while len(q) > 1: # 마지막 하나 남을 때까지
            num, c = q.popleft()
            c = c // 2 # 치즈 절반 감소
            
            if c == 0: # 다 녹았다면 
                if next_pizza < M: # 남은 피자가 있으면 넣기
                    q.append((next_pizza+1, cheese[next_pizza]))
                    next_pizza += 1
            else:
                q.append((num, c)) # 아직 남았으면 다시 넣기
        
        return q[0][0]

    print(f'#{t} {pizza(N, M, cheese)}')
        
    

    

