from turtle import *
import random

class Scenery(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.ts = self.getscreen()
        self.speed(0)
        self.ht()
##
##        self.place = self.ts.numinput('Place', '''What place do you want? Your options are:
##            → island = 1
##            → valley = 2
##            → hills = 3
##            → city = 4
##            → random = 5''', minval = 1, maxval = 5)
##
##        self.time = self.ts.numinput('Time of Day', '''What time of day do you want? Your options are:
##            → morning = 1
##            → midday = 2
##            → evening = 3
##            → random = 4''', minval = 1, maxval = 4)
##
##        self.weather = self.ts.numinput('Weather', '''What weather do you want? Your options are:
##            → rainy = 1
##            → sunny = 2
##            → foggy = 3
##            → snowy = 4
##            → random = 5''', minval = 1, maxval = 5)
##
##        if self.place == 5:
##            self.place = random.randint(1, 4)
##        if self.place == 1:
##            self.island()
##        elif self.place == 2:
##            self.valley()
##        elif self.place == 3:
##            self.hills()
##        elif self.place == 4:
##            self.city()
##
##    def island(self):
##        if self.time == 4:
##            self.time = random.randint(1, 3)
##        if self.time == 1:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 2:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 3:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##
##    def valley(self):
##        if self.time == 4:
##            self.time = random.randint(1, 3)
##        if self.time == 1:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 2:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 3:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##
##    def hills(self):
##        if self.time == 4:
##            self.time = random.randint(1, 3)
##        if self.time == 1:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 2:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 3:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##
##    def city(self):
##        if self.time == 4:
##            self.time = random.randint(1, 3)
##        if self.time == 1:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 2:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##        elif self.time == 3:
##            self.makeBg("stuff") # TODO
##            self.makeMg("stuff") # TODO
##            self.makeFg("stuff") # TODO
##
##    def makeBg(self, color, birds, sunpos, suncolor, clouds, mountains, stars):
##        
##        self.ts.bgcolor(color)
##        
##        if self.sunpos == 1:
##            self.sun(blah, suncolor)
##        elif sunpos == 2:
##            self.sun(blah, suncolor)
##            
##        if mountains:
##            self.mountains(blah)
##            
##        if clouds:
##            self.clouds(blah)
##            
##        if birds == 1:
##            self.birds("stuff") # TODO
##        elif birds == 2:
##            self.birds("stuff") #TODO
##        elif birds == 3:
##            self.birds("stuff") # TODO
##
##        if stars:
##            self.stars(blah)
##
##
##    def makeMg(self, stuff): #TODO
##        pass # TODO
##
##    def makeFg(self, trees, stuff): #TODO
##        pass #TODO

    def birds(self, num): # Working!!!
        for i in range(num):
            self.up()
            self.goto(random.randint(-self.ts.window_width()//2, self.ts.window_height()//2), random.randint(-self.ts.window_height()//2, self.ts.window_height()//2))
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

    def mountains(self, color):
        pass #TODO

    def stars(self, num, color): # Working!!!
        self.color(color)
        for i in range(num):
            self.up()
            self.goto(random.randint(-self.ts.window_width()//2, self.ts.window_height()//2), random.randint(-self.ts.window_height()//2, self.ts.window_height()//2))
            self.down()
            self.dot(10)

s = Scenery()
s.clouds("black", 20, 30, 50)
