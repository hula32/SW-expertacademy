# [문제] 카페에 같이 갈 친구가 2명 이상 경우의 수
# - 바이너리 카운팅 버전 코드입니다!
# - 재귀 호출로도 구현해보세요

# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)

# def get_sub(tar):
#     cnt = 0
#     for _ in range(n):
#         if tar & 0x1: # 0번째 비트가 1인지 0인지 확인, 1이면
#             cnt += 1
#         tar >>= 1 # 비트를 오른쪽으로 시프트
#     return cnt

# answer = 0
# for target in range(1 << n):
#     if get_sub(target) >= 2:
#         answer += 1
# print(answer)

# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)

# answer = 0

# def recur(idx, chosen):
#     global answer

#     if idx == n:
#         if len(chosen) >= 2:
#             answer += 1
#         return
    
#     recur(idx + 1, chosen+[arr[idx]])

#     recur(idx + 1, chosen)

# recur(0, [])
# print(answer)


    
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt

answer = 0
for target in range(1 << n):
    if get_count(target) >= 2:
        answer += 1
print(answer)
    