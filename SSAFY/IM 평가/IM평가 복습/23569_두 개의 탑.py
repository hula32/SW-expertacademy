# T = int(input())

# for t in range(1, T+1):
#     N, A, B = map(int, input().split())
#     number = list(map(int, input().split()))

N = 5
A = 2
B = 3
number = [7, 3, 4, 1, 5]

Num_t = sorted(number)
num = Num_t[::-1] # [7, 5, 4, 3, 1]


a_val = [] * A
b_val = [] * B

for idx in range(N): # 0,1,2,3,4
    if len(a_val) != A: # 2가 아니면 
        if idx == 0:
            a_val.append(num[idx])
        elif idx % 2 == 0:
            a_val.append(num[idx])
    
    else:
        b_val.append(num[idx])

    
    # if len(a_val) == A:
    #     if idx % 2 == 1:
    #         b_val.append(num[idx])

print(a_val)
print(b_val)

            









