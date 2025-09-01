T = int(input())

for t in range(1, T+1):
    word = input().strip() # I.evol.YFASS

    N = len(word)

    word_n = word.split(".") # ['I', 'evol', 'YFASS']

    result = [] # ['.I', '.love', '.SSAFY']
    for w in word_n:
        result.append("." + w[::-1]) # 사이사이 "." 넣기


    total = []
    for i in range(len(result)):
        for r in result[i]: # . I . l o v e . S S A F Y
            total.append(r)

    real = []
    for j in range(1, len(total)):  # 맨 앞에 있는 점 빼기
        real.append(total[j])


    print(f"#{t}", *real)



