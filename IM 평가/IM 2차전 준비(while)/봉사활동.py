T = int(input())

for t in range(1, T+1):
    N, min, max = map(int, input().split())
    scores = list(map(int, input().split()))

    min_diff = 9999999

    for score1 in range(1, 101):
        for score2 in range(score1, 101):

            cls_cnt = [0] * 3

            for score in scores:
                if score < score1:
                    cls_cnt[0] += 1
                elif score < score2:
                    cls_cnt[1] += 1
                else:
                    cls_cnt[2] += 1

            for i in range(3):
                if cls_cnt[i] < min and cls_cnt[i] > max:
                    break
            else:
                min_cnt = 9999999
                max_cnt = 0
                for i in range(3):
                    if cls_cnt[i] < min_cnt:
                        min_cnt = cls_cnt[i]
                    if cls_cnt[i] > max_cnt:
                        max_cnt = cls_cnt[i]
                diff = max_cnt - min_cnt
                if min_diff > diff:
                    min_diff = diff
    
    if min_diff == 9999999:
        print(f'#{t} 0')
    else:
        print(f'#{t} {min_diff}')
