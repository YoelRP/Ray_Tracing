#!/usr/bin/env python

import shutil
import tempfile

from vector import Vector
from image import Image
from color import Color
from point import Point
from sphere import Sphere
from generateScene import GenerateScene
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material
from mpi4py import MPI
import argparse
import importlib
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to rendered image")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)
    myScene = GenerateScene()
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    node_name = MPI.Get_processor_name()
    numFramesCam = 1
    numFramesMove = 3
    print(size)
    for i in range(numFramesCam):
        for j in range(numFramesMove):
            CAMERA = Vector(0, i, -1)
            myScene = GenerateScene(480, 270, Vector(0, -1, -i), "2balls1tri.ppm", Point(j, 0, 0))
            if((i % size) == rank):
                print(i)
                print(rank)
                print("cant objetos" + str(range(myScene.objects)))
                scene = Scene(myScene.camera, myScene.objects, myScene.lights,myScene.width, myScene.height)
                engine = RenderEngine()
                image = engine.render(scene)
                os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
                with open("FRAME_i " + str(i) + "j_" + str(j) + mod.RENDERED_IMG, "w") as img_file:
                    image.write_ppm(img_file)
                    

if __name__ == "__main__":

    main()
