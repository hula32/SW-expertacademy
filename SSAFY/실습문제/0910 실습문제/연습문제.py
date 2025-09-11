def recur(cnt, total, subset):
    if total == 10:
        print(subset)
        return
    
    if total > 10:
        return
    
    if cnt == 10:
        return
    
    recur(cnt + 1, total + arr[cnt], subset + [arr[cnt]])
    recur(cnt + 1, total, subset)


arr = [i for i in range(1, 11)]

recur(0, 0, [])
