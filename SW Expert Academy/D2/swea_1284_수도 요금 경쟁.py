T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = list(map(int, input().split()))

    # A사 수도요금
    A_charge = W * P

    # B사 수도요금
    B_charge = 0
    if W > R:
        B_charge += ((W-R) * S) + Q
    else:
        B_charge += Q

    if A_charge > B_charge:
        print(f'#{t} {B_charge}')
    else:
        print(f'#{t} {A_charge}')