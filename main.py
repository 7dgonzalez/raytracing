#!/usr/bin/env python
"""Daniel - A simple ray tracer"""
import argparse
import importlib
import os
import time 

from engine import RenderEngine
from scene import Scene

def main():
    # Parser for command line arguments. Line arguments are used to specify the scene file.
    parser = argparse.ArgumentParser()

    # Add argument for output image file. Image file is the rendered image.
    parser.add_argument("scene", help="Path to scene file (without .py extension)")

    # Add argument for output image file. 
    args = parser.parse_args()

    # Import the scene file.
    mod = importlib.import_module(args.scene)

    # Create a scene. 
    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    
    # Create a render engine. 
    engine = RenderEngine()

    # Start timer.
    start = time.time()

    # Render the scene
    image = engine.render(scene)

    # Save the image to a file. 
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))

    # Open the rendered image file in write mode.
    with open(mod.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)

    # End timer
    end = time.time()
    print("Rendering time: {:.2f}s".format(end - start))

if __name__ == "__main__":
    main()