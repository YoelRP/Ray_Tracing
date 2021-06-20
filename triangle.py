from math import sqrt
import sys
import numpy as np
from ray import Ray
from point import Point
from vector import Vector
class Triangle:
    def __init__(self,id, point1, point2, point3, material, upset=Point(0, 0, 0)):
        self.id = id
        self.point1 = point1 + upset
        self.point2 = point2 + upset
        self.point3 = point3 + upset
        self.edge1 = point2-point1
        self.edge2 = point3-point1
        self.material = material
        self.mynormal = (self.edge1.cross_product(self.edge2)).normalize()

    def  intersects(self, ray):
        dir_cross_e2 = self.edge2.cross_product(ray.direction)
        det = dir_cross_e2.dot_product(self.edge1)
        if (abs(det)<sys.float_info.epsilon):
            return None
        f = 1.0 / det
        p1_to_origin = self.point1 - ray.origin
        u = f * p1_to_origin.dot_product(dir_cross_e2)
        if u < 0.0 or u > 1.0:
            return None

        origin_cross_e1 = p1_to_origin.cross_product(self.edge1) 
        v = f * ray.direction.dot_product(origin_cross_e1)
        if v < 0.0 or (u + v) > 1.0:
            return None

        t = f * self.edge2.dot_product( origin_cross_e1)
        return  t

    def normalf(self,surface_point):
        return self.mynormal
    
    def compare(self, other):
        if (self.point1 == other.point1 and self.point2 == other.point2 and self.point3 == other.point3 and self.material == other.material):
            return True
        else:
            return False
