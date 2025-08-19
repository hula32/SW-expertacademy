T = int(input())

for t in range(1, T+1):
    N = int(input()) # 인원수
    arr = list(map(int, input().split())) # 카드(번호순)

# N = 4
# arr = [1, 3, 2, 1]

    # visited = [False] * N
    # res = [0] * 2 # 카드 값
    # res_idx = [0] * 2 # 카드의 원래 인덱스 값

    # # 순열 만들기
    # def perm(idx): 
        
    #     if idx == len(res): # 기저조건
    #         a = (res_idx[0], res[0]) # (인덱스, 값)
    #         b = (res_idx[1], res[1])
    #         print(winner(a, b)) # 승자 출력
    #         return
        
        
    #     for i in range(N):
    #         if not visited[i]:
    #             visited[i] = True
    #             res[idx] = arr[i]
    #             res_idx[idx] = i # 선택한 카드의 인덱스 저장
    #             perm(idx+1)
    #             visited[i] = False


    # 가위바위보 승자 가르기
    def winner(a, b): # 이긴 사람의 인덱스 번호도 필요하기 때문에, (인덱스, 값) 튜플로 넘겨주면 좋음
        if a[1] == b[1]:
            if a[0] < b[0]:
                return a
            else:
                return b
        elif (a[1] == 1 and b[1] == 3) or (a[1] == 2 and b[1] == 1) or (a[1] == 3 and b[1] == 2):
            return a
        else:
            return b
        
        
    # 최종 승자 가르기
    def solve(start, end): # start = 0, end = 3 -> 참가자 1~4 전부 (0, 3)
        if start == end: # 혼자면 승자
            return(start, arr[start])
        
        mid = (start + end) // 2 # 2
        left = solve(start, mid)
        right = solve(mid+1, end)

        return winner(left, right) # 두 그룹의 승자끼리 붙임
        
    champion = solve(0, N-1) # 0, 3

    print(f"#{t} {champion[0]+1}")





'''
[1, 3] 
[1, 2]
[1, 1]
[3, 1]
[3, 2]
[3, 1]
[2, 1]
[2, 3]
[2, 1]
[1, 1]
[1, 3]
[1, 2]
1 : 가위
2 : 바위
3 : 보
'''






