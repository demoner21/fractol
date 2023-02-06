# Pyfractol

Pyfractol is a Python program for rendering fractals using Pygame. It is capable of rendering the Mandelbrot Set and some other fractals.
Requirements

    Pygame
    Numpy
    Numba

## Usage

To run the program, simply execute the main.py file.
```
css

python main.py
```
## Description

The program contains two main classes: Fractal and App. The Fractal class handles the calculations and rendering of the fractal image, while the App class handles the display of the image using Pygame.

The Fractal class uses the Numba library to optimize the calculation of the fractal. The fractal image is stored as a Numpy array and updated with each iteration of the program loop.

The App class creates a Pygame window and runs the program loop, which continually updates and displays the fractal image.
Configuration

The settings for the program can be adjusted in the main.py file. Some of the adjustable settings include the screen resolution, the number of iterations for the fractal calculation, and the zoom level.