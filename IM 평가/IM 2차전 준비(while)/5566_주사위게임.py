# 출발점 1칸, 도착점 N칸
# 각 칸에는 지시 사항 있음(말이 얼만큼 이동해야 하는가)
# 주사위 굴리기 -> 주사위 눈의 수만큼 칸 이동 -> 도착한 칸에 쓰여있는 지시만큼 말 이동하기 
# 지시사항 이동 후에는 지시 따르지 않기
# N칸 넘어도 도착
# 몇 번 만에 도착하는가?

def game(arr, number):
    N = len(arr) # 10

    work = 0 # 이동 위치
    cnt = 0 # 주사위 돌린 횟수

    for m in number: # 1,3,5,1,5
        work += m
        cnt += 1

        if work >= N:
            return cnt
        
        work += arr[work]

        if work >= N:
            return cnt
        
    return cnt


N, M = map(int, input().split()) # N개의 줄, M 주사위 던진 횟수

arr = []
for n in range(N):
    arr.append(int(input()))

number = []
for m in range(M):
    number.append(int(input()))

print(game(arr, number))




def game(numbers, cnt_list):

    i = 0 # 이동위치
    cnt = 0 # 이동횟수

    for j in range(M): # 0,1,2,3,4
        i += cnt_list[j]
        if i >= N:
            return cnt + 1
        i += numbers[i]
        if i >= N:
            return cnt + 1
        cnt += 1

    return cnt

N, M = map(int, input().split())

numbers = [0] * (N)
for n in range(N):
    num = int(input())
    numbers[n] = num

cnt_list = []
for m in range(M):
    cnt = int(input())
    cnt_list.append(cnt)


print(game(numbers, cnt_list))







