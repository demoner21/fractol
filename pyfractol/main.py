from PIL import Image

def mandelbrot(x, y, max_iters):
    c = complex(x, y)
    z = 0
    iters = 0
    while abs(z) <= 2 and iters < max_iters:
        z = z*z + c
        iters += 1
    return iters

width = 1024
height = 768
image = Image.new("RGB", (width, height), color=(0, 128,128))
pixels = image.load()

for x in range(width):
    for y in range(height):
        z = mandelbrot(x / width * 3.5 - 2.5, y / height * 2 - 1, 100)
        r = int(255 * z / 100)
        g = int(255 * z / 100)
        b = int(255 * z / 100)
        pixels[x, y] = (r, g, b)

image.show()
