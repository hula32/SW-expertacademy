
T = int(input())
 
def make_pascal(N):
    pascal = []
    for i in range(1, N+1): # 1, 2, 3, 4
        row = [0]*i
        if i == 1:
            row[0] = 1
        else:
            row[0] = row[-1] = 1
        
        if i >= 3:
            before_row = pascal[-1]

            for j in range(len(row)):
                if row[j] == 0:
                    row[j] = before_row[j] + before_row[j-1]
        pascal.append(row)
    
    return pascal

for t in range(1, T+1):
    N = int(input())

    print(f'#{t}')
    print(make_pascal(N))