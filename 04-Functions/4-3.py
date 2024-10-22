import math

def triangle_area(a,b,c):
    half_triangle = (1/2)*(a+b+c)
    area = math.sqrt(half_triangle*(half_triangle-a)*(half_triangle-b)*(half_triangle-c))
    return area

print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area(3,4,5)}')
print(f'The area of a triangle with sides 5, 12, 13 is {triangle_area(5,12,13)}')
print(f'The area of a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')