T = int(input())

def is_run(cards):
    cards = sorted(cards)
    return cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2] 

def is_triplet(cards):
    return cards[0] == cards[1] == cards[2]

def recur(cards, cnt, start, path):
    global run_flag, triplet_flag

    if cnt == 3:
        if is_run(path) or is_triplet(path):
            run_flag, triplet_flag = True, True
            return 
        
    for i in range(start, len(cards)):
        path.append(cards[i])
        recur(cards, cnt + 1, i + 1, path)
        path.pop()     

for t in range(1, T+1):
    cards = list(map(int, input().split()))

    p1 = []
    p2 = []

    winner = 0

    for idx in range(12):
        if idx % 2 == 0:
            p1.append(cards[idx])

            if len(p1) >= 3:
                run_flag, triplet_flag = False, False
                recur(p1, 0, 0, [])
                if run_flag or triplet_flag:
                    winner = 1
                    break

        else:
            p2.append(cards[idx])

            if len(p2) >= 3:
                run_flag, triplet_flag = False, False
                recur(p2, 0, 0, [])
                if run_flag or triplet_flag:
                    winner = 2
                    break

    print(f'#{t} {winner}')