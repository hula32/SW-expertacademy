# # 조건 1 : 연속적인 기간(2일 ~ K일)의 온도의 합이 가장 큰 값
# # 설계 : 완전탐색 
# # 지나온 일수는 더해볼 필요 없음

# N, K = map(int,input().split()) 
# number = list(map(int, input().split()))
# # N = 전체 날짜의 수
# # K = 합을 구하기 위한 연속적인 날짜의 수-> range(K):

# max_val = float("-inf")
# # [idx:idx+k]까지 합계 구하기
# for idx in range(N-K+1):
#     result = sum(number[idx:idx+K])
#     max_val = max(max_val, result)

# print(max_val)

# 누적합
N, K = map(int,input().split()) 
number = list(map(int, input().split()))


subset = sum(number[0:K])
max_val = subset

for idx in range(1, N-K+1):
    new_subset = subset + number[idx+K-1] - number[idx-1]
    max_val = max(max_val, new_subset)
    subset = new_subset
    # print(subset, number[idx+K-1], number[idx-1])
print(max_val)





# 누적합 구하기
# 누적합 - 누적합 = 구간 합