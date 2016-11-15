"""
Scenery Generator: Generates Scenery using Turtle Graphics
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

import math
import random
from turtle import *


class Scenery(Turtle):
    """Scenery Generator"""
    def __init__(self):
        """Calls location functions, stops program at end"""
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
            → random = 4''', minval=1, maxval=4, default=4)

        self.weather = self.ts.numinput('Weather', '''What weather do you want? Your options are:
            → rainy = 1
            → sunny = 2
            → cloudy = 3
            → snowy = 4
            → random = 5''', minval=1, maxval=5, default=5)

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
        """Calls FG/MG/BG for time/weather in Island"""
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
        """Calls FG/MG/BG for time/weather in Valley"""
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

    def hills(self):
        """Calls FG/MG/BG for time/weather in Hills"""
        if self.time == 1:
            if self.weather == 1:
                self.make_bg("#FFB169", 0, 0, "#FFFD7C", 3, "#C69189", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", True, "#77809D", False, 1, 3,
                             "#000000")
            elif self.weather == 2:
                self.make_bg("#FFB169", 0, 0, "#FFFD7C", 0, "#FFFFFF", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 3:
                self.make_bg("#FFB169", 0, 0, "#FFFD7C", 2, "#C69189", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 4:
                self.make_bg("#C2b7da", False, 0, "#FFFF00", 3, "#9AA2AE", False, False, "#000000")
                self.make_fg(True, 10, "#C39E63", True, -.0005, 0, -100, "#B6C6D6", False, "blue", True, 1, 3, "White")
        elif self.time == 2:
            if self.weather == 1:
                self.make_bg("#3f3f3f", 0, 2, "#FFFF00", 3, "#D3D3D3", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "green", True, "blue", False, 1, 3, "#000000")
            elif self.weather == 2:
                self.make_bg("#0000FF", 0, 2, "#FFFF00", 0, "#FFFFFF", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#00FF00", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 3:
                self.make_bg("#0000FF", 0, 1, "#FFFF00", 1, "#FFFFFF", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#00FF00", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 4:
                self.make_bg("#82b7da", False, 2, "#FFFF00", 3, "#9AA2AE", False, False, "#000000")
                self.make_fg(True, 10, "#C39E63", True, -.0005, 0, -100, "#B6C6D6", False, "blue", True, 1, 3,
                             "#DBE3E7")

        elif self.time == 3:
            if self.weather == 1:
                self.make_bg("#FFB169", 0, 1, "#FFFD7C", 3, "#C69189", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", True, "#77809D", False, 1, 3,
                             "#000000")
            elif self.weather == 2:
                self.make_bg("#FFB169", 0, 1, "#FFFD7C", 0, "#FFFFFF", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 3:
                self.make_bg("#FFB169", 0, 1, "#FFFD7C", 2, "#C69189", False, False, None)
                self.make_fg(True, 10, "#964B00", True, -.0005, 0, -100, "#008800", False, "black", False, 1, 3,
                             "#000000")
            elif self.weather == 4:
                self.make_bg("#C2b7da", False, 1, "#FFFF00", 3, "#9AA2AE", False, False, "#000000")
                self.make_fg(True, 10, "#C39E63", True, -.0005, 0, -100, "#B6C6D6", False, "blue", True, 1, 3, "White")

    def city(self):  # TODO
        """Calls FG/MG/BG for time/weather in City"""
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
        """Generates background"""
        self.ts.bgcolor(color)

        if stars:
            self.stars(30, starcolor)

        if sunpos == 1:
            self.sun(suncolor, 1)
        elif sunpos == 2:
            self.sun(suncolor, 2)

        if mountains:
            self.mountains(20, 100, 200, -50)

        if clouds == 1:
            self.clouds(cloudcolor, 5, 50, 100)
        elif clouds == 2:
            self.clouds(cloudcolor, 10, 50, 100)
        elif clouds == 3:
            self.clouds(cloudcolor, 40, 50, 100)

        if birds == 1:
            self.birds(10)
        elif birds == 2:
            self.birds(20)
        elif birds == 3:
            self.birds(50)

    def make_mg(self, trees, a, b, c, hcolor, tcolor):
        """Generates Middleground"""
        self.hill_curve(hcolor, a, b, c, 2)
        self.trees_on_hill(trees, a, b, c, tcolor)

    def make_fg(self, trees, treenum, tcolor, hill, a, b, c, hcolor, rain, rcolor, snow, mins, maxs, scolor):
        """Generates Foreground"""
        if hill:
            self.hill_curve(hcolor, a, b, c, 2)
            if trees:
                self.trees_on_hill(treenum, a, b, c, tcolor)
        if rain:
            self.rain(100, rcolor)
        if snow:
            self.snow(200, mins, maxs, scolor)

    def birds(self, num):  # TODO actual bird shape, spacing/formations?
        """Randomly populates birds in the top half of the screen"""
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

    def sun(self, color, pos):  # TODO positioning
        """Places the sun in one location"""
        if pos is not 0:
            self.up()
            if pos == 2:
                self.goto(self.ts.window_width() // 2 - 100, self.ts.window_height() // 2 - 100)
            elif pos == 1:
                self.goto(0, -75)
            self.color(color)
            self.down()
            self.dot(100)

    def clouds(self, color, num, sizemin, sizemax):  # TODO cloud shapes, spacing?
        """Randonly populates clouds on the top half of the window"""
        self.color(color)
        if sizemin > 20:
            for i in range(num):
                self.up()
                x = random.randint(-self.ts.window_height() // 2, (self.ts.window_height() - 3 * sizemax) // 2)
                y = random.randint(0, (self.ts.window_height() - sizemax) // 2)
                self.goto(x, y)
                self.down()
                self.begin_fill()
                thex = self.xcor()
                they = self.ycor()
                for i in range(2):
                    self.dot(random.randint(sizemin, sizemax))
                    self.fd(random.randint(sizemin // 2, sizemax // 2))
                self.circle(random.randint(sizemin, sizemax))
                self.end_fill()

    def mountains(self, num, sizemin, sizemax, y):  # TODO filling, bottoms, spacing
        """Randomly populates mountains on a given line in y = a form"""
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
        """Randomly populates stars"""
        self.color(color)
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_width() // 2)
            y = random.randint(-self.ts.window_height() // 2, self.ts.window_height() // 2)
            self.goto(x, y)
            self.down()
            self.dot(random.randint(2, 10))

    def rain(self, num, color):  # TODO shapes? sizes? color?
        """Randomly populates rain"""
        self.color(color)
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_width() // 2)
            y = random.randint(-self.ts.window_height() // 2, self.ts.window_height() // 2)
            self.goto(x, y)
            self.down()
            self.dot(random.randint(1, 5))

    def hill_curve(self, color, a, b, c, accuracy):  # TODO smoothing, more hills?
        """Draws a parabola, fills in space between parabola and bottom of window"""
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
        """Finds points on a parabola for self.hill_curve()"""
        return math.ceil(a * x ** 2 + b * x + c)

    def trees_on_hill(self, num, a, b, c, color):  # TODO tree shapes, spacing?
        """Draws trees below parabola y = ax^2+bx+c"""
        self.color(color)
        for i in range(num):
            self.up()
            x = random.randint(-self.ts.window_width() // 2 + 30, self.ts.window_width() // 2 - 30)
            y = random.randint(-self.ts.window_height() // 2 + 30, self.parabola_point(a, b, c, x))
            self.goto(x, y)
            self.down()
            self.begin_fill()
            for j in range(4):
                self.fd(30)
                self.lt(90)
            self.end_fill()
    def tree(self, levels, sidelength,red,green,blue):
        self.pencolor(139, 69, 19)
        branches = random.choice([1,1,1,1,1,2,2])
        angle = random.randint(1,5)
        sidelength = random.randint(10,20)
        self.pensize((levels+2)-levels/levels)
        if (levels == 1):
            self.forward(sidelength)
            self.backward(sidelength)
        elif (levels == 2):
            branchangle = random.randint(10,30)
            self.forward(sidelength)
            self.left(branchangle)
            self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
            self.right(branchangle)
            self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
            self.right(branchangle)
            self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
            self.left(branchangle)
            self.backward(sidelength)
        else:
            if branches == 1:
                branchangle = random.randint(15,30)
                self.forward(sidelength)
                self.left(branchangle)
                self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
                self.right(branchangle*2)
                self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
                self.left(branchangle)
                self.backward(sidelength)
            else:
                branchangle = random.randint(10,30)
                self.forward(sidelength)
                self.left(branchangle)
                self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
                self.right(branchangle)
                self.tree(levels-branches, angle*sidelength/random.randint(angle,angle+5))
                self.right(branchangle)
                self.tree(levels-1, angle*sidelength/random.randint(angle,angle+5))
                self.left(branchangle)
                self.backward(sidelength)
    def snow(self, num, mins, maxs, color):  # TODO shape?
        """Randomly populates snow"""
        self.color(color)
        for i in range(num):
            x = random.randint(-self.ts.window_width() // 2, self.ts.window_width() // 2)
            y = random.randint(-self.ts.window_height() // 2, self.ts.window_height() // 2)
            self.up()
            self.goto(x, y)
            self.down()
            self.dot(random.randint(mins, maxs))
    def ellipse(self):
        t.shape('circle')
    t.shapesize(5,4,1)
    fillcolor("white")
    t.shape('turtle')

s = Scenery()
