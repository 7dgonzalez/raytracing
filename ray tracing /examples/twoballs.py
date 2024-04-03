from color import Color
from light import Light
from material import ChequeredMaterial, Material
from point import Point
from sphere import Sphere
from vector import Vector

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "two_balls.ppm"
CAMERA = Vector(0, -0.35, -1)

OBJECTS = [
    # Chequered plane is color white and black
    Sphere(Point(0, 10000.5, 1), 10000.0, 
           ChequeredMaterial(color1 = Color.from_hex("#420500"), 
                             color2 = Color.from_hex("#E6B87D"),
                             ambient = 0.2,
                             # Adjust value depending on how much light you want to reflect.
                             reflection = 0.2,
                             ),
                        ),
    # Sphere is color blue
    Sphere(Point(0.75,-0.1,1), 0.6, Material(Color.from_hex("#0000FF"))),
    # Sphere is color pink
    Sphere(Point(-0.75,-0.1,2.25), 0.6, Material(Color.from_hex("#FFC0CB"))),
]

""" List of lights in the scene. Light is a class that takes a Point and a Color."""
LIGHTS = [Light(Point(1.5,-0.5,-10.0), Color.from_hex("#FFFFFF")),
          Light(Point(-0.5,-10.5,0), Color.from_hex("#FFFFFF"))]

