# 조건 1 : 1일권
# 조건 2 : 1달권
# 조건 3 : 3달권 
# 조건 4 : 1년권
# 조건 5 : 가장 적은 비용으로 수영장을 이용할 수 있는 방법 -> 비용 도출

T = int(input())

def recur(month, total):
    global min_val
    if month > 12:
        min_val = min(min_val, total)
        return
    
    # 1일권
    recur(month + 1, total + (day * swimming[month]))
    # 1달권
    recur(month + 1, total + month_1)
    # 3달권
    recur(month + 3, total + month_3)
    # 1년권
    recur(month + 12, total + year)


for t in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split())
    swimming = [0] + list(map(int, input().split()))
    min_val = 31 * 12 * 3000
    recur(1, 0)
    print(f'#{t} {min_val}')

    