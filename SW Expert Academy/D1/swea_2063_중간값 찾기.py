# n개 입력값 받기
n = int(input())

# n개만큼 입력값 받기
n_case = list(map(int, input().split()))

if len(n_case) != n:
    print(None)

# 정렬하기
else :
    score = sorted(n_case)

 # 중간값 도출하기
    mid_val = round(len(score) / 2)

    result = score[mid_val - 1] 

    print(result)