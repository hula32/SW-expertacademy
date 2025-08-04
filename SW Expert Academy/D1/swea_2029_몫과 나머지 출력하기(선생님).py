T = int(input())
i = 1

for i in range(1, T + 1):             # 주어진 테스트 갯수만큼 input 받기
    a , b = map(int,input().split())
    print('#'+str(i), a // b, a % b) 


