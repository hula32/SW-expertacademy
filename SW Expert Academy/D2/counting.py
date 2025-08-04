nums = [4, 9, 6, 7, 9]
cnt = [0] * 10

for num in nums:
    cnt[num] += 1

print(cnt) # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]


max_val = 0 # 2
max_idx = -1 # 9

for idx, c in enumerate(cnt):
    if c > max_val:
        max_val = c
        max_idx = idx

print(max_idx, max_val)

