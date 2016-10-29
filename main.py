from turtle import *
import random
import math

class Scenery(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.ts = self.getscreen()
        self.speed(0)
        self.ht()

        self.place = self.ts.numinput('Place', '''What place do you want? Your options are:
            → island = 1
            → valley = 2
            → hills = 3
            → city = 4
            → random = 5''', minval = 1, maxval = 5)

        self.time = self.ts.numinput('Time of Day', '''What time of day do you want? Your options are:
            → morning = 1
            → midday = 2
            → evening = 3
            → random = 4''', minval = 1, maxval = 4)

        self.weather = self.ts.numinput('Weather', '''What weather do you want? Your options are:
            → rainy = 1
            → sunny = 2
            → foggy = 3
            → snowy = 4
            → random = 5''', minval = 1, maxval = 5)

        if self.weather == 5:
            self.weather = random.randint(1, 4)

        if self.time == 4:
            self.time = random.randint(1, 3)

        if self.place == 5:
            self.place = random.randint(1, 4)

        if self.place == 1:
            self.island()
        elif self.place == 2:
            self.valley()
        elif self.place == 3:
            self.hills()
        elif self.place == 4:
            self.city()

    def island(self): # TODO
        if self.time == 1:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
        elif self.time == 2:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
            elif self.time == 3:
                pass
        elif self.time == 3:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass

    def valley(self): # TODO
        if self.time == 1:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
        elif self.time == 2:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
            elif self.time == 3:
                pass
        elif self.time == 3:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass

    def hills(self): # TODO
        if self.time == 1:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
        elif self.time == 2:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
            elif self.time == 3:
                pass
        elif self.time == 3:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass

    def city(self): # TODO
        if self.time == 1:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
        elif self.time == 2:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass
            elif self.time == 3:
                pass
        elif self.time == 3:
            if self.weather == 1:
                pass
            elif self.weather == 2:
                pass
            elif self.weather == 3:
                pass
            elif self.weather == 4:
                pass

    def makeBg(self, color, birds, sunpos, suncolor, clouds, cloudcolor, mountains, stars, starcolor):

        self.ts.bgcolor(color)

        if stars:
            self.stars(30, starcolor)

        if sunpos == 1:
            self.sun(suncolor)
        elif sunpos == 2:
            self.sun(suncolor)

        if mountains:
            self.mountains(20, 100, 200, -50)

        if clouds:
            self.clouds(cloudcolor, 10, 50, 100)

        if birds == 1:
            self.birds(10)
        elif birds == 2:
            self.birds(20)
        elif birds == 3:
            self.birds(50)




    def makeMg(self, trees, a, b,c ):
        self.hillCurve("#000000", a, b, c, 2)
        self.trees(trees)

    def makeFg(self, trees, a, b,c ):
        self.hillCurve("#000000", a, b, c, 2)
        self.trees(trees)

    def birds(self, num):
        self.color("black")
        for i in range(num):
            self.up()
            self.goto(random.randint(-self.ts.window_width()//2, self.ts.window_height()//2), random.randint(0, self.ts.window_height()//2))
            self.down()
            for i in range(4):
                self.fd(10)
                self.lt(90)

    def sun(self, color):
        self.up()
        self.goto(self.ts.window_width()//2, self.ts.window_height()//2)
        self.color(color)
        self.down

    def clouds(self, color, num, sizemin, sizemax):
        self.color(color)
        if sizemin>20:
            for i in range(num):
                x = random.randint(sizemin, sizemax)
                y = random.randint(sizemin-20, sizemax-20)
                self.up()
                self.goto(random.randint(-self.ts.window_height()//2, (self.ts.window_height()-x)//2), random.randint(0, (self.ts.window_height()-y)//2))
                self.down()
                for i in range(2):
                    self.fd(x)
                    self.lt(90)
                    self.fd(y)
                    self.lt(90)

    def mountains(self, num, sizemin, sizemax, y):
        self.color("black")
        for i in range(num):
            x = random.randint(sizemin, sizemax)
            self.up()
            self.goto(random.randint(-self.ts.window_height()//2, (self.ts.window_height())//2), y) #WIP
            self.down()
            self.lt(75)
            for i in range(2):
                self.fd(x)
                self.rt(150)
            self.rt(135)

    def stars(self, num, color):
        self.color(color)
        for i in range(num):
            self.up()
            self.goto(random.randint(-self.ts.window_width()//2, self.ts.window_height()//2), random.randint(-self.ts.window_height()//2, self.ts.window_height()//2))
            self.down()
            self.dot(random.randint(2, 10))

    def hillCurve(self, color, a, b, c, accuracy):
        self.color(color)
        self.up()
        self.goto(-self.ts.window_width()//2, self.parabola_point(a, b, c, -self.ts.window_width()//2))
        self.down()
        while self.xcor() - accuracy < self.ts.window_width()//2:
            self.goto(self.xcor() + accuracy, self.parabola_point(a, b, c, self.xcor() + 2))

    def parabola_point(self, a, b, c, x):
        return math.ceil(a*x**2 + b*x + c)

    def trees(self, num):
        self.color("black")
        for i in range(num):
            self.up()
            self.goto(random.randint(-self.ts.window_width()//2, self.ts.window_width()//2), random.randint(-self.ts.window_height()//2, self.ts.window_height()//2))
            self.down()
            for i in range(4):
                self.fd(30)
                self.lt(90)
        

s = Scenery()
s.makeFg(4, -.0005, 0, -100)
s.ts.exitonclick()

