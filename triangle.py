def is_triangle(x, y, z):
    if z > (x+y) or y > (x+z) or x > (y+z):
        print('No')
    else:
        print('Yes')

def triangle():
    x = int(input('Please enter the length of the 1st stick:\n'))
    y = int(input('Please enter the length of the 2nd stick:\n'))
    z = int(input('Please enter the length of the 3rd stick:\n'))
    is_triangle(x, y, z)
triangle()


