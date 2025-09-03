class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population() # increase_population 호출하면 자기 자신 호출
        person.population += 1 # 가능하지 않을까? 똑같음 -> 하지만 설계와 구조에 대해 배우고 있음/ 객체지향적 구조에 따르면 좋은 설계가 아님
    # 클래스 메서드
    @classmethod
    def increase_population(cls):
        cls.population += 1


# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2
