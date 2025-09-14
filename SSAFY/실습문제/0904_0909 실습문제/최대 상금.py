def recur(cnt, path):
    global max_num

    if cnt == k:
        if len(path) == len(num):
            max_num = max(max_num, path)
        return
    
    for idx in range(len(num)):
        recur(cnt+1, path + num[idx])


number, K = input().split()

k = int(K)
max_num = '0'
num = []
for n in number:
    num.append(n)

recur(0, '')
print(max_num)