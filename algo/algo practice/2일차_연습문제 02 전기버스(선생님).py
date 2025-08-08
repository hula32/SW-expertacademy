T = int(input()) # 테케 수 입력 받기
 
def count_charge(K, N, M, chargers):
    # 주어진 입력값을 가지고
    # 문제의 조건대로 그대로 시뮬레이션 돌기
 
    # 시뮬레이션 결과 나온 cnt를 반환
    ...
    idx = 0 # 버스는 0번 정류장에서 출발
    cnt = 0 # 현재 충전횟수는 0
 
    print(f"while문 실행 전, 이때의 idx: {idx}")
    # while : True때는 반복, False일 때 종료
    while idx < N: 
        print(f" ***** while문 반복 : idx {idx} < N {N} = {idx < N}")
        # idx < N일 때는 반복하겠다
        # idx == N이면 멈추겠다.
        # 1. K만큼 갈수있는 거리 안에서 가장 먼 충전기 찾기
        candidates = [c for c in chargers if idx < c and c <= idx + K]
        print(f" - idx: {idx}일 때의 candidates: {candidates}")
 
        if idx + K >= N: # 만약 현재 위치에서 종점까지 갈 수 있다면..
            print(f" - idx: {idx}의 위치에서는 충전 없이 종점까지 바로 갈 수 있음. 여기서 함수 종료.")
            return cnt # 더이상 충전 필요 없고 현재까지 충전 카운트 바로 반환
        if len(candidates) == 0: # 충전소가 없다면
            print(f" - idx: {idx}에서 더 이상 갈 수 있는 충전소 없음.")
            return 0 # 충전소가 없어서 종점까지 갈 수 없는 경우는 0
        else: # 갈 수 있는 충전소가 있다면
            print(f" - idx: {idx}에서 ", end='')
            idx = max(candidates) # 갈 수 있는 충전소 중에서 가장 먼 충전소로 바로 건너 뛴다.
            print(f"idx: {idx} 위치의 충전기로 이동 후 충전, 충전횟수 +1")
            cnt += 1 # 충전을 한번 했으므로 충전 카운트 늘리기.
         
 
 
for tc in range(1, T+1): # 테케 수만큼 반복
    K, N, M = list(map(int, input().split()))
    chargers = list(map(int, input().split())) # 충전기의 위치
 
    # 우리가 구해야 할 것: 최소한으로 종점까지 갈 수 있는 충전 횟수
    cnt = count_charge(K, N, M, chargers)
 
    print(f"#{tc} {cnt}")