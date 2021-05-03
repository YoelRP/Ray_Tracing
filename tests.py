import numpy as np
from vector import Vector
import unittest

class testVectors(unittest.TestCase):
    def  setup(self):
        self.v1=Vectors(1.0,-2.0,-2.0)

    def  test_magnitude(self):
        self.assertEqual(self.v1.magnitude(),3)

if __name__ == '__main__':
    unittest.main()

#create a vector

#nomalies the vector .