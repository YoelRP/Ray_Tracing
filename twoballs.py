from vector import Vector
from image import Image
from color import Color
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import ChessMaterial, Material
WIDTH = 320
HEIGHT = 200
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
    #chess plane is just a big sphere
    Sphere(
        Point(0, 100000.5, 1), 
        10000.0,
        ChessMaterial(
            color1=Color.from_hex("#FFFFFF"),
            color2=Color.from_hex("#000000"),
            ambient=0.2,
            reflection=0.2
            ),
        ),

    Sphere(Point(0.75, -0.10, 1), 0.6, Material(Color.from_hex("#0000FF"))),

    Sphere(Point(-0.75, -0.1,2.25), 0.6, Material(Color.from_hex("#803980"))),

    ]
LIGHTS = [
    Light(Point(1.5, -0.5,-10.0),Color.from_hex("#FFFFFF")),
    Light(Point(-0.5, -10.5, 0 ),Color.from_hex("#E6E6E6"))
    ]
