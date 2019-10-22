#HW OOP1

import math

class line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        print ("New Line Created!")

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

coor1 = (3,2)
coor2 = (8,10)

li = line(coor1,coor2)

print("distance is {} and slope is {}".format(li.distance(),li.slope()))
