<<<<<<< HEAD
T = int(input())

for t in range(1, T+1):
    N = int(input())

    total = 0

    for n in range(1, N+1):
        if n % 2 != 0:
            total += n
        else:
            total -= n
    
=======
T = int(input())

for t in range(1, T+1):
    N = int(input())

    total = 0

    for n in range(1, N+1):
        if n % 2 != 0:
            total += n
        else:
            total -= n
    
>>>>>>> 075f6b5d78fd04aa8995c922e2d2f6abf160e832
    print(f'#{t} {total}')