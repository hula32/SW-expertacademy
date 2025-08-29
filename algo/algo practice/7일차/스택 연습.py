N = list(map(int, input().split()))

stack = [] * (len(N)+1)

for n in N:
    stack.append(n)

print(stack)
print(len(stack))

while isemat:
    stack.pop()
else:
    print(-1)


    
