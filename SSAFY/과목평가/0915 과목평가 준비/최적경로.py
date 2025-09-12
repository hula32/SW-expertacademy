# 조건 1 : 중복되지 않은 모든 경로 방문
# 조건 2 : 가장 짧은 경로
# 조건 3 :|x1 - x2|+|y1 - y2|

N = int(input())
num = list(map(int, input().split()))

for i in range(0, len(num), 2):
    company, home, *client = (num[i], num[i+1])
    print(company)
    # print(home)
    # print(client)
