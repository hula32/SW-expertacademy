l = 1
r = 400
# print((l + r)// 2)

A = 300
cnt = 0

while l < r:
    c = (l + r) // 2
    cnt += 1
    print(f"l={l}, r={r}, c={c}, cnt={cnt}")
    if c == A:
        break
    elif c < A:
        l = c
    else:
        r = c


while l < r:
    c = int(l+r)/2
    cnt +=1

    if c == A:
        break
    if c < A:
        l = c
