
class Animal:
    num_of_animal = 0

    def __init__(self):
        self.num_of_animal = Animal.num_of_animal
        Animal.num_of_animal += 1

class Dog(Animal):
    def __init__(self):
        super().__init__()


class Cat(Animal):
    def __init__(self):
        super().__init__()


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return (f'동물의 수는 {cls.num_of_animal}마리 입니다.')

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍')

    def sound(self):
        self.sound = "멍멍"
        


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def meow(self):
        print("야옹")
        
    def sound(self):
        self.sound = "야옹"
        

class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()
    #     # self.sound = sound 
    #     pass

    def play(self):
        print("애완동물과 놀기")
    
    def __str__(self):
        return (f"애완동물은 {self.sound} 소리를 냅니다.")

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# dog1 = Dog()
# dog1.bark()

# cat1 = Cat()
# cat1.meow()

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()

result = Pet.sound

print(result)