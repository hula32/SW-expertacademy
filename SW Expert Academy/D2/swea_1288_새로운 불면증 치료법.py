# T = int(input())

# for t in range(1, T+1):
#     N = int(input())


N = 1295

cnt = 0
nums = set()

i = 1
while True:
    if len(nums) == 10:
        result = total
        break

    total = N * i
    
    for num in list(str(total)):
        nums.add(num)

    cnt += 1
    i += 1
    


print(result)


    