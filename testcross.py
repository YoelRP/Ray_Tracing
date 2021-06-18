import unittest
import numpy as np

from vector import Vector

def main():
    v1 = Vector(1.0, 2.0, 3.0)
    v2 = Vector(4.0, 5.0, 6.0)
    v4 = Vector(-3.0, 6.0, -3.0)
    v3 = v1.cross_product(v2)
    print (v3.x, v3.y, v3.z)




if __name__ == "__main__":
    main()