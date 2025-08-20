# 큐 => deque
from collections import deque

T = int(input()) # 테스트케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque() # 큐 생성
    q.extend(arr) # arr의 수를 모두 큐에 삽입

    # M번 이동
    for _ in range(M):
        num = q.popleft() # dequeue : popleft
        q.append(num) # enqueue: append

    print(f"#{tc} {q.popleft()}")