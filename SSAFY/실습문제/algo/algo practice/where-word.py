arr = [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]


# 2개짜리는 몇개?
# 3개짜리, 4개짜리는 몇개...

# 연속된 1의 개수 구하기
cnt = 0
for i in range(len(arr)):
    if arr[i] == 1:
        cnt += 1
    elif arr[i] == 0:
        print(f"{cnt}개 연속된 1 발견!")
        cnt = 0
    print(i, arr[i], cnt)
if cnt != 0:
    print(f"{cnt}개 연속된 1 있음.")