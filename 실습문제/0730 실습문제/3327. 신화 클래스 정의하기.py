class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        # self.name2 = name2
        Myth.increase_type_of_myth()

    @classmethod
    def increase_type_of_myth(cls):
        cls.type_of_myth += 1

    def __str__(self):
        return self.name
    
    # def introduce(self):
        # return (f'{self.name} & {self.name2}')

    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')


p1 = Myth('dangun')
p2 = Myth('greek')
p3 = Myth('rome')

print(p1.name)
print(p2.name, '&', p3.name)
print(Myth.type_of_myth)
Myth.description()