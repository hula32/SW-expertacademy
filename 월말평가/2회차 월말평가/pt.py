# def simulation(i):
# #     num = [0] * 3
# #     visited = [False] * 7
# #
# #     idx = i
# #
# #     while idx < 3:
# #         for j in range(1, 7):
# #             if not visited:
# #                 visited[j] = True
# #                 num[i] = j
# #                 idx += 1
# #                 simulation(i)
# #                 visited[j] = False
# #     return num
# #
# #     number = simulation(1)
# #     print(number)

num = [0] * 3
visited = [False] * 7

result = []
max_val = 0

for i in range(1, 7):
    num[0] = i
    visited[i] = True
    for j in range(1, 7):
        num[1] = j
        visited[j] = True
        for x in range(1, 7):
            num[2] = x
            visited[x] = True
result.append(num)

for n in range(0):
    total = num[n] + num[n+1] + num[n+2]
    if max_val < total:
        max_val = total

print(result)

