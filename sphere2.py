from math import sqrt

from core import Intersection, dot, point, subtract, transform_from_yaml

from .material import Material
from .shape import Shape


class Sphere(Shape):
    def __init__(self):
        super().__init__()
        self.transformations = []

    @classmethod
    def from_yaml(cls, data):
        sphere = cls()
        sphere.init_from_yaml(data)

        if 'transform' in data:
            sphere.transformations = data['transform']
            sphere.set_transform(transform_from_yaml(data))

        if 'material' in data:
            sphere.material = Material.from_yaml(data)

        return sphere

    def local_intersect(self, local_ray):
        sphere_to_ray = subtract(local_ray.origin, point(0, 0, 0))

        a = dot(local_ray.direction, local_ray.direction)
        b = 2 * dot(local_ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return []

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        i1 = Intersection(t1, self)
        i2 = Intersection(t2, self)
        return [i1, i2]

    def local_normal_at(self, local_point, hit=None):
        return subtract(local_point, point(0, 0, 0))