#HW OOP Cylinder
import math

class Cylinder:
    def __init__(self,height,rad):
        self.height = height
        self.rad = rad

    def vol(self):
        vol = math.pi*(self.rad**2)*self.height
        return vol

    def surface_area(self):
        surface_area = (2*math.pi*self.rad**2) + self.height*(2*math.pi*self.rad)
        return

c = Cylinder(2,3)

print("volume is {} and surface area is {} ".format(c.vol(),c.surface_area()))