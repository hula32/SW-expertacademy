class Counter:
    def __init__(self): # 어떤 범주로 보면 인스턴스 변수
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        self.count += 1 # self 붙이는 이유는 호출하는 인스턴스 변수에 적용하기 때문


c1 = Counter()
c2 = Counter()

# 인스턴스 메서드 호출
c1.increment() # c1.count += 1 의미
print(c1.count) # 1
print(c2.count) # 0 / c2를 호출한 적 없기 때문에 0
