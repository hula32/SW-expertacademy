# 본인보다 2이상 큰 수 일 경우 오르막길 시작
# 연달아서 2이상 커질 경우 오르막길 계속
# 만약 본인보다 같거나 작은 수를 만나면 오르막길 종료
# 오르막길 시작 숫자와 끝 숫자의 차이가 오르막길 크기
# 그 크기를 비교해서 큰 오르막길 도출 

N = int(input())
hight = list(map(int, input().split())) # 1 2 1 4 6

h = []
state = 0

for i in range(N-1): # 0,1,2,3,4
    if hight[i+1] - hight[i] >= 1: # 본인보다 1이상 큰 수면 1로 변경
        state += 1
    elif state >= 1 and hight[i+1] - hight[i] <= 1: # st가 1 이상인데, 다음 수가 작을 경우, 결과 도출
        result = hight[i] - hight[i-state]
        h.append(result)
        state = 0
    else:
        h.append(0)

if state >= 1:
    result = hight[-1] - hight[-1-state]
    h.append(result)

max_val = max(h)
print(max_val)