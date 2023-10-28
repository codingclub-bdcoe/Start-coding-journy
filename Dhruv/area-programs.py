import math
def area_finder(mode):
    if mode == '0':
        base = input('Give the length of a base\n')
        height = input('Give the length of a height\n')
        print(f'The area of the triangle is {0.5*(int(base)*int(height))}')
    elif mode == '1':
        radius = input('Give the length of a radius\n')
        print(f'The area of the triangle is {math.pi*(int(radius)**2)}')


mode = input('Find Area of Triangle(0) or Circle(1)\n')
if mode != 0 and mode != 1:
    print('Select 0 for triangle and 1 for area')
    mode = input('Find Area of Triangle(0) or Circle(1)\n')
area_finder(mode)