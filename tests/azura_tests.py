import math
from math import *
import random

#misc functions
def Math_Tau(simplification):
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi
    answer = 2 * pi
    return answer

def Math_Pi(simplification):
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi
    answer = pi
    return answer
def Math_E(simplification):
    if simplification == "s":
        e = 2.71
    else:
        e = math.e
    answer = e
    return answer



#circle functions
def Solve_CircleArea(radius, simplification):
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi

    radiussquared = radius * radius
    answer = pi * radiussquared
    return answer


def Solve_CircleCircumference(radius, simplification):
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi

    diameter = radius * 2
    answer = pi * diameter
    return answer


def Solve_CircleDiameter(area, simplification):
    # to get area we use math.pi * r^2, here we reverse engineer it for the diameter.
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi

    answer = area / pi
    answer = sqrt(answer)
    answer = answer * 2
    return answer


def Solve_CircleRadius(area, simplification):
    # to get area we use math.pi * r^2, here we reverse engineer it for the radius.
    if simplification == "s":
        pi = 3.14
    else:
        pi = math.pi

    answer = area / pi
    answer = sqrt(answer)
    return answer

#square functions
def Solve_SquareArea(sidelength):
    answer = sidelength * sidelength
    return answer


def Solve_SquareSideLength(area):
    answer = sqrt(area)
    return answer


def Solve_SquarePerimeter(area):
    answer = sqrt(area)
    answer = answer + answer + answer + answer
    return answer


def Solve_RectangleArea(sidelength):
    answer = sidelength * sidelength
    return answer


def Solve_RectangleSideLength(area, sidelength1):
    answer = area / sidelength1
    return answer


def Solve_RectanglePerimeter(area, sidelength1):
    answer = area / sidelength1
    answer = (answer * 2) + (sidelength1 * 2)
    return answer


def Solve_TrapezoidArea(base1, base2, height):
    answer = (base1 + base2) / 2
    answer = answer * height
    return answer


def Solve_TrapezoidPerimeter(side1, side2, side3, side4):
    answer = side1 + side2 + side3 + side4
    return answer
#Basic Triangle Function
def Solve_TrianglePerimeter(side1, side2, side3):
    answer = side1 + side2 + side3
    return answer
#Right Triangle
def Solve_RightTriangleSide_C(side_a,side_b):
    answer = sqrt(side_a ** 2 + side_b ** 2)
    return answer

def Solve_RightTriangleSide_A(side_b,side_c):
    answer = sqrt(side_c) - sqrt(side_b)
    anser = sqrt(answer)

def Solve_RightTriangleSide_B(side_a,side_c):
    answer = sqrt(side_c) - sqrt(side_a)
    anser = sqrt(answer)

def Rand_Number(number1,number2):
    answer = random.randint(number1,number2)
    return answer