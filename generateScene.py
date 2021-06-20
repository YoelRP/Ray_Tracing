from vector import Vector
from image import Image
from color import Color
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import ChessMaterial, Material
from triangle import Triangle


class GenerateScene:
    def __init__(self, width=960, height=540, camera=Vector(0, -0.35, -1), rendered_img="2balls1tri.ppm", upset= Point(0,0,0)):
        self.width = width
        self.height = height
        self.rendered_img = rendered_img
        self.camera = camera
        self.upset = upset
        self.objects = [
            #chess plane is just a big sphere
            Sphere(
                1,
                Point(0, 10000.5, 1),
                10000.0,
                ChessMaterial(
                    color1=Color.from_hex("#FFFFFF"),
                    color2=Color.from_hex("#000000"),
                    ambient=0.2,
                    reflection=0.2,
                    ),
                upset
                ),

            Triangle(
                2,
                Point(0,100,100),
                Point(10,11,0),
                Point(10, 10, 11),
                Material(Color.from_hex("#8FFFFF")),
                self.upset
                ),

            Triangle(
                3,
                Point(0,100,100),
                Point(10,0,100),
                Point(100, 10, 11),
                Material(Color.from_hex("#8FFFFF")),
                self.upset
                ),

            Sphere(
                4,
                Point(0.75, -0.10, 1),
                0.6,
                Material(Color.from_hex("#0000FF")),
                self.upset
                ),

            Sphere(
                5,
                Point(-0.75, -0.1, 2.25),
                0.6,
                Material(Color.from_hex("#803980")),
                self.upset
                ),

            ]
        self.lights = [
            Light(Point(1.5, -0.5,-10.0),Color.from_hex("#FFFFFF")),
            Light(Point(-0.5, -10.5, 0 ),Color.from_hex("#E6E6E6"))
            ]
