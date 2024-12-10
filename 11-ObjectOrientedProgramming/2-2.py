class Square:
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a
    def perimiter(self):
        return self.a * 4


square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimiter()}')
print ('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimiter()}')