T = int(input())

for t in range(1, T+1):
    N = int(input()) # 전선의 개수

    wires = []
    answer_count = 0

    for n in range(N):
        start, end = map(int, input().split())

        for prev_s, prev_e in wires:
            if start > prev_s and end < prev_e:
                answer_count += 1
            
            elif start < prev_s and end > prev_e:
                answer_count += 1

        wires.append((start, end))

    print(f'#{t} {answer_count}')

