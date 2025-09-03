# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def print_info(self):
        return print(f'Width: {self.width}\nHeight: {self.height}\nArea: {self.width * self.height}\nPerimeter: {(self.width * 2) + (self.height * 2)}')

    


shape1 = Shape(5, 3)
shape1.print_info()