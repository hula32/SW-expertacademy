N = int(input())
seat = input()

i = 0
cnt = 0

while i != N:
    if i == 0:
        cnt += 1
    if seat[i] == 'S':
        cnt += 1
        i += 1
    elif seat[i] == 'L':
        cnt += 1
        i += 2

if cnt <= i:
    print(cnt)
else:
    print(i)


