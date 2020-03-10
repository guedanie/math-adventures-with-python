from turtle import *
shape('turtle')
speed(5)
def square(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)
for i in range(70):
    square(80)
    right(5)
