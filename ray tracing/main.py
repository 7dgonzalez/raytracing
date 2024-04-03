#!/usr/bin/env python
"""Daniel - A simple ray tracer"""
import argparse
import importlib
import os
import time 
from multiprocessing import cpu_count

from engine import RenderEngine
from scene import Scene

def main():

    # Parser for command line arguments. Line arguments are used to specify the scene file.
    parser = argparse.ArgumentParser()

    # Add argument for output image file. Image file is the rendered image.
    parser.add_argument("scene", help = "Path to scene file (without .py extension)")

    """-p" and "--processes" argument flags to select the number of processors. Then, we store in the specific
    destination which is processes. Help  provides a description of what the argument does."""
    parser.add_argument("-p", "--processes", action = "store", type = int, dest = "processes", default = 0,
                        help = "Number of processes (0 = auto)",)

    # Add argument for output image file. 
    args = parser.parse_args()

    if args.processes == 0:
        process_count = cpu_count()
    else: 
        process_count = args.processes  
    
    # Import the scene file.
    mod = importlib.import_module(args.scene)

    # Create a scene. 
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    
    # Create a render engine. 
    engine = RenderEngine()

    start = time.time()
    # Save the image to a file. 
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMG, "w") as img_fileobj:
        engine.render_multiprocess(scene, process_count, img_fileobj)

    # End timer
    end = time.time()
    print("Rendering time: {:.2f}s".format(end - start))

if __name__ == "__main__":
    main()