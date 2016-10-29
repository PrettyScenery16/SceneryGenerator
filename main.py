"""
Scenery Generator
Copyright (C) 2016  Proof School Intermediate Python Class 2016-17

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
from turtle import *


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
            → random = 5''', minval=1, maxval=5, default=3)

        self.time = self.ts.numinput('Time of Day', '''What time of day do you want? Your options are:
            → morning = 1
            → midday = 2
            → evening = 3
            → random = 4''', minval=1, maxval=4, default=2)

        self.weather = self.ts.numinput('Weather', '''What weather do you want? Your options are:
            → rainy = 1
            → sunny = 2
            → foggy = 3
            → snowy = 4
            → random = 5''', minval=1, maxval=5, default=2)

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

        self.ts.exitonclick()

    def island(self):  # TODO
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

    def valley(self):  # TODO
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

    def hills(self):  # TODO
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
                self.make_bg("#0000FF", 0, 1, "#FFFF00", 1, "#FFFFFF", False, False, None)
                self.make_fg(10, -.0005, 0, -100, "#00FF00", "#964B00")
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

    def city(self):  # TODO
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

    def make_bg(self, color, birds, sunpos, suncolor, clouds, cloudcolor, mountains, stars, starcolor):

        self.ts.bgcolor(color)

        if stars:
            self.stars(30, starcolor)

        if sunpos == 1:
            self.sun(suncolor)
        elif sunpos == 2:
            self.sun(suncolor)

        if mountains:
            self.mountains(20, 100, 200, -50)

        if clouds == 1:
            self.clouds(cloudcolor, 5, 50, 100)
        elif clouds == 2:
            self.clouds(cloudcolor, 10, 50, 100)
        elif clouds == 3:
            self.clouds(cloudcolor, 20, 50, 100)

        if birds == 1:
            self.birds(10)
        elif birds == 2:
            self.birds(20)
        elif birds == 3:
            self.birds(50)

    def make_mg(self, trees, a, b, c, hcolor, tcolor):
        self.hill_curve(hcolor, a, b, c, 2)
        self.trees_on_hill(trees, a, b, c, tcolor)

    def make_fg(self, trees, a, b, c, hcolor, tcolor):
        self.hill_curve(hcolor, a, b, c, 2)
        self.trees_on_hill(trees, a, b, c, tcolor)

    def birds(self, num):
        self.color("black")
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_height() // 2)
            y = random.randint(0, self.ts.window_height() // 2)
            self.goto(x, y)
            self.down()
            self.begin_fill()
            for j in range(4):
                self.fd(10)
                self.lt(90)
            self.end_fill()

    def sun(self, color):
        self.up()
        self.goto(self.ts.window_width() // 2 - 100, self.ts.window_height() // 2 - 100)
        self.color(color)
        self.down()
        self.dot(100)

    def clouds(self, color, num, sizemin, sizemax):
        self.color(color)
        if sizemin > 20:
            for i in range(num):
                self.up()
                x = random.randint(-self.ts.window_height() // 2, (self.ts.window_height() - sizemax) // 2)
                y = random.randint(0, (self.ts.window_height() - sizemin - 20) // 2)
                self.goto(x, y)
                self.down()
                self.begin_fill()
                x1 = random.randint(sizemin, sizemax)
                y1 = random.randint(sizemin - 20, sizemax - 20)
                for j in range(2):
                    self.fd(x1)
                    self.lt(90)
                    self.fd(y1)
                    self.lt(90)
                self.end_fill()

    def mountains(self, num, sizemin, sizemax, y):
        self.color("black")
        for i in range(num):
            x = random.randint(sizemin, sizemax)
            self.up()
            self.goto(random.randint(-self.ts.window_height() // 2, (self.ts.window_height()) // 2), y)  # WIP
            self.down()
            self.lt(75)
            for j in range(2):
                self.fd(x)
                self.rt(150)
            self.rt(135)

    def stars(self, num, color):
        self.color(color)
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_height() // 2)
            y = random.randint(-self.ts.window_height() // 2, self.ts.window_height() // 2)
            self.goto(x, y)
            self.down()
            self.dot(random.randint(2, 10))

    def hill_curve(self, color, a, b, c, accuracy):
        self.color(color)
        self.up()
        self.goto(-self.ts.window_width()//2, self.parabola_point(a, b, c, -self.ts.window_width()//2))
        self.down()
        self.begin_fill()
        while self.xcor() - accuracy < self.ts.window_width()//2:
            self.goto(self.xcor() + accuracy, self.parabola_point(a, b, c, self.xcor() + 2))
        self.goto(self.ts.window_width() // 2, -self.ts.window_height() // 2)
        self.goto(-self.ts.window_width() // 2, -self.ts.window_height() // 2)
        self.goto(-self.ts.window_width() // 2, self.parabola_point(a, b, c, -self.ts.window_width() // 2))
        self.rt(90)
        self.end_fill()

    @staticmethod
    def parabola_point(a, b, c, x):
        return math.ceil(a*x**2 + b*x + c)

    def trees_on_hill(self, num, a, b, c, color):
        self.color(color)
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_width() // 2 - 30)
            y = random.randint(-self.ts.window_height() // 2 + 30, self.parabola_point(a, b, c, x))
            self.goto(x, y)
            self.down()
            self.begin_fill()
            for j in range(4):
                self.fd(30)
                self.lt(90)
            self.end_fill()

s = Scenery()
