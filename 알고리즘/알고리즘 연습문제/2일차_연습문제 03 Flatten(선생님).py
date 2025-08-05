for t in range(1, 11):
    dump = int(input()) # 834
    box_h = list(map(int, input().split())) # 42 68 ...

    for _ in range(dump): # 주어진 횟수만큼 덤프를 한다.

        max_h = 0 # 최대 높이 찾기
        max_idx = -1 # 그때의 idx값 저장
        min_h = 101 # 최소 높이
        min_idx = -1 # 그때의 idex

        for idx, high in enumerate(box_h):
            if max_h < high:
                max_h = high
                max_idx = idx
            if min_h > high:
                min_h = high
                min_idx = idx

        box_h[max_idx] -= 1 # 최대 높이에서 -1
        box_h[min_idx] += 1 # 최소 높이에서 +1

        if min_h == max_h:
            break


    max_h = 0
    max_idx = -1
    min_h = 101
    min_idx = -1

    for idx, high in enumerate(box_h):
        if max_h < high:
            max_h = high
            max_idx = idx
        if min_h > high:
            min_h = high
            min_idx = idx

    box_score = max_h - min_h

    print(f'{t} {box_score}')


T = 10
for t in range(1, T+1):
    N = int(input())
    N_height = list(map(int, input().split()))

    for _ in range(N):

        max_h = 0
        max_idx = -1
        min_h = 101
        min_idx = -1

        for idx in range(len(N_height)):
            if N_height[idx] > max_h:
                max_h = N_height[idx]
                max_idx = idx
            if N_height[idx] < min_h:
                min_h = N_height[idx]
                min_idx = idx

        N_height[max_idx] -= 1
        N_height[min_idx] += 1

        if max_h - min_h <= 1:
            break

        max_h = 0
        max_idx = -1
        min_h = 101
        min_idx = -1

        for idx in range(len(N_height)):
            if N_height[idx] > max_h:
                max_h = N_height[idx]
                max_idx = idx
            if N_height[idx] < min_h:
                min_h = N_height[idx]
                min_idx = idx

        result = max_h - min_h
        
    print(f'#{t} {result}')


# 카운팅 배열을 만들어서 최대 최소 찾기
# ex) 14, 13, 11, 2, 3, 4, 5, 8, 11, 14
# 카운팅 배열을 만드는 순간 정렬이 된다.

T = 10

for t in range(1, T+1):
    N = int(input())
    N_height = list(map(int, input().split()))

    # 카운팅 배열
  # 카운팅 배열을 쓰는 풀이

T = 10 # 테스트케이스 수가 10개로 고정, 따로 입력을 받지 않음.


for tc in range(1, T+1):
    dump_cnt = int(input()) # 덤프 횟수
    data = list(map(int, input().split())) # 상자 높이 배열 (100개)

    # 카운팅 배열
    # - 상자의 높이를 카운팅하면, 카운팅 배열에서 0이 아닌 값을 찾으면 됨
    #  - 가장 왼쪽에 있는 값이 최소값의 개수
    #  - 가장 오른쪽에 있는 값이 최대값의 개수

    # 카운팅 배열 만들기
    cnt = [0] * 101 # 인덱스 최댓값이 100이므로 101개 배열을 만든다.
    # 높이의 갯수 세기
    for num in data: # 높이를 순회
        cnt[num] += 1
    
    # 덤프 횟수만큼 덤프하기
    for _ in range(dump_cnt):
        lft = 0 # 왼쪽 인덱스 0에서부터 출발
        rgt = 100 # 오른쪽 인덱스는 100에서부터 출발

        """
        
        lft = 0부터 시작해서 오른쪽으로 가면서 0이 아닌 첫번째 수(최소값)를 찾고 싶음
        목표 : lft != 0 => 반복 종료
        원치 않는 상태: lft == 0 => while문 조건에 넣기
        
        """

        while cnt[lft] == 0: # 갯수가 0이면(원치 않는 상황)
            # cnt[lft] == 0 : 반복 돌기
            lft += 1 # 오른쪽으로 이동
        # 언제 반복이 종료?
        # cnt[lft] != 0이 되는 첫번째 순간에 반복이 종료가 됨.

        # while 문을 빠져나왔다는 것은 cnt[lft] != 0인 첫번째 상황을 만난 것임.
        # lft : 높이의 최솟값. cnt[lft]: 최소값의 개수

        while cnt[rgt] == 0: # 갯수가 0이면
            rgt -= 1 # 왼쪽으로 이동
        
        # rgt: 높이의 최댓값

        # 덤프 수행
        cnt[lft] -= 1
        cnt[rgt] -= 1
        cnt[lft +1] += 1
        cnt[rgt -1] += 1

    # 모든 덤프 완료
    # 덤프 완료 후에 다시 최대, 최소를 찾는다.
    lft = 0
    rgt =100

    while cnt[lft] == 0:
        lft += 1
    while cnt[rgt] == 0:
        rgt -= 1

    print(f"#{tc} {rgt - lft}")









                  


