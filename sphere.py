from math import sqrt
from point import Point
class Sphere:
    #is the only 3d shape implemente has a radios,center and material
    def __init__(self,id, center, radios, material, upset = Point(0,0,0)):
        self.center = center + upset
        self.radios = radios
        self.material = material
        self.id = id

    def  intersects(self, ray):
        #the ray intersects
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radios * self.radios
        discriminant = b * b- 4 * c

        if discriminant >=0:
            dist = (-b-sqrt(discriminant))/2
            if dist > 0:
                return dist
        return None
    def normalf(self,surface_point):
        #return the surface on a sphere
        return (surface_point-self.center).normalize()
    
    def compare(self,other):
        if (self.center == other.center and self.radios == other.radios and self.material == other.material):
            return True
        else:
            return False
