
# a = [1]

# b = [1, 1]

# c = [1, 2, 1]

# d = [1, 3, 3, 1]


# arr = [0, 0, 0, 0, 0]

# arr[0] = arr[4] = 1
# arr[1] = d[0] + d[1]
# arr[2] = d[1] + d[2]
# arr[3] = d[2] + d[3]

# print(arr)


def make_pascal(N):
    pascal = []
    for i in range(1, N+1):
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


print(f'#{t}')
print()