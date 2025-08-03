
class Animal:
    num_of_animal = 0

    def __init__(self):
        self.num_of_animal = Animal.num_of_animal
        Animal.num_of_animal += 1

class Dog(Animal):
    sound = "멍멍"

    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍멍')

    # def sound(self):
    #     self.sound = "멍멍"
        

class Cat(Animal):
    sound = "야옹"

    def __init__(self):
        super().__init__()

    def meow(self):
        print("야옹")
        
    # def sound(self):
    #     self.sound = "야옹"
        

class Pet(Dog, Cat):

    def __init__(self):
        super().__init__()

    def play(self):
        print("애완동물과 놀기")
    
    def __str__(self):
        return (f"애완동물은 {self.sound} 소리를 냅니다.")


# result = Pet()

# print(result)

print(Pet())