def my_function():
    print("hello")
    my_function # 종료 조건을 설정해서 재귀 호출이 멈추도록 함

my_function()

def factorial(n):
    if n == 0 :
        return 1
    else :
        return n * factorial(n - 1)
    
print(factorial(5))