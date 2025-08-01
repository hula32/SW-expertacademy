class Person:
    # 생성자 메서드
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print("인스턴스가 생성되었습니다.") # 어떤 타이밍에 호출되는 지 확인 여부
    
    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

person1 = Person("지민") # 인스턴스가 생성되었습니다.
print(person1.name) # 지만
person1.greeting() # 안녕하세요 지민입니다.


# 초기값이 없어도 알아서 빈생성자 메서드라도 만들어두는 것을 명시
# def __init__(self):
#     pass