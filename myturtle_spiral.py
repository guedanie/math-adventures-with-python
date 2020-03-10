## Creates a spiral of squares. Function spiral creates a single square,
## and the second loop runs that function 60 times, increasing the length
## after drawing a square. 

from turtle import *
shape('turtle')
speed(10)

def spiral(length):
    for i in range(4):
        forward(length)
        right(90)
        
length = 5
for i in range(60):
    spiral(length)
    right(5)
    length += 5 
