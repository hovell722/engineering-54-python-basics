# functions
# practice using, defining and calling functions

# Build a basic object functional calculator
# phase 1: build a function containing add, subtract, multiply, divide

# phase 2: find area of a circle, triangle and square

import math

def calc_add(x, y):
    return x + y

print("Calling calc_add() with 30 and 10, expect 40 to be result")
print(calc_add(30, 10) == 40)
print('got: ', calc_add(30, 10))

def calc_subtract(x, y):
    return x - y

print("Calling calc_subtract() with 30 and 10, expect 20 to be result")
print(calc_subtract(30, 10) == 20)
print('got: ', calc_subtract(30, 10))

def calc_multiply(x, y):
    return x * y

print("Calling calc_multiply() with 30 and 10, expect 300 to be result")
print(calc_multiply(30, 10) == 300)
print('got: ', calc_multiply(30, 10))

def calc_divide(x, y):
    return x / y

print("Calling calc_divide() with 30 and 10, expect 3 to be result")
print(calc_divide(30, 10) == 3)
print('got: ', calc_divide(30, 10))

def square_area(height, length):
    return height * length

print("Calling square_area() with 30 and 10, expect 300 to be result")
print(square_area(30, 10) == 300)
print('got: ', square_area(30, 10))

def triangle_area(height, length):
    return height * length * 0.5

print("Calling triangle_area() with 30 and 10, expect 150 to be result")
print(triangle_area(30, 10) == 150)
print('got: ', triangle_area(30, 10))

def circle_area(radius):
    return (radius ** 2) * math.pi

print("Calling circle_area() with 30, expect 2827.4333882308138 to be result")
print(circle_area(30) == 2827.4333882308138)
print('got: ', circle_area(30))

def sphere_volume(radius):
    return 4 / 3 * (radius ** 3) * math.pi

print("Calling sphere_volume() with 30, expect 113097.33552923256 to be result")
print(sphere_volume(30) == 113097.33552923256)
print('got: ', sphere_volume(30))

def fibonacci(n):
    # n is the nth number in the sequence
    # a is 1st n in sequence, b is 2nd
    a = 0
    b = 1
    # n cannot be less than 0
    if n < 0:
        print("Incorrect input")
    # n == 0 will return 0th number in sequence
    elif n == 0:
        return a
    # n == 1 will return 1st number in sequence
    elif n == 1:
        return b
    # else will calculate rest of the numbers
    else:
        # need to use a for loop to get rest of values
        # must be in range from 2nd number to nth number
        for i in range(2, n+1):
            # n2 = n1 + n0
            c = a + b
            # defines new n0 = previous iterations n1
            a = b
            # defines new n1 = previous iterations n2
            b = c
        # will always return iterations n2
        return b

print("Calling fibonacci() with 8, expect 21 to be result")
print(fibonacci(8) == 21)
print('got: ', fibonacci(8))

