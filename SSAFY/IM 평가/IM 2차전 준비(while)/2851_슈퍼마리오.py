result = []
for n in range(1, 11):
    num = int(input())
    result.append(num)

i = 0
total = 0
new_total = 0 #prev

while i < 10:
    new_total = total # 바뀐부분
    total += result[i]
    i += 1

    if total == 100:
        print(total)
        break

    elif total > 100:
        if  abs(total - 100) < abs(new_total - 100):
            print(total)
        elif abs(total - 100) == abs(new_total - 100):
            print(total)
        else:
            print(new_total)
        break
else:
    print(total) # 바뀐부분



