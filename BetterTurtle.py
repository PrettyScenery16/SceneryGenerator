from turtle import *
import random

class PTurtle(Turtle):
    
    def __init__(self, inputname = "You Lost"):
        Turtle.__init__(self)
        self.name = inputname
        colormode(255)
    def square(self, sidelength):
        for i in range(4):
            self.forward(sidelength)
            self.right(90)
    def polygon(self, sidelength, sides):
        for i in range(sides):
            self.forward(sidelength)
            self.right(360/sides)
    def rectangle(self, sidelength1, sidelength2):
        self.forward(sidelength1)
        self.right(90)
        self.forward(sidelength2)
        self.right(90)
        self.forward(sidelength1)
        self.right(90)
        self.forward(sidelength2)
        self.right(90)
    def TROLL(self):
        print("I trolled you with recusion!!!!")
        try:
            self.getscreen().bgcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.TROLL()
        except:
            self.TROLL()
    def randompencolor(self):
        self.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def drawName(self):
        self.write(self.name, font = ("Ariel", 32, "normal"))
    def turndown(self):
        self.right(self.towards(self.xcor(), (self.ycor() + 1)))
    def turnup(self):
        self.right(self.towards(self.xcor(), (self.ycor() - 1)))
