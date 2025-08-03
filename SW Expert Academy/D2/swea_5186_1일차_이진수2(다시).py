T = int(input())

for t in range(1, T+1):
    t_case = float(input())
    num = t_case - int(t_case)

    result = ''
    count = 0

    while num != 0:
        num = num * 2
        a = int(num)
        result += str(a)
        num = num - a
        count += 1

        if count > 13:
            print('overflow')
            break
    
    print(f'#{t} {result}')
