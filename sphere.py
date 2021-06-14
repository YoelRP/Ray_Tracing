from math import sqrt

class Sphere:
    #is the only 3d shape implemente has a radios,center and material
    def __init__(self, center, radios, material):
        self.center = center
        self.radios = radios
        self.material = material

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
    def normal(self,surface_point):
        #return the surface on a sphere
        return (surface_point-self.center).normalize()