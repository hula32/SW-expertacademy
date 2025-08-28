number1 = {
    0 : "ZRO",
    1 : "ONE",
    2 : "TWO",
    3 : "THR",
    4 : "FOR",
    5 : "FIV",
    6 : "SIX",
    7 : "SVN",
    8 : "EGT",
    9 : "NIN"
}

number2 = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9}


T = int(input())

for t in range(1, T+1):
    N = list(map(str, input(). split()))
    M = list(map(str, input(). split()))

    num = [] # [7, 4, 0, 9, 4, 8, 8, 2]

    for m in M:
        num.append(number2[m])

    result = []
    nums = sorted(num)
    for n in nums:
        result.append(number1[n])

    print(f'#{t}')
    print(*result)













    

    






    