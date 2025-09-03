N = int(input())
number = list(map(int, input().split()))

max_val = 0
cnt = []

for i in range(N-1):
    if number[i] < number[i+1]:
        cnt.append(number[i])

    else:
        max_val = cnt[-1] - cnt[0]
        cnt = []
    


print(max_val)

