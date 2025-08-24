N = int(input())

i = 665
cnt = 0

while cnt != N:
    i += 1 # 666
    for n in range(len(str(i)) - 2): # 3 / 0
        if int(str(i)[n]) == 6 :
            if int(str(i)[n+1]) == 6 and int(str(i)[n+2]) == 6:
                cnt += 1
                break

print(i)





