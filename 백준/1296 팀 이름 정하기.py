name = input().strip()
N = int(input())

# team = []
# for n in range(N):
#     team_name = input().strip()
#     team.append(team_name)

# team_r = sorted(team)
# result = []
# max_val = -1

# for i in range(len(team_r)):
#     cnt = [0] * 4
#     for t in team_r[i]:
#         if t == 'L':
#             cnt[0] += 1
#         elif t == 'O':
#             cnt[1] += 1
#         elif t == 'V':
#             cnt[2] += 1
#         elif t == 'E':
#             cnt[3] += 1

#     total = ((cnt[0]+cnt[1]) * (cnt[0]+cnt[2]) * (cnt[0]+cnt[3]) * (cnt[1]+cnt[2]) * (cnt[1]+cnt[3]) * (cnt[2]+cnt[3])) % 100

#     if max_val <= total:
#         max_val = total
#         result = team_r
# result.sort()
# print(result[0])

# 실패