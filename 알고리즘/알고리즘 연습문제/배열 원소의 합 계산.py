N = int(input())
arr = list(map(int, input().split()))


# 배열 원소의 합
s = 0

for i in range(N):
    s += arr[i]

print(s)

# 배열 원소 중 최댓값 max_v 찾기
max_v = arr[0]

for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]

print(max_v)


# 배열 원소 중 최댓값의 인덱스 max_idx

max_idx = 0

for i in range(1, N):
    if arr[max_idx] < arr[i]:
        max_idx = i

print(max_idx) # 1 -> 인덱스 호출

# 배열 원소 중 최댓값의 인덱스 max_idx 2 ( 마지막 값으로 인덱스 가져오기)

max_idx = 0

for i in range(1, N):
    if arr[max_idx] <= arr[i]:
        max_idx = i

print(max_idx)


# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1 idx에 넣기
N, V = map(int, input().split())
arr = list(map(int, input().split()))

idx = -1

for i in range(N):
    if arr[i] == V:
        idx = i
        break

print(idx) # 2

