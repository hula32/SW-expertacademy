N = 9
txt = 'algorithm'

def is_palindrome(N, txt):
    for i in range(N//2): # 0,1,2,3
        if txt[i] != txt[N-1-i]: # i : 0,1,2,3 , [N-1-i]: 8,7,6,5
            return False
    return True

print(is_palindrome(N, txt))

